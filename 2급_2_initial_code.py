'''
1. 문제 분석
- 할인받은 금액이 얼마인가?
- 할인된 금액이 얼마인가?
2. 할인받은 금액 : 깍아준 금액을 의미
3. 할인된 금액 : 할인받은 금액을 빼고 실제 지불할 금액
4. 할인율 = (할인액 / 상품액) * 100              = (2,000 / 10,000) * 100 = 0.2 * 100 = 20%
5. 할인 적용된 가격 = 상품액 * (100% - 할인율)   = 10,000 * (1.00 - 0.1) = 9,000원

1) 매개변수의 이해
2) 반환의 이해
'''
#다음과 같이 import를 사용할 수 있습니다.
#import math

# def solution(price, grade):
#     # 여기에 코드를 작성해주세요.
#     answer = 0
#     if grade == 'V':
#         sale = price * 0.15
#         answer += (price - int(sale))
#     elif grade == 'G':
#         sale = price * 0.1
#         answer += (price - int(sale))
#     elif grade == 'S':
#         sale = price * 0.05
#         answer += (price - int(sale))
#     return answer

def solution(price, grade):
    # 여기에 코드를 작성해주세요.
    answer = 0
    # 전달된 문자열 상수 'S' 'G' 'V' 중 하나의 주소와 같으면
    if grade == 'S':
        answer = int(price * 0.95)  # 5% 할인받아 95%만 내면 된다.
    elif grade == 'G':
        answer = int(price * 0.9)   # 10% 할인받아 90%만 내면 된다.
    elif grade == 'V':
        answer = int(price * 0.85)  # 5%를 할인받아 85%만 내면 된다.
    return answer                   # 또는 int(answer)

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
price1 = 2500
grade1 = "V"
ret1 = solution(price1, grade1)
print(ret1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
# print("solution 함수의 반환 값은", ret1, "입니다.")
    
price2 = 96900
grade2 = "S"
ret2 = solution(price2, grade2)
print(ret2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
# print("solution 함수의 반환 값은", ret2, "입니다.")