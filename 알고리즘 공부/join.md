### 파이썬 join 함수

**''.join(리스트)**

**'구분자'.join(리스트)**

> join 함수는 매개변수로 들어온 리스트에 있는 요소 하나하나를 합쳐서 하나의 문자열로 바꾸어 반환하는 함수입니다.



ex)

```python
a = ['a', 'b', 'c', 'd', '1', '2', '3']
result1 = "".join(a)
print(result1)
# abcd123
```



```python
a = ['BlockDMask', 'python', 'join', 'example']
result1 = "_".join(a)
print(result1)
# BlockDMask_python_join_example

result2 = ".".join(a)
print(result2)
# BlockDMask.python.join.example
```

