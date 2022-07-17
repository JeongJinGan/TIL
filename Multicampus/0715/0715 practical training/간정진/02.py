with open('./data/fruits.txt','r',encoding='utf-8') as f:
    lines = f.read()
    names = lines.split("\n")
    fruit_name= ''
    list = []
    for name in names:
        #print(name[-5::])
        if name[-5::] == 'berry':
            list.append(name)
    set_list = set(list)  
    print(len(set_list))       
    for i in set_list:
        print(i)
   
with open('02.txt', 'w', encoding='utf-8') as f:
    f.write(f'{len(set_list)}\n')
    for i in set_list:
        f.write(f'{i}\n')
    