import random

import messages


def ask_for_number():
    # Abfrage der höchsten Spielzahl
    highest = input(messages.give_highest_number)
    print("Wir spielen mit den Zahlen von 0 bis " + highest)
    no = random.randint(0, int(highest))
    print("Test: Meine Zahl ist " + str(no))
    return no
