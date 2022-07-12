# numbers = [3, 10, 20]
# avg = int(0)
# num = 0
# for a in numbers:
#     avg += a
#     num +=1
# print(avg/num)


# 강사님 풀이
numbers = [3, 10, 20]
result = 0
count = 0
for number in numbers:
    result += number
    count += 1
print(result/count)
# print(sum(numbers)/len(numbers)) - 물론 쉬운 방법
