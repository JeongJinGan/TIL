def solution(numbers):
    answer = []
    set_ = set() # set을 변수로 쓰고 싶으면 뒤에 _(언더바) 붙여주기
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            n1 = numbers[i]
            n2 = numbers[j]

            sum_ = n1 + n2 # sum도 쓰고 싶으면 언더바 붙이기

            set_.add(sum_)
    # 순서가 없는 set을 순서가 있는 list로 형변환
    list_ = list(set_)        
    answer = sorted(list_)

    return answer  

print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))
