# Convert the emoji converter program to a funciton.
# Fun exercise to display emoji when you give keyboard emojis

message = input("Your message here >> ")

def emoji_converter(message):
    words = message.split(' ')

    # Create a dictionary for emojis
    emojis = {
        ":)": "😊",
        ":(": "🙁",
        "<3": "💖"
    }

    output = ""
    # Use dictionary .get(key, optional word) to simplify the if condition
    for word in words:
        output += emojis.get(word, word) + " "

    return output

print(emoji_converter(message))