'''
1. 문제 분석
- 며칠만큼 떨어져 있냐는 건 일(day) 수를 계산(같은 월에서는 일을 뺄셈으로 알 수 잇음)
2. 1월 31일은 1월 1일부터 30일(31-1) 만큼 지난 날짜이다.
3. 2월 2일은 1월은 31일이고 2일을 더 지난날이니 31+2=33인데 기준일인 1월 1일 하루를 뺀 일수는 33-1=32일이 된다.
   즉 1월 1일로부터 32일이 지난 날짜이다.

def func_a(month, day):
    month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total = 0
    for i in (          ):
        total += (          )
    total += (          )
    return total - 1

def solution(start_month, start_day, end_month, end_day):
    start_total = func_a(start_month, start_day)
    end_total = func_a(end_month, end_day)
    return end_total - start_total

for문 빈칸 부분은 리스트나 리스트의 요소 번호 범위를 작성하는 곳(range 사용)
total += 변수의 빈칸은 total = total + 빈칸의 값(주로 총합을 구하거나 개수를 셀 때 많이 사용)

코드 분석>
1. 완성해야 할 함수는 func_a 함수이다.
2. func_a 함수는 1월 1일로부터 전달되는 날짜(month, day)까지의 일수를 계산
3. func_a 함수는 전달되는 월(month)의 바로 전 월까지의 일수를 총합한다.
4. 직전 월(month-1)까지의 일 수를 구한 후 전달받은 day를 더하여 일수를 구한다.
5. 계산된 일수에서 1을 뺄셈한 값을 반환한다.
'''
def func_a(month, day):
    month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    #print(len(month_list))     #month_list의 길이(요소 개수) 출력
    total = 0
    #print(total)               #month_list 내 요소들의 총합
    #요소번호 [0]번이 1월이므로 전달받은 month가 3(월)이면 2월인 [1]번까지 반복
    for i in range(month - 1):
        total += month_list[i]
    total += day
    return total - 1            #기준일이 되는 1월 1일로부터 경과된 일수를 계산하는 것이므로 1월 1일 하루를 빼야됨
        
def solution(start_month, start_day, end_month, end_day):
    start_total = func_a(start_month, start_day)
    end_total = func_a(end_month, end_day)
    return end_total - start_total

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
start_month = 1
start_day = 2
end_month = 2
end_day = 2
ret = solution(start_month, start_day, end_month, end_day)

print(ret)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")