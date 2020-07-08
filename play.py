import messages


def play(number):
    no = number
    while True:
        guess = input("Welche Zahl bin ich? ")
        if int(guess) == no:
            print(messages.correct)
            exit()
        elif no < int(guess):
            print(messages.lower)
        elif no > int(guess):
            print(messages.higher)
