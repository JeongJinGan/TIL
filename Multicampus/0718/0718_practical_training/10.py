# number_list = [1, 23, 9, 6, 91, 59, 29]
# max = max(number_list)

# number_list2 = [2, 5, 100, 20, 50, 10, 91, 82]
# max2 = max(number_list2)

# if max > max2:
#     print("첫 번째 리스트의 최댓값이 더 큽니다.")

# elif max < max2:
#     print("두 번째 리스트의 최댓값이 더 큽니다.")

# else:
#     print("첫 번째 리스트의 최댓값과 두 번째 리스트의 최댓값은 같습니다.")

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