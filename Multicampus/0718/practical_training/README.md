# 문제 & 해결

# 03. [오류 해결] 입력 받기

## 오류 코드

```python
numbers = input().split()
print(sum(numbers))
```

## Input

```python
10 20
```

## Output

```python
30
```

## 나의 코드

```python
# int 형을 문자열과 합할 수 없다.
# map을 통해 입력받을때, int로 받는다.

numbers = map(int, input().split())
print(sum(numbers))
```


# 04. [오류 해결] 입력 받기 -2

## 오류 코드

```python
words = list(map(int, input().split()))
print(words)
```

## Input

```python
I'm Tutor 6
```

## Output

```python
["I'm", 'Tutor', '6']
```

## 나의 코드

```python
# int형으로 입력을 받고 있지만 각각의 문자열로 출력받으려고 함

words = input().split()
print(words)
```


# 05. [오류 해결] 숫자의 길이 구하기

## 오류 코드

```python
number = 22020718
print(len(number))
```

## Output

```python
8
```

## 나의 코드

```python
# int는 len을 사용할 수 없다.
number = '22020718'
print(len(number))
# number = 22020718
# print(len(str(number)))r))
```



# 06. [오류 해결] 1부터 N까지의 2의 곱 저장하기

## 오류 코드

```python
N = 10
answer = ()
for number in range(N + 1):
    answer.append(number * 2)

print(answer)
```

## Output

```python
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```

## 나의 코드

```python
# 튜플은 append라는게 없어서 사용할 수 없다.

N = 10
answer = []
for number in range(N + 1):
    answer.append(number * 2)

print(answer)
```


# 07. [오류 해결] 평균 구하기

## 오류 코드

```python
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0
count = 0

for number in number_list:
    total += number
count += 1

print(total // count)
```

## Output

```python
5.5
```

## 나의 코드

```python
# count를 for문안에 넣어놓지 않아서 1개씩 진행될때마다 
# 추가해주지 못한다.
# print문의 //연산자는 소수점 이하를 버리기 때문에 /나누기로 출력
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0
count = 0

for number in number_list:
    total += number
    count += 1
print(total / count)
```



# 08. [오류 해결] 모음의 개수 찾기

## 오류 코드

```python
word = "HappyHacking"

count = 0

for char in word:
    if char == "a" or "e" or "i" or "o" or "u":
        count += 1

print(count)
```

## Output

```python
3
```

## 나의 코드

```python
# or문법을 올바르게 사용해야한다.
word = "HappyHacking"

count = 0

for char in word:
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
        count += 1

print(count)

# 간단하게는 in을 사용할 수 있다.
# if char in "aeiou":
```



# 09. [오류 해결] 과일 개수 구하기

## 오류 코드

```python
from pprint import pprint

fruits = [
    "Soursop",
    "Grapefruit",
    "Apricot",
    "Juniper berry",
    "Feijoa",
    "Blackcurrant",
    "Cantaloupe",
    "Salal berry",
]

fruit_count = {}

for fruit in fruits:
    if fruit not in fruit_count:
        fruit_count = {fruit: 1}
    else:
        fruit_count[fruit] += 1

pprint(fruit_count)
```

## Output

```python
{'Apricot': 1,
 'Blackcurrant': 1,
 'Cantaloupe': 1,
 'Feijoa': 1,
 'Grapefruit': 1,
 'Juniper berry': 1,
 'Salal berry': 1,
 'Soursop': 1}
```

## 나의 코드

```python
# fruit_count = {fruit: 1} => 반복문이 돌아갈때마다 기존의 값을 replace한다.
# 그래서 마지막 값만 fruit_count에 저장되게 된다.

from pprint import pprint

fruits = [
    "Soursop",
    "Grapefruit",
    "Apricot",
    "Juniper berry",
    "Feijoa",
    "Blackcurrant",
    "Cantaloupe",
    "Salal berry",
]

fruit_count = {}

for fruit in fruits:
    if fruit not in fruit_count:
        fruit_count [fruit] = 1
    else:
        fruit_count[fruit] += 1
        
pprint(fruit_count)
```



# 10. [오류 해결] 더 큰 최댓값 찾기

## 오류 코드

```python
# 예제 10. [오류 해결] 더 큰 최댓값 찾기

# 문제

> 아래 코드는 리스트에서 최댓값을 구하는 코드입니다.
코드에서 오류를 찾아 원인을 적고, 수정하세요.
> 

## 오류 코드

```pyt
number_list = [1, 23, 9, 6, 91, 59, 29]
max = max(number_list)

