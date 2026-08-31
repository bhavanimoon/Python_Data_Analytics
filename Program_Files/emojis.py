# Fun exercise to display emoji when you give keyboard emojis

message = input("Your message here >> ")
words = message.split(' ')

emojis = {
    ":)": "😊",
    ":(": "🙁",
    "<3": "💖"
}

output = ""

'''
# I wrote this for loop, bit big and unneccessary conditions.
for word in words:
    if emojis.get(word):
        output += emojis.get(word) + " "
    else:
        output += word + " "
'''

# Another way to simplify this for loop
for word in words:
    output += emojis.get(word, word) + " "

print(output)