import sys

sys.stdin = open("_문자열의거울상.txt", 'r')

mirror = '' # 거울에 비친 문자열 초기화
T = int(input())    # 전체 테스트 케이스의 수 입력받기

for test_case in range(T):
    words = input() # 문자열 입력받기
    words = words[::-1] # 입력받은 문자 뒤집기
    for word in range(len(words)): # 뒤집은 문자 하나씩 순회
        if words[word] == 'b': # 만약 b라면
            mirror += 'd' # d로 변환 후 문자열 더하기
        elif words[word] == 'd':
            mirror += 'b'
        elif words[word] == 'p':
            mirror += 'q'
        else:
            mirror += 'p'  
    print(f'#{test_case + 1} {mirror}')
    mirror = '' # 출력 후 거울에 비친 문자열 초기화