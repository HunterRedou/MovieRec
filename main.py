
import sys
import pyfiglet
sys.path.append('/home/philipp/Projects/MovieRec/dataset')
import dataset


def welcome():
    welcome_ASCII = pyfiglet.figlet_format("Welcome", font='slant')
    print(welcome_ASCII)
    print("Hello, this is MovieRec your Number One Movie Recommendation Programm.\n")
    print("In the following we ask a few Questions about what you search for, just\n")
    print("answer the Questions with Yes or No or type the Genres what you like if\n")
    print("the Programm ask for it. So enjoy the Questions.\n")

def questions():
    print("Do you like old Movies?")
    first_input = input()
    if first_input.lower() == "yes":
        print("These are the oldest Movies we have to show you: \n")
        print(oldest_movies)
        print("To make a better Selection please type a Genres that you like. I will still be a Old Movie.")
        user_input = input()
        getting_genre(user_input, old_mo)
    elif first_input.lower() == "no":
        print("These are the newest Movies we have to show you: \n")
        print(newest_movies)
        print("To make a better Selection please type a Genres that you like. I will still be a New Movie.")
        user_input = input()
        getting_genre(user_input, new_mo)
    else:
        return "Sorry I think you got a typo. Only answer with Yes or No."

def main():
    welcome()
    questions()

if __name__ == "__main__":
    main()