number_list2 = [2, 5, 100, 20, 50, 10, 91, 82]
max2 = max(number_list2)

if max > max2:
    print("첫 번째 리스트의 최댓값이 더 큽니다.")

elif max < max2:
    print("두 번째 리스트의 최댓값이 더 큽니다.")

else:
    print("첫 번째 리스트의 최댓값과 두 번째 리스트의 최댓값은 같습니다.")
```

## Output

```python
두 번째 리스트의 최댓값이 더 큽니다.
```

## 나의 코드

```python
# 변수 max와 메소드 max의 명칭이 똑같아서 뭐를 읽어올지 몰라 에러가 난다.
# 변수명을 바꿔준다.
number_list = [1, 23, 9, 6, 91, 59, 29]
number_list_max = max(number_list)

number_list2 = [2, 5, 100, 20, 50, 10, 91, 82]
number_list2_max = max(number_list2)

if number_list_max > number_list2_max:
    print("첫 번째 리스트의 최댓값이 더 큽니다.")

elif number_list_max < number_list2_max:
    print("두 번째 리스트의 최댓값이 더 큽니다.")

else:
    print("첫 번째 리스트의 최댓값과 두 번째 리스트의 최댓값은 같습니다.")
```



# 예제 11. [오류 해결] 영화 정보 찾기

## 오류코드

```python
from pprint import pprint

def movie_info(movie, genres):
    genres_names = []
    genre_ids = movie["genre_ids"]
    for genre_id in genre_ids:
        for genre in genres:
            if genre_id == genre["id"]:
                genre_name = genre["name"]
                genres_names.append(genre_name)

    new_movie_info = {
        "genre_names": genres_names,
        "id": movie["id"],
        "overview": movie["overview"],
        "title": movie["title"],
        "vote_average": movie["vote_average"],
    }



if __name__ == "__main__":
    movie = {
        "adult": False,
        "backdrop_path": "/tXHpvlr5F7gV5DwgS7M5HBrUi2C.jpg",
        "genre_ids": [18, 80],
        "id": 278,
        "original_language": "en",
        "original_title": "The Shawshank Redemption",
        "overview": "촉망받는 은행 간부 앤디 듀프레인은 아내와 그녀의 정부를 살해했다는 누명을 쓴다. 주변의 증언과 살해 현장의 그럴듯한 증거들로 그는 종신형을 선고받고 악질범들만 수용한다는 지옥같은 교도소 쇼생크로 향한다. 인간 말종 쓰레기들만 모인 그곳에서 그는 이루 말할 수 없는 억압과 짐승보다 못한 취급을 당한다. 그러던 어느 날, 간수의 세금을 면제받게 해 준 덕분에 그는 일약 교도소의 비공식 회계사로 일하게 된다. 그 와중에 교도소 소장은 죄수들을 이리저리 부리면서 검은 돈을 긁어 모으고 앤디는 이 돈을 세탁하여 불려주면서 그의 돈을 관리하는데...",
        "popularity": 67.931,
        "poster_path": "/3hO6DIGRBaJQj2NLEYBMwpcz88D.jpg",
        "release_date": "1995-01-28",
        "title": "쇼생크 탈출",
        "video": False,
        "vote_average": 8.7,
        "vote_count": 18040,
    }

    genres_list = [
        {"id": 28, "name": "Action"},
        {"id": 12, "name": "Adventure"},
        {"id": 16, "name": "Animation"},
        {"id": 35, "name": "Comedy"},
        {"id": 80, "name": "Crime"},
        {"id": 99, "name": "Documentary"},
        {"id": 18, "name": "Drama"},
        {"id": 10751, "name": "Family"},
        {"id": 14, "name": "Fantasy"},
        {"id": 36, "name": "History"},
        {"id": 27, "name": "Horror"},
        {"id": 10402, "name": "Music"},
        {"id": 9648, "name": "Mystery"},
        {"id": 10749, "name": "Romance"},
        {"id": 878, "name": "Science Fiction"},
        {"id": 10770, "name": "TV Movie"},
        {"id": 53, "name": "Thriller"},
        {"id": 10752, "name": "War"},
        {"id": 37, "name": "Western"},
    ]

    pprint(movie_info(movie, genres_list))
