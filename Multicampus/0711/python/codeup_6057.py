a,b = input().split()
a = bool(int(a))
b = bool(int(b))
print(not a and not b or a and b)