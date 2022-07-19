# 얕은 복사

a = [1, 2, 3]
b = a 
b[0] = 'hi'

# list 형변환
c = [3, 4, 5]
d = list(c)
d[0] = 'hi'

# 슬라이싱 
e = [4, 5, 6]
f = e[::]
f[0] = 'hi'

# 깊은 복사
a = [[1, 2], 2, 3]
b = list(a)
b[0][0] = 'hi'

print(a) # [[1,2],2,3] or [['hi',2],2,3]
print(b) # [['hi',2],2,3]

import copy
c = [[1, 2], 2, 3]
d = copy.deepcopy(c)
d[0][0] = 'hi'
print(a)
print(b)