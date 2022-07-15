a = int(input())
list = [3,6,9]
for i in range(1, a+1):
    if i%10 in list:
        print("X",end=' ')
    else:
        print(i, end =' ')