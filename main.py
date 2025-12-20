
import sys
import pyfiglet
sys.path.append('/home/philipp/Projects/MovieRec/dataset')
import dataset


def welcome():
    welcome_ASCII = pyfiglet.figlet_format("Welcome", font='slant')
    print(welcome_ASCII)
    print("Hello, this is MovieRec your Number One Movie Recommendation Programm.\n")
    print("We have sorted out Movies to your liking with simple Commends you can acess them.\n")
    print("The Commands that you can choose are:\n")
    print("old - To show the oldest Movies in our Dataset.\n")
    print("new - To show the newest Movies in our Dataset.\n")
    print("desi - To show the desicription of a Title.\n")
    print("genre - To show the best Movies out of that Genre.\n")
    print("best - To show the best Movies in our Dataset.\n")
    print("long - To show how much runtime a Movie has.\n")
    print("welcome - To show these Commands again.\n")
    print("end - To end the Programm.\n")


def main():
    welcome()
    run = True
    while run:
        user = input("Please enter a Commend from above:\n")
        if user == "old":
            show_old()
        if user == "new":
            show_new()
        if user == "desi":
            user_input = input("Please enter the Title that you like to see:\n")
            getting_description(user_input)
        if user == "genre":
            user_input = input("Please enter the Genre that you like to see:\n")
            getting_genres(user_input)
        if user == "welcome":
            welcome()
        if user == "best":
            best_in_slot()
        if user == "long":
            user_input = input("Please enter the Title that you like to see:\n")
            runtime_movie(user_input)
        if user == "end":
            run = False

if __name__ == "__main__":
    main()
