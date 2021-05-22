import random

class Console:
    """A code template for a computer console. The responsibility of this 
    class of objects is to display text output.
    
    Stereotype:
        Service Provider, Interfacer
    """
     
    def displayMan(self, Lives):
        """Gets text input from the user through the screen.

        Args: 
            self (Screen): An instance of Screen.

        Returns:
            Prints the Gameboard.
        """
        if Lives >= 4:
            print("  ___  ")
        if Lives >= 3:
            print(" /___\ ")
        if Lives >= 2:
            print(" \   / ")
        if Lives >= 1:
            print("  \ /  ")
            print("   0   ")
            print("  /|\  ")
            print("  / \  ")
        elif Lives <= 0:
            print("   x   ")
            print("  /|\  ")
            print("  / \  ")
        

    def displayWord(self):
        print(self.secretWord.getProgress())