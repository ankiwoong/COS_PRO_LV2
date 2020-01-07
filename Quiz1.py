'''
1. 문제 분석
- 자연수 : 0보다 큰 정수(즉, 1 이상인 양의 정수)
- 5부터 10까지의 총합 계산
1부터 5 - 1인 4까지의 합
= 1 + 2 + 3 + 4 = 10
1부터 10까지의 합
= 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55
1부터 4까지의 합이 10이므로
-> (1 + 2 + 3 + 4) + 5 + 6 + 7 + 8 + 9 + 10
-> (10) + 5 + 6 + 7 + 8 + 9 + 10과 같다
따라서 10을 빼면
-> 5 + 6 + 7+ 8 + 9 + 10과 같다
- n부터 m까지 자연수의 합 (n <= m) / sum = ((n + m) * (m - n + 1)) / 2

2. 필요한 기능(문법)적 요소들 추리기

def func_a(k):
    sum = 0
    for i in range(     ):
        sum += (        )
    return sum

def solution(n, m):
    sum_to_m = func_a(m)
    sum_to_n = func_a(n-1)
    answer = sum_to_m - sum_to_n
    return answer
'''
def func_a(k):
    sum = 0                         # 총합을 저장할 변수
    for i in range(k + 1):          # range(1, k + 1) 동일 / 더할 데이터들의 리스트 또는 range() 범위
        sum += i                    # 하니씩 더하여 총합 계산
    return sum

def solution(n, m):
    sum_to_m = func_a(m)
    sum_to_n = func_a(n-1)
    answer = sum_to_m - sum_to_n
    return answer

print(solution(5, 10))
print(solution(6, 6))