'''
1. 문제 분석
- 공식을 확인
- 총합 : 모든 값을 더한 값
- 평균 : 총합을 개수로 나눈 것
- '~ 이하'는 <= 연산으로 표현 / 작거나 같은 / 같거나 작은

2. 필요한 기능(문법)적 요소들 추리기

def solution(data):
    total = sum(data)
    average = len(data) / total
    cnt = 0
    for d in data:
        if d <= average:
            cnt += 1
    return cnt
'''
def solution(data):
    total = sum(data)               # 총합을 저장할 변수
    average = total / len(data)     # average는 실수(float) / 평균 = 총합 / 갯수
    cnt = 0
    for d in data:
        if d <= average:
            cnt += 1
    return cnt

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래 코드는 잘못된 부분이 없으니, solution함수만 수정하세요.
data1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ret1 = solution(data1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")
    
data2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 10]
ret2 = solution(data2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")