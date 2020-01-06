'''
1. 문제 분석
- 작성되어 잇는 코드에서 한 줄만 수정(디버깅 문제)
- 범위가 주어지는 문제는 '이상, 이하, 초과, 미만' 표현을 확인
- 650 이상은 650보다 크거나 같다 / 650 초과는 650보다 크다를 의미
- 650 이상 800 미만 관계연산자 : score >= 650 and score < 800 / 650 <= scroe and score < 800
2. 실행 예상하기
- 하나씩 나누어 동작을 예상
- 연산 기호에 동작을 예상

def solution(scores):
    count = 0
    for s in scores:
        if 650 <= s or s < 800:
            count += 1
    return count
'''
def solution(scores):
    count = 0                           # score 리스트에 저장된 값들 중 '수강대상 조건'에 해당하는 개수를 세어 저장할 변수 / 이 값을 반환 하는것이 목적
    for i in range(len(scores)):
        if 650 <= scores[i] < 800:      # 수강 대상자 조건인 650이상 800미만 점수인지 판단
        # and 연산을 생략 : 650 <= s < 800:
        # and 연산을 사용 : 650 <= s and s < 800:
            count += 1                  # 수강 가능조건 만족이 참일 때 count 변수의 값을 1씩 증가
    return count

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래 코드는 잘못된 부분이 없으니, solution함수만 수정하세요.
scores = [650, 722, 914, 558, 714, 803, 650, 679, 669, 800]
ret = solution(scores)

print(ret)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")