'''
1. 문제 분석
- 과목별 점수 : 점수들
- 해결 과정
모든 과목 점수의 합을 구함(리스트 요소들을 모두 더하여 반환) > 최고 점수를 구함(리스트 요소들 중 최대값을 찾아 반환 >
최저 점수를 구함(리스트 요소들 중 최소값을 찾아 반환) > (모든 과목 점수의 합) - (최고 점수) - (최저 점수)의 값을 return(반환되는 값을 계산하여 최종적인 결과를 반환

2. 필요한 기능(문법)적 요소들 추리기

def func_a(s):
    ret = 0
    for i in s:
        if i > ret:
            ret = i
    return ret

def func_b(s):
    ret = 0
    for i in s:
        ret += i
    return ret

def func_c(s):
    ret = 101
    for i in s:
        if i < ret:
            ret = i
    return ret

def solution(scores):
    sum = func_ (       )
    max_score = func_ (     )
    min_score = func_ (     )
    return sum - max_score - min_score
'''
def func_a(s):              # 가장 큰 수를 찾는 함수(최고 점수)
    ret = 0                 # 리스트에 저장될 범위보다 작은 값으로 초기화
    for i in s:
        if i > ret:
            ret = i
    return ret

def func_b(s):              # 모든 요소의 합을 구하는 함수
    ret = 0                 # 총합을 저장할 변수
    for i in s:
        ret += i
    return ret

def func_c(s):              # 가장 작은 수를 찾는 함수(최저 점수)
    ret = 101               # 리스트에 저장될 범위보다 큰 값으로 초기화
    for i in s:
        if i < ret:
            ret = i
    return ret

def solution(scores):
    sum = func_b(scores)                    # 모든 과목 점수의 합을 할당
    max_score = func_a(scores)              # 최고 점수를 할당
    min_score = func_c(scores)              # 최저 점수를 할당
    return sum - max_score - min_score      # 모든 과목 점수의 합 - 최고점수 - 최저점수

student_score = solution([50, 35, 78, 91, 85])
print(student_score)