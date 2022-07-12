# 01. 수 구분하기

## 문제

> 주어진 수 n이 3의 배수이면서 짝수인 경우 ‘참’을 거짓인 경우 ‘거짓'을 출력하시오.

```python
a = int(input())
if a % 3 == 0:
    if a % 2 == 0:
        print("참")
else:
    print("거짓")
```



# 02. 길이 구하기

## 문제

> 문자열 word의 길이를 출력하는 코드를 각각 작성하시오. 
>
> len() 함수를 바로 쓰기보다는 반복문을 활용하세요.

```python
a = input()
num = 0
for words in a:
    num+=1
print(num)
```



# 03. 합 구하기

## 문제

> 1부터 n까지의 합을 구하여 출력하는 코드를 
>
> 1) while 문 2) for 문으로 각각 작성하시오. 
> 2) sum() 함수 사용 금지

```python
# while문
a = int(input())
num = 1
total = 0
while num <= a:
    total+=num
    num+=1
print(total)

#for문
a = int(input())
total = 0
for sum in range(1, a+1):
    total += sum
print(total)
```



# 04. 곱 구하기

## 문제

> 1부터 n까지의 곱을 구하여 출력하는 코드를 
>
> 1) while 문 2) for 문으로 각각 작성하시오.

```python
# while문
a = int(input())
num = 1
total = 1
while num <= a:
    total*=num
    num+=1
print(total)

#for문
a = int(input())
total = 1
for sum in range(1, a+1):
    total *= sum
print(total)
```



# 05. 평균 구하기

## 문제

> 주어진 숫자의 평균을 구하는 코드를 작성하시오. 
>
> sum(), len()  함수 사용 금지

```python
numbers = [3, 10, 20]
avg = int(0)
num = 0
for a in numbers:
    avg += a
    num +=1
print(avg/num)
```



# 06. 최댓값 구하기

## 문제

> 주어진 리스트 numbers에서 최댓값을 구하여 출력하시오.
>
> max() 함수 사용 금지

```python
numbers = [0, 20, 100, 50, -60, 50, 100]
max = numbers[0]
for a in numbers:
    if max < a:
        max = a
print(max)
```



# 07. 최솟값 구하기

## 문제

> 주어진 리스트 numbers에서 최솟값을 구하여 출력하시오. 
>
> min() 함수 사용 금지

```python
numbers = [0, 20, 100]
min = numbers[0]
for a in numbers:
    if min > a:
        min = a
print(min)
```



# 08. 두번째로 큰 수 구하기

## 문제

> 주어진 리스트 numbers에서 두번째로 큰 수를 구하여 출력하시오. 
>
> max() 함수 사용 금지

```python
numbers = [0, 20, 100]
first = numbers[0]
second = numbers[0]

for num in numbers:
    if num > first:
        second = first
        first = num
    if second < num and num < first:
        second = num
print(second)
```



