# while문
a = int(input())
num = 1
total = 1
while num <= a:
    total*=num
    num+=1
print(total)

#for문
a = int(input())
total = 1
for sum in range(1, a+1):
    total *= sum
print(total)