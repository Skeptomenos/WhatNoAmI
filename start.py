import messages
import my_number
import play

# Erst Ausgabe und Einführung ins Spiel

print(messages.welcome_message)

no = my_number.ask_for_number()
play.play(no)
