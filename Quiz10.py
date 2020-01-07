'''
1. 문제 분석
- 리스트의 요소가 리스트인 구조
- n x 4 = 행의 개수 n 개에 각 행마다 4개의 요소(a[n][4])
- k 번 반복 한다{
    최소값을 찾는다.
    최소값을 제외한 리스트를 얻는다.
}

2. 필요한 기능(문법)적 요소들 추리기
'''
def solution(arr, k):
    # 2차원 리스트를 1차원 리스트로 변환
    container = []              # 빈 리스트 생성
    for i in arr:
        container += i
    container.sort()            # container 숫자 오름차순 정렬
    return container[k - 1]     # k번째로부터 작은 수를 반환하면 된다. 리스트의 인덱스 시작번호는 0번이므로 k-1

print(solution([[5, 12, 4, 31], [24, 13, 11, 2], [43, 44, 19, 26], [33, 65, 20, 21]], 4))

def solution1(arr, k):
    answer = 0
    temp = []               # arr의 요소들을 모두 복사하여 저장할 리스트(1차)
    for a in arr:
        for b in a:
            temp.append(b)  # b의 값을 temp 리스트에 추가
    temp.sort()             # 리스트를 정렬
    answer = temp[k-1]      # k 번째 작은 수는 [k-1] 번 요소이다.
    return answer