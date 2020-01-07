'''
1. 문제 분석
- money - price = 0 이면 money와 price는 같은 값이다.
> 0이면 money가 price보다 큰 값이다.
< 0이면 money가 price보다 작은 값이다.
- 식을 작성하자.
- 물건값 계산하고 거스름돈 받아오기

2. 필요한 기능(문법)적 요소들 추리기

'''
def solution(price, money):
    answer = 0
    total = 0
    for i in price:
        total += i
    answer = money - total
    if answer < 0:
        answer = -1
    return answer

price = solution([5000, 3200, 2100, 800], 10000)
print(price)