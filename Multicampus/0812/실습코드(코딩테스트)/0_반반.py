import sys

sys.stdin = open("_반반.txt")

T = int(input())
flag = 1

for _ in range(T):
    words = list(input())
    # print(words)

    for i in words:
        # print(i)
        if words.count(i)  == 2:
            flag = 1
        else:
            flag = 0

    if flag == 1:
        print(f'#{_ + 1} Yes')   
    else:
        print(f'#{_ + 1} No')   