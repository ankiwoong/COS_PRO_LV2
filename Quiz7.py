'''
1. 문제 분석
- 문자열 -> 리스트 / 리스트 -> 문자열
- 어떤 조건이 참일 때와 거짓일 때로 구간을 나눈 방법은 else

2. 코드 실행 예상하기

def solution(s):
    s_list = list(s)
    n = len(s)
    for i in range(n):
        if s_list[i] == 'a':
            s_list[i] = 'z'
        if s_list[i] == 'z':
            s_list[i] = 'a'
    return ''.join(s_list)
'''
def solution(s):
    s_list = list(s)                # 문자열을 리스트화
    n = len(s)                      # 문자열의 길이
    for i in range(n):              # 각각의 요소 값의 대해서 조건문
        if s_list[i] == 'a':        # s_list[i]가 'a'이면(참)
            s_list[i] = 'z'         # s_list[i]의 값이 'z'로 바뀐다.
        elif s_list[i] == 'z':      # s_list[i]가 'z'이면(참)
            s_list[i] = 'a'         # s_list[i]의 값이 'a'로 바뀐다.
    return ''.join(s_list)          # 리스트를 문자열로 변환

print(solution('abz'))