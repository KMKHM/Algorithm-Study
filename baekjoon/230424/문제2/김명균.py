"""
세 개의 소수 문제
문제: https://www.acmicpc.net/problem/11502
"""
import sys
from itertools import combinations
input = sys.stdin.readline

# 테스트 케이스
t = int(input())

# 최대 정수
limit = 1000

prime = [True]*(limit + 1)

# 아리토스테네스의 체
for i in range(2, int(limit**0.5) + 1):
    if prime[i]:
        for j in range(i*2, limit+1, i):
            prime[j] = False

# 소수값만 추출
possible = []

for i in range(2, 1001):
    if prime[i]:
        possible.append(i)

# print 함수
def print_num(n):
    for i in possible:
        for j in possible:
            for k in possible:
                if i+j+k == n:
                    print(i, j, k)
                    return
    print(0)

for _ in range(t):
    n = int(input())
    print_num(n)



