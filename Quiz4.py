'''
1. 문제 분석
- 여러 명의 점수를 일정한 구간으로 나누어 문자로 표현
- 각 구간별로 등급 매김
- 학생들의 점수가 저장되어 있고 점수 구간에 따라 학생 수를 세어 저장한 리스트를 반환

2. 필요한 기능(문법)적 요소들 추리기
- 가장 위의 if 조건이 True 이든 False 이든 관계없이 다음 if 조건은 실행
- if 조건이 여러 개이고 첫 조건이 다음 조건에 영향을 주는 경우 사용하는 것이 elif

def solution(scores):
    grade_counter = [0 for i in range(5)]           # 학생들의 수를 세기 위한 리스트를 [0, 0, 0, 0, 0]으로 초기화
    for x in scores:
        if (      ):                                 # A학점
            grade_counter[0] += 1
        elif (      ):                               # B학점
            grade_counter[1] += 1
        elif (      ):                               # C학점
            grade_counter[2] += 1
        elif (      ):                               # D학점
            grade_counter[3] += 1
        else:                                       # F학점
            grade_counter[4] += 1
    return grade_counter
'''
def solution(scores):
    grade_counter = [0 for i in range(5)]           # 학생들의 수를 세기 위한 리스트를 [0, 0, 0, 0, 0]으로 초기화
    """
    grade_count = []
    for i in range(5):                  # range(5)는 [0, 1, 2, 3, 4] 와 같으므로 5번 반복된다.
        grade_counte.append(0)
    """
    for x in scores:
        if x >= 85:                                 # 85점 ~ 100점(A학점)
            grade_counter[0] += 1
        elif x >= 70:                               # 70점 ~ 74점(B학점)
            grade_counter[1] += 1
        elif x >= 55:                               # 55점 ~ 69점(C학점)
            grade_counter[2] += 1
        elif x >= 40:                               # 40점 ~ 54점(D학점)
            grade_counter[3] += 1
        else:                                       # 0점 ~ 39점(F학점)
            grade_counter[4] += 1
    return grade_counter

print(solution([86, 72, 98, 60, 45]))