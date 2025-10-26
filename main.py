
import sys
import pyfiglet
sys.path.append('/home/philipp/Projects/MovieRec/dataset')
from dataset import *


def welcome():
    f = pyfiglet.figlet_format("Welcome", font='slant')
    print(f)


def main():
    welcome()

if __name__ == "__main__":
    main()