```

## Output

```python
{'genre_names': ['Drama', 'Crime'],
 'id': 278,
 'overview': '촉망받는 은행 간부 앤디 듀프레인은 아내와 그녀의 정부를 살해했다는  
누명을 쓴다. 주변의 증언과 살해 현장의 '
             '그럴듯한 증거들로 그는 종신형을 선고받고 악질범들만 수용한다는 지옥 
같은 교도소 쇼생크로 향한다. 인간 말종 '
             '쓰레기들만 모인 그곳에서 그는 이루 말할 수 없는 억압과 짐승보다 못한
 취급을 당한다. 그러던 어느 날, 간수의 '
             '세금을 면제받게 해 준 덕분에 그는 일약 교도소의 비공식 회계사로 일하
게 된다. 그 와중에 교도소 소장은 죄수들을 '
             '이리저리 부리면서 검은 돈을 긁어 모으고 앤디는 이 돈을 세탁하여 불려
주면서 그의 돈을 관리하는데...',
 'title': '쇼생크 탈출',
 'vote_average': 8.7}
```

## 나의 코드

```python
# 함수인데 return값이 없다.


from pprint import pprint


def movie_info(movie, genres):
    genres_names = []
    genre_ids = movie["genre_ids"] #genre_ides == [18, 80]
    for genre_id in genre_ids:
        for genre in genres:
            if genre_id == genre["id"]:
                genre_name = genre["name"] #genre_name == drama, crime
                genres_names.append(genre_name) 
                #genres_names == ['drama', 'crime']

    new_movie_info = {
        "genre_names": genres_names,
        "id": movie["id"],
        "overview": movie["overview"],
        "title": movie["title"],
        "vote_average": movie["vote_average"],
    }
    return new_movie_info



if __name__ == "__main__":
    movie = {
        "adult": False,
        "backdrop_path": "/tXHpvlr5F7gV5DwgS7M5HBrUi2C.jpg",
        "genre_ids": [18, 80],
        "id": 278,
        "original_language": "en",
        "original_title": "The Shawshank Redemption",
        "overview": "촉망받는 은행 간부 앤디 듀프레인은 아내와 그녀의 정부를 살해했다는 누명을 쓴다. 주변의 증언과 살해 현장의 그럴듯한 증거들로 그는 종신형을 선고받고 악질범들만 수용한다는 지옥같은 교도소 쇼생크로 향한다. 인간 말종 쓰레기들만 모인 그곳에서 그는 이루 말할 수 없는 억압과 짐승보다 못한 취급을 당한다. 그러던 어느 날, 간수의 세금을 면제받게 해 준 덕분에 그는 일약 교도소의 비공식 회계사로 일하게 된다. 그 와중에 교도소 소장은 죄수들을 이리저리 부리면서 검은 돈을 긁어 모으고 앤디는 이 돈을 세탁하여 불려주면서 그의 돈을 관리하는데...",
        "popularity": 67.931,
        "poster_path": "/3hO6DIGRBaJQj2NLEYBMwpcz88D.jpg",
        "release_date": "1995-01-28",
        "title": "쇼생크 탈출",
        "video": False,
        "vote_average": 8.7,
        "vote_count": 18040,
    }

    genres_list = [
        {"id": 28, "name": "Action"},
        {"id": 12, "name": "Adventure"},
        {"id": 16, "name": "Animation"},
        {"id": 35, "name": "Comedy"},
        {"id": 80, "name": "Crime"},
        {"id": 99, "name": "Documentary"},
        {"id": 18, "name": "Drama"},
        {"id": 10751, "name": "Family"},
        {"id": 14, "name": "Fantasy"},
        {"id": 36, "name": "History"},
        {"id": 27, "name": "Horror"},
        {"id": 10402, "name": "Music"},
        {"id": 9648, "name": "Mystery"},
        {"id": 10749, "name": "Romance"},
        {"id": 878, "name": "Science Fiction"},
        {"id": 10770, "name": "TV Movie"},
        {"id": 53, "name": "Thriller"},
        {"id": 10752, "name": "War"},
        {"id": 37, "name": "Western"},
    ]

    pprint(movie_info(movie, genres_list))
```



# 19. 문제19. 숫자의 길이 구하기

## 문제

> 양의 정수 number가 주어질 때, 숫자의 길이를 구하시오. 양의 정수number를 문자열로 변경하는 것은 금지입니다. str() 사용 금지

## Input

```python
123
```

## Output

```python
3
```

## 나의 코드

```python
a = int(input())
cnt = 0
while a>0:
    a //= 10
    cnt +=1

print(cnt)
```
