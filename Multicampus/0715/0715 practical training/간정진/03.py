with open('./data/fruits.txt', 'r', encoding='utf-8') as f:
    lines = f.read()
    names = lines.split("\n")
    fruit_name= ''

    dic = {}
    for name in names:
        if name in dic:
            dic[name] +=1
        else:
            dic[name] = 1

    for key in list(dic.keys()):
        print(key, dic[key])

with open('03.txt', 'w', encoding='utf-8') as f:
    for key in list(dic.keys()):
        f.write(f'{key} {dic[key]}\n')