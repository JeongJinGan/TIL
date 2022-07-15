a = int(input())
sum = 0
for i in range(1, a+1):
    sum += i
    if sum >= a:
        break
print(i)
