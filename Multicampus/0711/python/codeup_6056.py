a,b = input().split()
a = bool(int(a))
b = bool(int(b))
print((a and (not b)) or ((not a) and b))