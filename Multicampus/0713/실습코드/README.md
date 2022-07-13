# 01. 기초함수1

## 문제

> 숫자 n을 받아 세제곱 결과를 반환하는 함수 cube를 정의하시오.  
>
> cube 함수를 호출하여 12의 세제곱 결과를 출력하시오

```python
def cube(x):
    return x**3
print(cube(12))
```



# 02. 기초함수2

## 문제

> 가로와 세로의 길이를 각각 a, b로 받아 사각형 넓이와 둘레를 함께 반환하는 함수 rectangle을 정의하시오.  
>
> 사각형이 가로가 20, 세로가 30일 때의 결과를 출력하시오. 
>
> * 사각형 넓이 : 가로 * 세로  * 
> * 사각형 둘레 : (가로 + 세로) * 2

```python
def rectangle(x, y):
    return x*y, (x+y)*2
print(rectangle(20,30))
```

# 09. 득표수 구하기

## 문제

>주어진 리스트가 반장 선거 투표 결과일 때 이영희의 총 득표수를 출력하시오.

```python
students = ['이영희', '김철수', '이영희', '조민지', '김철수', '조민지', '이영희', '이영희']
cnt = 0
for student in students:
    if student == '이영희':
        cnt += 1
print(cnt)
```



# 10. 5의 개수 구하기

## 문제

>주어진 리스트의 요소 중에서 5의 개수를 출력하시오.

```python
numbers = [7, 17, 10, 5, 4, 3, 17, 5, 2, 5]
cnt = 0
for number in numbers:
    if number == 5:
        cnt += 1
print(cnt)
```



# 11. 구구단 출력하기

## 문제

> 2단부터 9단까지 반복하여 구구단을 출력하세요. 
>
> * 문자열 출력시 f-string을 활용하면 편하게 작성할 수 있습니다.

```python
for i in range(2,10):
    print(f'{i}단')
    for j in range(1,10):
        print(f'{i} X {j} = {i*j}')
```



# 12. 문자열 조작하기

## 문제

> 주어진 문자열 word가 주어질 때, 해당 단어에서 ‘a’를 모두 제거한 결과를 출력하시오.

```python
# apple 한정
a = 'apple'
print(a[1:])

# replace사용
a = 'appleelaeell'
new_a = a.replace('a','')
print(new_a)

# for문
word = 'apple'
result = ''
for char in 'apple':
	if char != 'a':
		result = result + char
print(result)    
```



# 13. 문자열 조작하기

## 문제

>주어진 문자열 word가 주어질 때, 해당 단어를 역순으로 뒤집은 결과를 출력하시오.

```python
fruit = 'apple'
print(fruit[::-1])

# for문
word = 'apple'
result = ''
for char in 'apple':
    result = char + result
print(result)  
```





