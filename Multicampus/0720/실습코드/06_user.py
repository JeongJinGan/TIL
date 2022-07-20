import lotto_class

lotto = lotto_class.Lotto()
lotto.generate_lotto()
print(lotto.numbers)
print(lotto.get_money([1,2,3,4,5,6])) 