message=input('>')
words=message.split(' ')

emojis={
    ':)':'\U0001F60D'
}

output=""
for word in words:
    output+=emojis.get(word,word)+' '

print(output)