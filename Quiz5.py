'''
1. 문제 분석
- 점프 : 이동 점프 = 돌의 개수
- 돌을 하나씩 2번 점프하는 것인가?(한 번에 1칸씩 2번 가라는 의미인가?)
- 돌 2개만큼 1번 점프하는 것인가?(한 번에 2칸 가라는 의미인가?)
- 현재 요소번호와 그 요소의 값을 더하여 다음 요소번호를 구한다.
- 다음 요소번호로 이동하고 이동한 횟수를 센다.
- 현재 요소번호가 리스트의 길이보다 작으면 현재 요소번호와 그 요소의 값을 더하여 다음 요소번호를 구하는것을 반복 아니면 종료

2. 필요한 기능(문법)적 요소들 추리기
- 현재 위치는 개구리가 점프할 때마다 바뀐다.

def solution(stones):
    cnt = 0
    current = 0
    n = len(stones)
    while (     ):
        current += (     )
        cnt += 1
    return cnt
'''
def solution(stones):
    cnt = 0                             # 시작위치는 [0]번 요소(개구리 점프 횟수)
    current = 0                         # 점프할 다음 요소 / stones 리스트의 요소번호(개구리 현재 위치)
    n = len(stones)
    while current < n:                  # 개구리의 현재 위치가 stones 리스트의 길이보다 더 크다면 징검 다리를 모두 건넌 상황
        current += stones[current]      # 개구리가 점프하는 거리는 stones[현재위치]
        cnt += 1                        # 개구리가 점프하는 횟수
    return cnt                          # currnet가 n보다 크거나 같아지면 반복문 종료

print(solution([2, 5, 1, 3, 2, 1]))