from pprint import pprint

alpha = {
    'a' : 'apple',
    'b' : 'banana',
    'c' : 'cat',
    'd' : 'apple',
    'e' : 'banana',
    'f' : 'cat',
    'a' : 'apple',
    'b' : 'banana',
    'c' : 'cat',
    'a' : 'apple',
    'b' : 'banana',
    'c' : 'cat'
}
# pprint는 말그대로 prettyprint 예쁘게 줄단위로, 순서대로 출력
pprint(alpha)
print(alpha)
