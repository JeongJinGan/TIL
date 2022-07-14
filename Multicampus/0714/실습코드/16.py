word = input()
collection = ['a','e','i','o','u']
cnt = 0
for words in word:
    if words in collection:
        cnt+=1
print(cnt)

# 다른 방법
# word = input()
# cnt = 0
# for char in word:
#     if char in 'aeiou':
#         cnt+=1
# print(cnt)