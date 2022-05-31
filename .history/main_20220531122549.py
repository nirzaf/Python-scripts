
message  = input (">")
words = message.split(' ')
print(words)

emojis = { ":)":"😊"}

output = ""

for word in words:
    emojis.get(word, word)
