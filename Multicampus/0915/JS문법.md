# 문법과 자료형

> JavaScript는 **대소문자를 구별**하며 **유니코드** 문자셋을 이용한다.



```javascript
var 갑을 = "병정";
var Früh = "foobar";
Früh는 früh와 다르다. 대소문자를 구분하기 때문이다.
```

JavaScript에서는 명령을 명령문이라고 부르며, **세미콜론(;)**으로 구분합니다.



## 주석

```javascript
// 한 줄 주석

/* 이건 더 긴,
 * 여러 줄 주석입니다.
 */

/* 그러나, /* 중첩된 주석은 쓸 수 없습니다 */ SyntaxError */
```



## 선언

> JavaScript의 선언에는 3가지 방법이 있습니다.

- var
  - 변수를 선언. 추가로 동시에 값을 초기화.
- let
  - 블록 스코프 지역 변수를 선언. 추가로 동시에 값을 초기화.
- const
  - 블록 스코프 읽기 전용 상수를 선언.



### 변수

> 애플리케이션에서 값에 상징적인 이름으로 변수를 사용합니다. 변수명은 식별자(identifiers)라고 불리며 특정 규칙을 따릅니다.

- JavaScript 식별자는 문자, 밑줄 (`_`) 혹은 달러 기호 (`$`)로 시작해야 하는 반면 이후는 숫자 (`0`–`9`) 일 수도 있습니다.

- JavaScript가 대소문자를 구분하기에, 문자는 "`A`"부터 "`Z`" (대문자)와 "`a`"부터 "`z`" (소문자)까지 모두 포함합니다.

- 적절한 이름으로는 `Number_hits`, `temp99`, `$credit` 및 `_name` 등 입니다.



### 변수 선언

- `var x = 42`와 같이 [`var`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Statements/var) 키워드로 변수를 선언할 수 있습니다. 이 구문은 실행 맥락에 따라 **지역 및 전역 변수**를 선언하는데 모두 사용될 수 있다.

