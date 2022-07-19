# readline
# with open('students.txt', 'r', encoding='utf-8') as f:
#     for line in f:
#         print(line, end='')
    # lines = f.readline()
    # print(lines, type(lines))
    # lines = f.readline()
    # print(lines, type(lines))
    # lines = f.readline()
    # print(lines, type(lines))
    # lines = f.readline()
    # print(lines, type(lines))
    # lines = f.readline()
    # print(lines, type(lines))




# readlines
with open('students.txt','r',encoding='utf-8') as f:
    lines = f.readlines()
    print(lines, type(lines))