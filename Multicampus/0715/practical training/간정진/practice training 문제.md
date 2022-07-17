# 00. 텍스트 데이터 출력(연습)

- 아래의 내용을 00.txt에 기록

### 결과 예시

```bash
N회차 홍길동
Hello, Python!
1일차 파이썬 공부 중
2일차 파이썬 공부 중
3일차 파이썬 공부 중
4일차 파이썬 공부 중
5일차 파이썬 공부 중
```



# 01. 텍스트 데이터 입력(연습)

- 과일 데이터 fruits.txt를 활용하여 총 과일의 갯수를 01.txt 에 기록하시오.
  
  - 과일은 하나당 한 줄에 기록되어 있습니다.

### 결과 예시

```bash
394
```



# 02. 텍스트 데이터 활용 - 특정 단어 추출

- 과일 데이터 fruits.txt를 활용하여 berry로 끝나는 과일의 갯수와 목록을 02.txt 에 기록하시오.
  
  - 과일은 하나당 한 줄에 기록되어 있습니다.

### 결과 예시

```bash
**결순서는 다를 수 있음**

18
Honeyberry
Blackberry
Gooseberry
Juniper berry
Cranberry
Salal berry
Goji berry
Salmonberry
Bilberry
Cloudberry
Huckleberry
Raspberry
Mulberry
Elderberry
Marionberry
Strawberry
Boysenberry
Blueberry
```



# 03. 텍스트 데이터 활용 - 등장 횟수

- 과일 데이터 fruits.txt를 활용하여 과일의 이름과 등장 횟수를 03.txt 에 기록하시오.

### 결과 예시

```bash
**결과 순서는 다를 수 있음**

Boysenberry 3
Blueberry 4
Avocado 1
Marionberry 3
Date 9
...
Melon 1
berryfake 1
```



# 04. JSON 데이터 활용 - 영화 단일 정보

- 영화 데이터 movie.json 을 활용하여 필요한 정보로만 구성된 딕셔너리를 출력하시오.
  
  - 코드는 선언된 함수 내에 작성하며, 결과 딕셔너리를 반환합니다.
  
  - JSON으로 가져온 데이터가 함수의 인자로 전달됩니다.

- id, title, vote_average, overview, genre_ids으로 구성된 결과를 만듭니다.

### 결과 예시

```json
{'genre_ids': [18, 80],
 'id': 278,
 'overview': '촉망받는 은행 간부 앤디 듀프레인은 아내와 그녀의 정부를 살해했다는 누명을 쓴다. 주변의 증언과 살해 현장의 '
             '그럴듯한 증거들로 그는 종신형을 선고받고 악질범들만 수용한다는 지옥같은 교도소 쇼생크로 향한다. 인간 말종 '
             '쓰레기들만 모인 그곳에서 그는 이루 말할 수 없는 억압과 짐승보다 못한 취급을 당한다. 그러던 어느 날, 간수의 '
             '세금을 면제받게 해 준 덕분에 그는 일약 교도소의 비공식 회계사로 일하게 된다. 그 와중에 교도소 소장은 죄수들을 '
             '이리저리 부리면서 검은 돈을 긁어 모으고 앤디는 이 돈을 세탁하여 불려주면서 그의 돈을 관리하는데...',
 'title': '쇼생크 탈출',
 'vote_average': 8.7}
```



# 05. JSON 데이터 활용 - 영화 단일 정보 응용

- 영화 데이터 movie.json 와 genres.json 을 활용하여 필요한 정보로만 구성된 딕셔너리를 출력하시오.
  
  - 코드는 선언된 함수 내에 작성하며, 결과 딕셔너리를 반환합니다.
  
  - JSON으로 가져온 데이터가 함수의 인자로 전달됩니다.

- id, title, vote_average, overview, genre_names로 결과를 만듭니다.
  
  - genre_names는 각 장르 정보를 값으로 가집니다.
  
  - genre_ids를 장르 번호에 맞는 name 값으로 대체합니다.

### 결과 예시

```json
{'genre_names': ['Drama', 'Crime'],
 'id': 278,
 'overview': '촉망받는 은행 간부 앤디 듀프레인은 아내와 그녀의 정부를 살해했다는 누명을 쓴다. 주변의 증언과 살해 현장의 '
             '그럴듯한 증거들로 그는 종신형을 선고받고 악질범들만 수용한다는 지옥같은 교도소 쇼생크로 향한다. 인간 말종 '
             '쓰레기들만 모인 그곳에서 그는 이루 말할 수 없는 억압과 짐승보다 못한 취급을 당한다. 그러던 어느 날, 간수의 '
             '세금을 면제받게 해 준 덕분에 그는 일약 교도소의 비공식 회계사로 일하게 된다. 그 와중에 교도소 소장은 죄수들을 '
             '이리저리 부리면서 검은 돈을 긁어 모으고 앤디는 이 돈을 세탁하여 불려주면서 그의 돈을 관리하는데...',
 'title': '쇼생크 탈출',
 'vote_average': 8.7}
```



# 06. JSON 데이터 활용 - 영화 다중 정보 활용

- 영화 데이터 movies.json 와 genres.json 을 활용하여 필요한 정보로만 구성된 리스트를 출력하시오.
  
  - 코드는 선언된 함수 내에 작성하며, 결과 리스트를 반환합니다.
  
  - JSON으로 가져온 데이터가 함수의 인자로 전달됩니다.

- 전체 영화 정보는 평점 높은 20개의 영화 데이터입니다.
  
  - 개별 영화 데이터는 id, title, vote_average, overview, genre_names로 구성된 딕셔너리입니다.
    
    - genre_names는 각 장르 정보를 값으로 가집니다.
    
    - genre_ids를 장르 번호에 맞는 name 값으로 대체합니다.

### 결과 예시

```json

```


