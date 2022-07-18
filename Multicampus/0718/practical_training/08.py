# word = "HappyHacking"

# count = 0

# for char in word:
#     if char == "a" or "e" or "i" or "o" or "u":
#         count += 1

# print(count)

# if 조건 부분에서 주어진 문자열이 모음(aeiou)이 속해있는게 몇개인지를
# 알기위해 ==이 아니라 in을 사용함

# or문법을 올바르게 사용해야한다.
word = "HappyHacking"

count = 0

for char in word:
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
        count += 1

print(count)

# 간단하게는 in을 사용할 수 있다.
# if char in "aeiou":