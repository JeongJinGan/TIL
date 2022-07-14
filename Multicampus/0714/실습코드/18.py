word = 'banana'
dic = {}
for words in word:
    if words in dic:
        dic[words] +=1
    else:
        dic[words] = 1

for key in list(dic.keys()):
    print(key ,dic[key])

# get메소드를 활용한 방법
# word = 'banana'
# result = {}
# for char in word:
#     result[char] = result.get(char,0) + 1
# print(result)

# for key in list(char.keys()):
#     print(key ,char[key])