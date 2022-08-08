import sys

sys.stdin = open("2309.txt", "r")
list_ = []
for _ in range(9):
    seven_ = int(input())
    list_.append(seven_)
    sum_ = sum(list_)
for i in range(9):
    for j in range(i+1, 9):
        if sum_ - (list_[i] + list_[j]) == 100:
            lie1 = list_[i]
            lie2 = list_[j]

list_.remove(lie1)
list_.remove(lie2)
list_.sort()

for k in list_:
    print(k)






