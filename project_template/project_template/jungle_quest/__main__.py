# program entry point
import arcade
from game.jungle import Jungle

def main():
    """ Main method """

    
    window = Jungle()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()