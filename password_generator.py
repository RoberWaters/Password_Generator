import random


def generate_password():
    capital_letters = ["A", "B", "C", "D", "E", "F", "G", 
    "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
     "S", "T", "U", "V", "W", "X", "Y", "Z" ]
    
    lowercase = ["a", "b", "c", "d", "e", "f", "g", "h", "i",
    "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", 
    "u", "v", "ww", "x", "y", "z"]

    symbols = ["!", "@", "#", "$", "%", "&", "/", "(", ")", "=", 
    "?", "¡", "'", "¿", "_", "-", "*", ">", "<"]

    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

    spaces = [" ", " ", " ", " ", " ", " ", " ", " "]

    characters = capital_letters + lowercase + symbols + numbers +spaces

    password = []

    for i in range(15):
        ramdon_character = random.choice(characters)
        password.append(ramdon_character)

    password = "".join(password)

    return password


def run():
    password = generate_password()
    print("Your suggested password is: " + password)



if __name__ == "__main__":
    run()