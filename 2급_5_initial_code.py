'''
1. 문제 분석
- 리스트에서 역순 처리
2. 필요한 기능(문법)적 요소들 추리기
- 두 변간의 값을 교환

def solution(arr):
    left, right = 0, len(arr)-1
    while (     ):
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr
'''
def solution(arr):
    left, right = 0, len(arr)-1                             # 첫 요소[0] 리스트의 마지막 요소 번호 / 요소번호 초기화
    while left < right:                                     # left는 right보다 작아야 한다.
        # 왼쪽 요소와 오른쪽 요소의 값 교환
        arr[left], arr[right] = arr[right], arr[left]       # 순서 주의
        left += 1                                           # 왼쪽(0번 요소 쪽)에서 오른쪽(마지막 요소 쪽)으로 진행
        right -= 1                                          # 오른쪽(마지막 요소 쪽)에서 왼쪽(0번 요소 쪽)으로 진행
    return arr

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
arr = [1, 4, 2, 3]
ret = solution(arr)

print(ret)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret, " 입니다.")