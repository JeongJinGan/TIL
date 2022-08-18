import sys

sys.stdin = open("17388.txt", "r")

list_ = list(map(int, input().split()))

if sum(list_) >= 100:
    print('OK')
else:
    if min(list_) == list_[0]:
        print('Soongsil')
    elif min(list_) == list_[1]:
        print('Korea')  
    else:
        print('Hanyang')