word = input()
cnt = 0
if 'a' in word:
    for words in range(len(word)):
        if word[words] == 'a':
            print(words)
            break
else:
    print(-1)
        
