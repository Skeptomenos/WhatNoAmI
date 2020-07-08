import random

from src import messages


def play():
    no = int(ask_for_number())  ## asks user for number to play with
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
        play()
    elif more == "N":
        print("Bis zum nächsten mal!")
        exit()
    else:
        print("Ich habe deine Antwort nicht verstanden. Bitte versuche es noch ein mal.\n")
        finish()


def ask_for_number():
    # Abfrage der höchsten Spielzahl
    highest = int(input(messages.give_highest_number))
    if highest > 0:
        print("Wir spielen mit den Zahlen von 1 bis " + str(highest) + "\n")
        no = random.randint(1, highest)
        print("Test: Ich bin " + str(no) + "\n")
        return no
    else:
        print("Bitte wähle eine Zahl > 0.")
        ask_for_number()
