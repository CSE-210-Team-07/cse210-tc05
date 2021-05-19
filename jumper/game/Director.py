from game.SecretWord import SecretWord
from game.HighScore import HighScore
from game.Console import Console

class Director:
    """ A code template that directs the sequence of play.
    Responsibility is to manage the other classes
    
    Stereotype:
        Controller

    Attributes:
        lives (integer): How many lives the user has remaining
        console (Console): an instance of console
        highScore (HighScore): an instance of highScore
        secretWord (SecretWord): an instance of secretWord
    """

    def __init__(self):
        """The class constructor.

        Args:
            self (Director): and instance of Director.
        """
        self.console = Console()
        self.highScore = HighScore()
        self.secretWord = SecretWord()
        self.lives = 4
        self.guess = "a"
    
    def start_game(self):
        """Starts the game loop that controls the sequence of play

        Args:
            self (Director): an instance of Director

        """
        self.console.displayMan(self.lives)
        while self.lives > 0:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Gets the inputs at the beginning of each round.
        determines if user's guess is a character or the
        whole word

        """

        self.guess = input("Guess a letter [a-z]:")
        

    def do_updates(self):
        """Updates game information.  Adds guesses to lists,
        and updates number of lives

        """
        guessLength = len(self.guess)
        if guessLength == 1:
            if self.secretWord.guessLetter(self.guess):
                self.lives += 0
            else:
                self.lives -= 1
        else:
            if self.secretWord.guessWord(self.guess):
                self.lives += 0
            else:
                self.lives -= 1

    def do_outputs(self):
        """Outputs game information. in this case, displays our parachuter
        and the current guesses
        """

        self.console.displayWord()
        self.console.displayMan(self.lives)
