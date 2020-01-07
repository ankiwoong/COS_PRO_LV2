'''
1. 문제 분석
- 리스트에 저장되어 있는 값 중 특정 값보다 큰 값을 찾는 문제
- ~ 보다 큰 = ~ 초과
- height[i] > 175 또는 175 < height[i]

2. 코드의 실행 예상하기
- 문법적 / 논리적 오류 찾기

def solution(hegit, k):
    answer = 0
    n = len(hegit)
    for h in hegit:
        if h >= k:
            answer += 1
    return answer
'''
def solution(hegit, k):
    answer = 0                  # 키가 k보다 큰 사람의 수
    n = len(hegit)
    for h in hegit:
        if h > k:               # 키가 k보다 큰 사람이므로 키가 k인 사람은 제외
            answer += 1
    return answer

"""
def solution(hegit, k):
    answer = 0
    n = len(hegit)
    index = 0
    while index < n:        # index == n이면 반복 종료
        if height[index] > k:
            answer += 1
        index += 1          # index(요소번호)를 1씩 증가시킨다.
    return answer
"""

print(solution([165, 170, 175, 180, 184], 175))