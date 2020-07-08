import messages
import my_number


def play(number):
    no = int(number)
    while True:
        guess = int(input("Welche Zahl bin ich? "))
        if guess == no:
            print(messages.correct)
            finish()
        elif no < guess:
            print(messages.lower)
        elif no > guess:
            print(messages.higher)


def finish():
    more = input("Möchtest du nochmal spielen? [J/n]").upper()
    if more == "Y" or more == "J":
        play(my_number.ask_for_number())
    elif more == "N":
        print("Bis zum nächsten mal!")
        exit()
    else:
        print("Ich habe deine Antwort nicht verstanden. Bitte versuche es noch ein mal.\n")
        finish()
