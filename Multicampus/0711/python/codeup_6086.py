a = int(input())
cnt = int(0)
sum = int(0)
while True:
    cnt +=1
    sum += cnt
    if sum >= a:
        break
print(sum)
