import sys

sys.stdin = open("2857.txt", "r")

list_ = []
result = []
for _ in range(5):
    fbi = input()
    list_.append(fbi)

for i in list_:
    # print(i)
    if 'FBI' in i:
        result.append(list_.index(i)+1)

if len(result) == 0:
    print('HE GOT AWAY!')
print(*result)


