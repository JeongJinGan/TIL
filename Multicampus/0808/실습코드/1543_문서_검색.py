import sys

sys.stdin = open("1543.txt", "r")

doc = input()
find_ = input()
# print(doc.count(find_))
# ababababa
# aba
# ['', 'b', 'ba']  # --> ['', 'b', '', 'ba']

# aaaaaaa
# aa
# ['', '', '', 'a']
result = doc.split(find_)
print(result)
print(len(result)-1)