import random

import messages


def ask_for_number():
    # Abfrage der höchsten Spielzahl
    highest = int(input(messages.give_highest_number))
    if highest > 0:
        print("Wir spielen mit den Zahlen von 1 bis " + str(highest))
        no = random.randint(1, highest)
        print("Test: Ich bin " + str(no))
        return no
    else:
        print("Bitte wähle eine Zahl > 0.")
        ask_for_number()
