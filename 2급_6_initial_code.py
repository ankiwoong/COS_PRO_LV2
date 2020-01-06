'''
1. 문제 분석
- number가 60일 때 1부터 60까지 범위에서 3, 6, 9가 포함된 것을 찾아보고 박수를 몇번 쳐야하는지 생각
- 정수를 한 자리씩 쪼개어 특정 값이 있는지를 판단하는 조건식
- 10을 기준으로 자릿수가 늘어나는 것을 곱셈으로, 자릿수가 줄어드는 것을 나눗셈으로 표현
2. 필요한 기능(문법)적 요소들 추리기
- 시작 값에서부터 종료 값까지 1씩 증가하는 변수는 for 문과 range 함수르 이용해 표현
3. temp 변수와 print 함수는 문제 결과와 관계없는 코드

def solution(number):
    count = 0
    for i in range(1, number + 1):
        current = i
        temp = count
        while current != 0:
            if (        ):
                count += 1
                print("짝", end = '')
            current = current // 10
        if temp == count:
            print(i, end = '')
        print(" ", end = '')
    print("")
    return count
'''
def solution(number):
    count = 0                               # count 변에 3, 6, 9의 개수를 세어 저장하므로 처음에 0으로 초기화
    for i in range(1, number + 1):          # 1부터 number까지이므로 range(1, number + 1)로 범위 지정
        current = i                         # i 변수의 값을 current 변수에 복사(3, 6, 9가 잇는지 확인할 대상)
        temp = count                        # count 값을 temp 변수에 복사
        while current != 0:                 # current 변수의 값이 0이면 while 반복이 종료 / 0이 아니면 계속 반복 / 3, 6, 9가 있는지 확인
            if current % 10 == 3 or current % 10 == 6 or current % 10 == 9:     # current % 10은 어떤 정수의 일의 자리값을 확인 / current의 일의 자리값이 '3이거나 6이거나 9이면 참'
                count += 1                  # if 조건이 참이면 count의 값을 1증가
                print("짝", end = '')       # '짝(박수치는 소리)' 출력
            current = current // 10         # current 변수의 값을 계속 10으로 나누어 저장하면서 자릿수를 줄여가는 과정
        if temp == count:                   # 현재값 current(=i)의 정수에는 3, 6, 9가 없었다는 말이 된다.
            print(i, end = '')
        print(" ", end = '')
    print("")                               # 행을 한 줄 내린다
    return count

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
number = 40
ret = solution(number)
print(ret)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")