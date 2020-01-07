'''
1. 문제 분석
- 공항의 방문객 수를 며칠 도안 조사하여 리스트에 저장
- 가장 많은 방문객 수 : 리스트 요소의 값 중에서 가장 큰 최대값
- 두 번째로 많은 방문객 수 : 가장 큰 값을 제외한 나머지 중에서 최대값을 의미

2. 필요한 기능(문법)적 요소들 추리기

def func_a(arr, n):
    ret = []
    for x in arr:
        if x != n:
            ret.append(x)
    return ret

def func_b(a, b):
    if a >= b:
        return a- b
    else:
        return b - a

def func_c(arr):
    ret = -1
    for x in arr:
        if ret < x:
            ret = x
    return ret

def solution(visitor):
    max_first = func_ (     )
    visitor_removed = func_ (       )
    max_second = func_ (        )
    answer = func_ (        )
    return answer
'''
def func_a(arr, n):                 # arr에서 n 값이 같은 요소를 제거한 새로운 리스트를 생성
    ret = []                        # 리스트 객체 생성
    for x in arr:
        if x != n:                  # x가 n이랑 같지 않으면 ret 리스트에 x를 추가
            ret.append(x)
    return ret

def func_b(a, b):                   # 두 정수를 매개변수로 받아 두 수의 차이를 구해 반환
    if a >= b:
        return a- b
    else:
        return b - a

def func_c(arr):                    # arr에 들어있는 모든 요소를 순서대로 검사하면서 발견한 가장 큰 수인 ret보다 x가 크다면 ret를 변경 / 최대값
    ret = -1                        # 전달되는 리스트 arr에는 방문객의 수를 저장한 것으로 모든 요소들이 0 이상의 값이 저장
    for x in arr:
        if ret < x:                 # arr 리스트의 [i]번 요소의 값이 ret보다 크면 그 값을 ret 변수에 덮어씀
            ret = x
    return ret

def solution(visitor):
    max_first = func_c(visitor)                         # 가장 많은 방문객 수 찾기 / visitior 리스트에서 최대값을 반환
    visitor_removed = func_a(visitor, max_first)        # 가장 많은 방문객 수에서 찾은 값을 제외하고 나머지 값들로 새로운 리스트 생성 / visitor에서 max_first 제외
    max_second = func_c(visitor_removed)                # 새로운 리스트에서 가장 많은 방문객 수 찾기 / visitor_removed 리스트의 최대값
    answer = func_b(max_first, max_second)              # 위에서 구한 값의 차이 구하기 / max_first와 max_second 차이
    return answer

print(solution([4, 7, 2, 9, 3]))