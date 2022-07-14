word = 'banana'
for words in word:
    words = ord(words)
    words = chr(words-32)
    print(words, end='')