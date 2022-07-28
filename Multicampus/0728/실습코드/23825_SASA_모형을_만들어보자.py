# https://www.acmicpc.net/problem/23825
import sys

sys.stdin = open("23825_SASA_모형을_만들어보자.txt", "r")

S, A = map(int, input().split())
block_S = S // 2    # 2로 나눈 몫
block_A = A // 2    # 2로 나눈 몫

print(min(block_S, block_A))    # 한쪽만 적게있으면 만들수 없기 때문에 적은 쪽만 생각