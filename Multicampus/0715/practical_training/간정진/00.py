with open('00.txt', 'w', encoding='utf-8') as f:
    f.write('N회차 홍길동\n')
    f.write('Hello, Python\n')
    for i in range(1,6):
        f.write(f'{i}일차 파이썬 공부 중!\n')