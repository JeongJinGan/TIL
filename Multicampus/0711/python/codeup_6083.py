a,b,c = map(int, input().split())
cnt = 0
for i in range(0,a):
    for j in range(0,b):
        for k in range(0,c):
            cnt +=1
            print(i,j,k,sep=' ')
print(cnt)