- `let y = 13`와 같이 [`const`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Statements/const) 혹은 [`let`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Statements/let) 키워드로 변수를 선언할 수 있습니다. 이 구문은 블록 스코프 지역 변수를 선언하는데 사용될 수 있습니다. 아래 [변수 스코프](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Grammar_and_types#변수_스코프)를 참고.

- 구조 분해 할당 구문을 사용하여 객체 리터럴에서 값을 풀기 위해 변수를 선언할 수 있습니다. 예를 들면, `let { bar } = foo`. 이 구문은 `bar`라는 이름의 변수를 생성하고 `foo` 객체에 있는 동일한 이름의 키에 해당하는 값을 변수에 할당한다.

  간단히 변수에 값을 할당 할 수도 있습니다. 예를 들어, `x = 42` 와 같은 구문은 **선언되지 않은 전역변수**를 만듭니다. 뿐만 아니라, 자바스크립트의 엄격한 경고를 만들어냅니다. 선언되지 않은 전역변수는 의도되지 않은 동작을 만들어내고는 합니다. 따라서 선언되지 않은 전역변수를 사용하면 안된다.



### 변수 할당

> 지정된 초기 값 없이 `var` 혹은 `let` 문을 사용해서 선언된 변수는 `undefined` 값을 갖는다.
>
> 선언되지 않은 변수에 접근을 시도하는 경우 `ReferenceError` 예외가 발생합니다.

```javascript
var a;
console.log('a 값은 ' + a); // a 값은 undefined

console.log('b 값은 ' + b); // b 값은 undefined
var b;
// 이것은 아래의 '변수 호이스팅'을 읽기 전에는 혼란스러울 수 있음

console.log('c 값은 ' + c); // Uncaught ReferenceError: c is not defined

let x;
console.log('x 값은 ' + x); // x 값은 undefined

console.log('y 값은 ' + y); // Uncaught ReferenceError: y is not defined
let y;
```



### 변수 스코프

> 어떤 함수의 바깥에 변수를 선언하면, 현재 문서의 다른 코드에 해당 변수를 사용할 수 있기에 전역 변수라고 합니다. 만약 함수 내부에 변수를 선언하면, 오직 그 함수 내에서만 사용할 수 있기에 지역 변수라고 부릅니다.

```javascript
if (true) {
  var x = 5;
}
console.log(x); // 5

// 이 동작은 let 선언을 사용하면 바뀐다.
if (true) {
  let y = 5;
}
console.log(y); // ReferenceError: y is not defined
```



### 전역 변수

> 전역 변수는 사실 전역 객체의 속성(property)입니다.
>
> 웹 페이지에서 전역 객체는 `window` 이므로, `windows.variable` 구문을 통해 전역 변수를 설정하고 접근할 수 있습니다.



### 상수

> `const` 키워드로 읽기 전용 상수를 만들 수 있습니다.

```javascript
const PI = 3.14;
```





## 데이터 구조 및 형

### 데이터 형

- 7가지 원시 데이터 형

  1. Boolean. `true`와 `false`
  2. null. null 값을 나타내는 특별한 키워드. (JavaScript는 대소문자를 구분하므로, `null`은 `Null`, `NULL` 혹은 다른 변형과도 다릅니다.)
  3. undefined. 값이 정의되어 있지 않은 최상위 속성.
  4. Number (en-US. 정수 또는 실수형 숫자. 예: `42` 혹은 `3.14159`.
  5. BigInt (en-US). 임의 정밀도의 정수. 예: `9007199254740992n`.
  6. String. 문자열. 예:"안녕"
  7. Symbol. (ECMAScript 2015에 도입) 인스턴스가 고유하고 불변인 데이터 형.
- 그리고 Object(객체)



### 자료형 변환

> JavaScript는 동적 형지정(정형) 언어입니다. 이는 변수를 선언할 때 데이터 형을 지정할 필요가 없음을 의미합니다. 또한 데이터 형이 스크립트 실행 도중 필요에 의해 자동으로 변환됨을 뜻합니다.

 ```javascript
 var answer = 42;
 // 그리고 나중에, 동일한 변수에 문자열 값을 할당할 수도 있습니다. 아래와 같이,
 answer = 'Thanks for all the fish...';
 ```



  ### 숫자와 '+' 연산자

```javascript
x = 'The answer is ' + 42 // "The answer is 42"
y = 42 + ' is the answer' // "42 is the answer"

// 다른 연산자를 포함한 식의 경우, JavaScript는 숫자 값을 문자열로 변환하지 않습니다.
'37' - 7 // 30
'37' + 7 // "377"
```



  ### 문자열을 숫자로 변환하기

> 숫자를 나타내는 값이 문자열로 메모리에 있는 경우, 변환을 위한 메서드가 있습니다.

- parseInt() - 오직 정수만 반환하므로, 소수에서는 사용성이 떨어집니다.
- parseFloat()

```javascript
parseInt('101', 2) // 5

// 문자열을 숫자로 변환하는 대안은 + (단항 더하기) 연산자입니다.
'1.1' + '1.1' // '1.11.1'
(+'1.1') + (+'1.1') // 2.2
// 참고: 괄호는 명확성을 위해 추가, 필요한 것은 아닙니다.
```



## 리터럴

> JavaScript에서 값을 나타내기 위해 리터럴을 사용합니다. 이는 말 그대로 스크립트에 부여한 고정 값으로, 변수가 아닙니다. 이 구획에서는 다음과 같은 형태의 리터럴을 설명합니다.



### 1. 배열 리터럴

> 배열 리터럴은 0개 이상의 식(expression) 목록입니다. 각 식은 배열 요소를 나타내고 대괄호(`[]`)로 묶입니다. 배열 리터럴을 사용하여 배열을 만들 때, 그 요소로 지정된 값으로 초기화되고, 그 `length`는 지정된 인수의 갯수로 설정됩니다.

```javascript
let coffees = ['French Roast', 'Colombian', 'Kona'];
```



#### 배열 리터럴의 추가 쉼표

```javascript
let fish = ['Lion', , 'Angel'];
```

- fish[0]은 "Lion"
- fish[1]은 undefined
- fish[2]는 "Angel"

```javascript
//아래 예제에서, 배열의 length는 4이며, myList[0]과 myList[2]는 값이 빠졌습니다.
var myList = [ , 'home', , 'school'];

// 아래 예제에서, 배열의 length는 4이며, myList[1]과 myList[3]은 값이 빠졌습니다. 마지막 쉼표는 무시됩니다.
var myList = ['home', , 'school', , ];
```



### 2. 불리언 리터럴

> 불리언 형은 `true`와 `false`의 리터럴 값을 가집니다.

  

  ### 3. 숫자 리터럴

> JavaScript 숫자 리터럴은 다른 진법의 정수 리터럴과 10진수의 부동 소수점 리터럴이 포함됩니다.



#### 정수 리터럴

> 정수와 `BigInt`리터럴은 10진수, 16진수, 8진수 및 2진수로 표현될 수 있습니다.

 ```javascript
 // 정수 리터럴
 0, 117, 123456789123456789n             (10진수)
 015, 0001, 0o777777777777n              (8진수)
 0x1123, 0x00111, 0x123456789ABCDEFn     (16진수)
 0b11, 0b0011, 0b11101001010101010101n   (2진수)
 ```



  ### 4. 부동 소수점 리터럴

- 부호없는 10진 정수
- 소수점 ("`.`")
- 소수 (또 다른 10진수)
- 지수

```javascript
// 예시
3.1415926
.123456789
3.1E+12
.1e-23
```



  ### 5. 객체 리터럴

> 객체 리터럴은 중괄호(`{}`)로 묶인 0개 이상인 객체의 속성명과 관련 값 쌍 목록입니다.

```javascript
var sales = 'Toyota';

function carTypes(name) {
  if (name === 'Honda') {
    return name;
  } else {
    return "Sorry, we don't sell " + name + ".";
  }
}

var car = { myCar: 'Saturn', getCar: carTypes('Honda'), special: sales };

console.log(car.myCar);   // Saturn
console.log(car.getCar);  // Honda
console.log(car.special); // Toyota

// 게다가, 속성명으로 숫자나 문자열 리터럴을 사용하거나 또다른 객체 리터럴 내부에 객체를 중첩할 수도 있습니다. 아래 예제는 이 옵션을 사용합니다.
var car = { manyCars: {a: 'Saab', b: 'Jeep'}, 7: 'Mazda' };

console.log(car.manyCars.b); // Jeep
console.log(car[7]); // Mazda
```



  ### 6. 정규식 리터럴

> 정규식 리터럴은 정규식 상세 슬래시(`/`)사이에 감싸인 패턴

```javascript
var re = /ab+c/;
```



### 7. 문자열 리터럴

> 문자열 리터럴은 큰 따옴표(`"`) 혹은 작은 따옴표(`'`)로 묶인 0개 이상의 문자입니다. 문자열은 같은 형 따옴표 (즉 큰 따옴표 쌍이나 작은 따옴표 쌍) 로 구분되어야 합니다.

```javascript
'foo'
"bar"
'1234'
'one line \n another line'
"John's cat"
```





  # 제어문

## 블록문

> 가장 기본적인 명령문은, 명령문들을 그룹으로 묶을 수 있는 **블록문**입니다. 블록문의 블록은 한 쌍의 중괄호로 감싸는 것으로 나타냅니다.

```javascript
{
  statement_1;
  statement_2;
  ⋮
  statement_n;
}
```

### 예제

- 블록문은 제어 흐름 명령문과 많이 사용합니다. (if, for, while)

```javascript
while (x < 10) {
  x++;
}

// 여기서 { x++; }가 블록문입니다.
```



 ## 조건문

> 조건문은 지정한 조건이 참인 경우에 실행하는 명령 집합입니다. JavaScript는 `if...else`와 `switch` 두 종류의 조건문을 지원합니다.



### 1. if...else 문

> 명령문을 논리 조건이 참일 때 실행하려면 `if` 문을 사용하세요. 선택적으로, `else` 절을 추가해서 조건이 거짓인 경우에 실행할 명령문을 지정할 수 있습니다.

```javascript
if (condition) {
  statement_1;
} else {
  statement_2;
}
```

#### - else if 를 사용해서 다수의 조건을 순차적으로 검사할 수도 있다.

```javascript
if (condition_1) {
  statement_1;
} else if (condition_2) {
  statement_2;
} else if (condition_n) {
  statement_n;
} else {
  statement_last;
}

// 모범 사례 
// 일반적으로는 if에 항상, 특히 if 문을 중첩할 때는 블록문을 함께 사용하는 것이 좋습니다.
if (condition) {
  statement_1_runs_if_condition_is_true;
  statement_2_runs_if_condition_is_true;
} else {
  statement_3_runs_if_condition_is_false;
  statement_4_runs_if_condition_is_false;
}
```

  

  #### ❌또한 `if...else`의 조건에 "`x = y`"와 같은 할당은 지양하세요.

```javascript
if ((x = y)) {
  /* 명령문 */
}
```



  ### 거짓 값

> 다음 값은 `false`로 평가됩니다.

- false
- undefined
- null
- 0
- NAN
- 빈 문자열("")

  

#### 예제

- 다음 예제에서, 함수 `checkData`는 `Text` 객체에 포함된 문자의 수가 3이면 `true`를 반환합니다. 그렇지 않으면 경고를 표시한 후 `false`를 반환합니다.

````javascript
function checkData() {
  if (document.form1.threeChar.value.length == 3) {
    return true;
  } else {
    alert(
      '정확히 세 글자를 입력하세요. ' +
      `${document.form1.threeChar.value}은(는) 유효하지 않습니다.`);
    return false;
  }
}
````



  ### 2. switch문

> `switch` 문은 프로그램이 표현식을 평가한 후, 그 값과 `case` 레이블의 값을 비교해 일치하는 `case`의 명령문을 실행합니다.

```javascript
switch (expression) {
  case label_1:
    statements_1;
    break;
  case label_2:
    statements_2;
    break;
    …
  default:
    statements_default;
}
```

- 우선 표현식(`expression`)의 결과와 일치하는 레이블을 가진 `case` 절을 찾아, 관련된 명령문을 실행합니다.

- 일치하는 레이블을 찾지 못했으면 `default` 절을 탐색합니다.

  - `default` 절을 찾았으면 관련된 명령문을 실행합니다.

  - `default` 절을 찾지 못했으면 `switch` 문 바깥의 다음 명령문을 실행합니다.

  - (`default`를 마지막에 배치하는 것은 관습적인 것으로, 사실 위치는 상관 없습니다.)

    

  #### break문

> 각각의 `case`에는 선택적으로 `break` 문을 추가할 수 있습니다. `break`는 `case`의 명령문을 실행한 후에 프로그램이 `switch`의 밖으로 나가도록 합니다. `break`를 생략하면 프로그램은 `switch` 문을 탈출하지 않고, 다음 `case`의 명령문을 실행합니다.

```javascript
switch (fruittype) {
  case '오렌지':
    console.log('오렌지는 파운드 당 $0.59입니다.');
    break;
  case '사과':
    console.log('사과는 파운드 당 $0.32입니다.');
    break;
  case '바나나':
    console.log('바나나는 파운드 당 $0.48입니다.');
    break;
  case '체리':
    console.log('체리는 파운드 당 $3.00입니다.');
    break;
  case '망고':
    console.log('망고는 파운드 당 $0.56입니다.');
    break;
  case '파파야':
    console.log('망고와 파파야는 파운드 당 $2.79입니다.');
    break;
  default:
    console.log(`죄송합니다. ${fruitType}은 품절입니다.`);
}
console.log('더 필요한게 있으신가요?');
```



  

## 예외 처리 명령문

> `throw` 문을 사용하면 예외를 던질 수 있고, 던진 예외는 `try...catch` 문으로 처리할 수 있습니다.

- thorw문
- try...catch문



### 1. throw문

> 예외를 던질 땐 `throw` 문을 사용하세요. `throw`에 던질 값을 지정하면 됩니다.

```javascript
throw 'Error2'; // String
throw 42; // Number
throw true; // Boolean
throw {
  toString: function () {
    return '저는 객체예요';
  },
};
```



### 2. try...catch문

> `try...catch` 문은 실행을 시도할 블록을 표시하고, 그 안에서 예외가 발생할 경우 처리를 맡을 하나 이상의 반응 명령문을 지정합니다. 예외가 발생하면, `try...catch` 문이 잡아냅니다.

```javascript
function getMonthName(mo) {
  mo = mo - 1; // 배열 인덱스에 맞춰 월 조절 (1 = Jan, 12 = Dec)
  let months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
  if (months[mo]) {
    return months[mo];
  } else {
    throw 'InvalidMonthNo'; // 여기서 throw 키워드 사용
  }
}

try {
  // 시도할 명령문
  monthName = getMonthName(myMonth); // 예외가 발생할 수 있는 함수
} catch (e) {
  monthName = 'unknown';
  logMyErrors(e); // 오류 처리기에 예외 객체 전달
}
```



  #### catch 블록

> `try` 블록에서 발생할 수 있는 모든 예외는 `catch` 블록에서 처리할 수 있습니다.

```javascript
catch (catchID) {
  statements;
}

// 아래는 예외를 던지고 잡는 예제 코드입니다. 예외를 던지면 그 순간 제어권이 catch 블록으로 넘어갑니다.
try {
  throw 'myException'; // 예외 생성
} catch (e) {
  // 모든 예외를 처리하기 위한 명령문
  logMyErrors(e); // 오류 처리기에 예외 객체 전달
}
```



  #### finally 블록

> `finally` 블록은 `try`와 `catch` 블록 실행이 끝난 후 이어서, 그리고 `try...catch...finally` 문 이후의 명령문들보다는 먼저 실행할 명령문을 담습니다.

```javascript
openMyFile();
try {
  writeMyFile(theData); // 오류가 발생할 수 있는 코드
} catch (e) {
  handleError(e); // 오류가 발생하면 처리함
} finally {
  closeMyFile(); // 항상 리소스 해제
}
```



#### 예제

```javascript
// 1. 만약 finally 블록이 값을 반환한다면, 그 값이 전체 try...catch...finally 문의 반환 값이 됩니다. try와 catch 블록에서 반환하는 값은 무시합니다.
function f() {
  try {
    console.log(0);
    throw 'bogus';
  } catch (e) {
    console.log(1);
    return true; // finally 블록의 실행이 끝날 때까지 중단됨
    console.log(2); // 접근 불가
  } finally {
    console.log(3);
    return false; // 앞선 return보다 우선함
    console.log(4); // 접근 불가
  }
  // return false가 실행됨
  console.log(5); // 접근 불가
}
console.log(f()); // 0, 1, 3, false

// 2. finally의 반환 값이 우선하는 것은 catch 블록에서 던진 예외에도 적용됩니다.
function f() {
  try {
    throw '예외';
  } catch (e) {
    console.log('내부 "예외" 포획');
    throw e; // finally 블록의 실행이 끝날 때까지 중단
  } finally {
    return false; // 앞선 throw보다 우선함
  }
  // return false가 실행됨
}

try {
  console.log(f());
} catch (e) {
  // 도달 불가능한 catch 블록!
  // f()가 실행되면 `finally`에서 false를 반환함
  // 반환이 catch의 throw보다 우선했으므로 예외가 없음
  console.log('caught outer "bogus"');
}

// 출력 결과
// 내부 "예외" 포획
// false
```



  #### Error 객체 활용하기

> `Error` 객체의 `name`과 `message` 속성으로부터 오류의 유형에 따라 좀 더 정제된 메시지를 가져올 수 있습니다.

```javascript
function doSomethingErrorProne () {
  if (ourCodeMakesAMistake()) {
    throw (new Error('메시지'));
  } else {
    doSomethingToGetAJavascriptError();
  }
}
⋮
try {
  doSomethingErrorProne();
}
catch (e) {
  console.log(e.name); // 'Error' 기록
  console.log(e.message); // '메시지' 또는 JavaScript 오류 메시지 기록
}
```



 



# 반복문(루프와 반복)

  ## for 문

> for 반복문은 어떤 특정한 조건이 거짓으로 판별될 때까지 반복합니다. 자바스크립트의 반복문은 C의 반복문과 비슷합니다.

```javascript
    for ([초기문]; [조건문]; [증감문])
      문장
```



##  do...while 문

> do...while 문은 특정한 조건이 거짓으로 판별될 때까지 반복합니다.

```javascript
    do
      문장
    while (조건문);
```

**조건문을 확인하기 전에 문장은 한번 실행됩니다. 많은 문장을 실행하기 위해선 { }를 써서 문장들을 묶어줍니다. 만약 조건이 참이라면, 그 문장은 다시 실행됩니다. 매 실행 마지막마다 조건문이 확인됩니다. 만약 조건문이 거짓일 경우, 실행을 멈추고 do...while 문 바로 아래에 있는 문장으로 넘어가게 합니다.**

```javascript
// 다음 예제에서, do 반복문은 최소 한번은 반복됩니다. 그리고 i 가 5보다 작지 않을 때까지 계속 반복됩니다.
do {
  i += 1;
  console.log(i);
} while (i < 5);
```



 ## while 문

> while 문은 어떤 조건문이 참이기만 하면 문장을 계속해서 수행합니다.

```javascript
    while (조건문)
      문장
```

```javascript
// 다음 while 반복문은 n이 3보다 작은 한, 계속 반복됩니다.
n = 0;
x = 0;
while (n < 3) {
  n++;
  x += n;
}
```

- 첫번째 경과 후: `n` = 1 and `x` = 1
- 두번째 경과 후: `n` = 2 and `x` = 3
- 세번째 경과 후: `n` = 3 and `x` = 6
- 세번째 경과 후에, n < 3 은 더이상 참이 아니므로, 반복문은 종결됩니다.

```javascript
// 조건문은 항상 거짓이 될지라도 무한 루프는 피해야 합니다. 그렇지 않으면 그 반복문은 영원히 끝나지 않을 것입니다. 아래의 while 문은 조건문이 절대 거짓이 될 수 없으므로 영원히 반복될 것입니다.

// 다음과 같은 코드는 피하세요.
while (true) {
  console.log("Hello, world");
}
```



## 레이블 문

> 프로그램에서 다른 곳으로 참조할 수 있도록 식별자로 문을 제공합니다. 예를 들어, 여러분은 루프를 식별하기 위해 레이블을 사용하고, 프로그램이 루프를 방해하거나 실행을 계속할지 여부를 나타내기 위해 break나 continue 문을 사용할 수 있습니다.

```javascript
    label :
       statement
```

````javascript
// 레이블 markLoop는 while 루프를 식별합니다.
markLoop:
while (theMark == true) {
   doSomething();
}
````



  ## break 문

> break문은 반복문, switch문, 레이블 문과 결합한 문장을 빠져나올 때 사용합니다.

- 레이블 없이 break문을 쓸 때: 가장 가까운 `while`, `do-while`, `for`, 또는 `switch`문을 종료하고 다음 명령어로 넘어갑니다.
- 레이블 문을 쓸 때: 특정 레이블 문에서 끝납니다.

  ```javascript
  // break 문법
  1. break;
  2. break [레이블];
  ```

```javascript
for (i = 0; i < a.length; i++) {
  if (a[i] == theValue) {
    break;
  }
}
```



## continue 문

> `continue` 문은 while, do-while, for, 레이블 문을 다시 시작하기 위해 사용될 수 있습니다.

- 레이블없이 continue를 사용하는 경우, 그것은 가장 안쪽의 while, do-while, for 문을 둘러싼 현재 반복을 종료하고, 다음 반복으로 루프의 실행을 계속합니다. break문과 달리, continue 문은 전체 루프의 실행을 종료하지 않습니다. while 루프에서 그것은 다시 조건으로 이동합니다. for 루프에서 그것은 증가 표현으로 이동합니다.
- 레이블과 함께 continue를 사용하는 경우, continue는 그 레이블로 식별되는 루프 문에 적용됩니다.

  ```javascript
  // continue 문의 구문
  1. continue;
  2. continue label;
  ```

```javascript
// 다음의 예는 i 값이 3일 때 실행하는 continue 문과 함께 while 루프를 보여줍니다. 따라서, n은 값 1, 3, 7, 12를 취합니다.
i = 0;
n = 0;
while (i < 5) {
  i++;
  if (i == 3) {
    continue;
  }
  n += i;
}
```



  ### for...in 문

> `for...in` 문은 객체의 열거 속성을 통해 지정된 변수를 반복합니다. 각각의 고유한 속성에 대해, JavaScript는 지정된 문을 실행

```javascript
for (variable in object) {
  statements
}
```

```javascript
function dump_props(obj, obj_name) {
  var result = "";
  for (var i in obj) {
    result += obj_name + "." + i + " = " + obj[i] + "<br>";
  }
  result += "<hr>";
  return result;
}

// 속성 make와 model을 가진 객체 car의 경우, 결과는 다음과 같습니다:
car.make = Ford
car.model = Mustang
```



## for...of 문

> for...of 문은 각각의 고유한 특성의 값을 실행할 명령과 함께 사용자 지정 반복 후크를 호출하여, 반복 가능한 객체(`배열`, `Map`, `Set`, `인수` 객체 등을 포함)를 통해 반복하는 루프를 만듭니다.

```javascript
  for (variable of object) {
      statement
    }
```

```javascript
// 다음 예는 for...of 루프와 for...in 루프의 차이를 보여줍니다. 속성 이름을 통해 for...in이 반복하는 동안, for...of은 속성 값을 통해 반복합니다.

let arr = [3, 5, 7];
arr.foo = "hello";

for (let i in arr) {
   console.log(i); // logs "0", "1", "2", "foo"
}

for (let i of arr) {
   console.log(i); // logs "3", "5", "7"
}
```





















