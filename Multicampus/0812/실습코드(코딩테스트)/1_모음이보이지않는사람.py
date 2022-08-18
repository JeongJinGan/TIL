import sys

sys.stdin = open("_모음이보이지않는사람.txt")

T = int(input())

vowel = ['a', 'e', 'i', 'o', 'u']

for _ in range(T):
    words = list(input())
    result = ''
    for i in range(len(words)):
        if words[i] in vowel:
            continue
        result += words[i]
    print(f'#{_ + 1} {result}')