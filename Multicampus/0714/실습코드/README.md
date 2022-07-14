# 14. 문자의 갯수 구하기

## 문제

> 문자열 word가 주어질 때, 해당 문자열에서 a 개수를 구하세요. count() 메서드 사용 금지

```python
word = input()
cnt = 0
for words in word:
    if words == 'a':
        cnt+=1
print(cnt)
```



# 15. 문자의 위치 구하기

## 문제

>문자열 word가 주어질 때, 해당 문자열에서 a 가 처음으로 등장하는 위치(index)를 출력해주세요. 
>
>a 가 없는 경우에는 -1을 출력해주세요. find() index() 메서드 사용 금지

```python
word = input()
cnt = 0
if 'a' in word:
    for words in range(len(word)):
        if word[words] == 'a':
            print(words)
            break
else:
    print(-1)
        
```

# 15+. 추가문제

## 문제

>문자열 word가 주어질 때, 해당 문자열에서 a 의 모든 위치(index)를 출력해주세요. 
>
>find() index() 메서드 사용 금지

```python
word = input()
if 'a' in word:
    for words in range(len(word)):
        if word[words] == 'a':
            print(words,end=' ')
else:
    print(-1)
```

# 16. 모음 등장 여부 확인하기

## 문제

>문자열 word가 주어질 때, 해당 문자열에서 모음의 갯수를 출력하시오. 
>
>모음 : a, e, i, o, u  count() 사용 금지

```python
word = input()
collection = ['a','e','i','o','u']
cnt = 0
for words in word:
    if words in collection:
        cnt+=1
print(cnt)
```



# 17. 소문자-대문자 변환하기

## 문제

>소문자로 구성된 문자열 word가 주어질 때, 모두 대문자로 바꾸어 표현하시오. 
>
>.upper(), .swapcase() 사용 금지

```python
word = 'banana'
for words in word:
    words = ord(words)
    words = chr(words-32)
    print(words, end='')
```



# 18. 알파벳 등장 갯수 구하기

## 문제

>문자열 word가 주어질 때, Dictionary를 활용해서 해당 문자열에서 등장한 모든 알파벳 개수를 구해서 출력하세요.

```python
word = 'banana'
dic = {}
for words in word:
    if words in dic:
        dic[words] +=1
    else:
        dic[words] = 1

for key in list(dic.keys()):
    print(key ,dic[key])
```

