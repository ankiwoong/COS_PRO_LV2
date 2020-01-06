'''
1. 문제 분석
2. 단체 티셔츠 주문하기
3. 학생별로 원하는 티셔츠 사이즈를 조사
4. 작은 순서대로 'XS', 'S', 'M', 'L', 'XL', 'XXL' 총 6종류
5. 학생별로 원하는 티셔츠 사이즈를 조사한 결과가 들어있는 리스트 shirt_size가 매개 변소로 주어질 때
6. 사이즈별로 티셔츠가 몇 벌씩 필요한지 가장 작은 사이즈부터 순서대로 리스트에 담아 return 하도록 solution 함수를 완성

1) 매개변수의 이해
2) 반환의 이해
'''

#다음과 같이 import를 사용할 수 있습니다.
import math

def solution(shirt_size):
    #여기에 코드를 작성해주세요.
    # _ : for 실행에서 별도의 변수는 사용하지 않음(시험에서 자주 사용)
    size_counter = [0 for _ in range(6)]    # [0, 0, 0, 0, 0, 0] 으로 해도 상관 없음
    for size in shirt_size:
        if size == "XS":                    # 반드시 if로 시작
            size_counter[0] += 1            # 가장 작은 사이즈의 개수는 [0]번에 저장
        elif size == 'S':                   # 위에 if size == 'XS'가 False 일 때만 실행
            size_counter[1] += 1
        elif size == 'M':                   # 위 조건이 True이면 elif는 실행하지 않고 건너뛴다.
            size_counter[2] += 1
        elif size == 'L':
            size_counter[3] += 1
        elif size == 'XL':
            size_counter[4] += 1
        elif size == 'XXL':
            size_counter[5] += 1            # 가장 큰 사이즈의 개수는 [5]번에 저장
    return size_counter

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
shirt_size = ["XS", "S", "L", "L", "XL", "S"]
ret = solution(shirt_size);

print(ret)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
# print("solution 함수의 반환 값은 ", ret, " 입니다.")