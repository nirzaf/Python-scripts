
message  = input (">")
words = message.split(' ')
print(words)

emojis = { ":)":"😊"}

for word in words:
    emojis.get(word)
