word = input()
if 'a' in word:
    for words in range(len(word)):
        if word[words] == 'a':
            print(words,end=' ')
else:
    print(-1)

# append를 이용한 방법  
# word = input()
# result = []
# for words in range(len(word)):
#     if word[words] == 'a':
#         result.append(words)
# print(result)
    