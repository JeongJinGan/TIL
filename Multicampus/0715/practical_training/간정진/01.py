with open('./data/fruits.txt','r',encoding='utf-8') as f:
    lines = f.read()
    names = lines.split("\n")
    cnt = 0
    for name in names:
        cnt +=1
    print(cnt)
# f.close()    
with open('01.txt', 'w', encoding='utf-8') as f:
    f.write(str(cnt))
    