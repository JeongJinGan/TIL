import sys

sys.stdin = open("6996.txt", "r")

for i in range(int(input())):
    word1, word2 = map(str, input().split())

    r_list1 = sorted(list(word1))
    r_list2 = sorted(list(word2))
    
    if r_list1 == r_list2:
        print(f'{word1} & {word2} are anagrams.')
    else:
        print(f'{word1} & {word2} are NOT anagrams.')
