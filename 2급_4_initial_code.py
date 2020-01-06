'''
1. 필요한 기능(문법)적 요소들 추리기
- 리스트에 들어있는 각 자연수의 개수를 세기
- 가장 많이 등장하는 수의 개수 구하기
- 가장 적게 등장하는 수의 개수 구하기
2. 어느 함수를 호출할 것인지와 그 함수에 무엇을 전달해줄 것인가를 찾는다
3. 위에서 하래로 순차적으로 실행됨

def func_a(arr):
    counter = [0 for _ in range(1001)]
    for x in arr:
        counter[x] += 1
    return counter

def func_b(arr):
    ret = 0
    for x in arr:
        if ret < x:
            ret = x
    return ret

def func_c(arr):
    INF = 1001
    ret = INF
    for x in arr:
        if x != 0 and ret > x:
            ret = x
    return ret

def solution(arr):
    counter = func_ (        )
    max_cnt = func_ (        )
    min_cnt = func_ (        )
    return max_cnt // min_cnt
'''
# 자연수의 개수를 세는 함수
def func_a(arr):
    counter = [0 for _ in range(1001)]          # 0으로 초기화된 길이 1001인 리스트
    for x in arr:                               # 전달된 리스트 arr의 자연수들을 하나씩 꺼내어 x에 대입
        counter[x] += 1                         # counter[x]를 1씩 증가 / x는 arr의 요소값이면서 counter의 [요소번호]
    return counter

# 최댓값을 찾는 함수
def func_b(arr):
    ret = 0             
    for x in arr:           # 전달받은 리스트 arr의 길이만큼 반복
        if ret < x:         # x의 값이 ret 값보다 크면
            ret = x         # ret 변수에 x의 값을 저장
    return ret

# 최소값을 찾는 함수
def func_c(arr):
    INF = 1001                      # arr에 저장된 자연수는 1000 이하이다.
    ret = INF
    for x in arr:
        if x != 0 and ret > x:      # x의 값은 1 이상이어야 한다.
            ret = x
    return ret

def solution(arr):
    counter = func_a(arr)           # couner = 함수명(전달인자)
    max_cnt = func_b(counter)       # max_cnt = 함수명(전달인자)
    min_cnt = func_c(counter)       # min_cnt = 함수명(전달인자)
    return max_cnt // min_cnt       # 나눗셈의 결과를 정수로 반환하기 위해 //로 사용 최대 개수가 최소 개수의 몇 배인지 구하여 반환

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
arr = [1, 2, 3, 3, 1, 3, 3, 2, 3, 2]
ret = solution(arr)

print(ret)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")