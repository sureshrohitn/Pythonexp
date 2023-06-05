def emoji(message):
    words = message.split(' ')

    emojis = {
        ':)': '\U0001F60D'
    }

    output = ""
    for word in words:
        output += emojis.get(word, word) + ' '
    return output

message = input('>')

print(emoji(message))
