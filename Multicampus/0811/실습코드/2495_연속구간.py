import sys

sys.stdin = open("2495.txt", "r")

list_ = []

for _ in range(3):
    nums = input()
    cnt = 1
    max_ = 1
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            cnt += 1
        else:
            max_ = max(cnt, max_)
            cnt = 1

    max_ = max(cnt, max_)
    print(max_)


