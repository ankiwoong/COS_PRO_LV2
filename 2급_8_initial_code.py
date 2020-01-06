'''
1. 문제 분석
- 단어, 문장 = 문자열 = 문자들을 요소로 하는 리스트(ex> 'race' > 'r', 'a', 'c', 'e')
- 펠린드롬(회문)
  문자열을 // 2로 나누어 리스트의 [3]번 요소가 가운데 값이 되고 왼쪽의 [0], [1], [2]번 요소 문자와 오른쪽의 [6], [5], [4]번 요소 문자가 순서에 맞추어 같은 경우
  (ex> 'racecar' > 7 // 2 = 3 > [3] 가운데)
  [0]번 문자와 [6]번 문자, [1]번 문자와 [5]번 문자, [2]번 문자와 [4]번 문자가 같은 문자인 경우
  짝수인 경우에는 모든 문자를 비교하여 같은지 확인
- 공백과 마침표를 제거
2. 논리적 판단 능력을 묻는 시험

def solution(sentence):
    str = ''
    for c in sentence:
        if c != '.' or c != ' ':
            str += c
    size = len(str)
    for i in range(size // 2):
        if str[i] != str[size - 1 - i]:
            return False
    return True
'''
def solution(sentence):
    str = ''                                # 빈 문자열을 생성 / sentence에서 일부 문자를 제거한 상태를 만듬
    for c in sentence:                      # sentence에 들어있는 각 문자들을 차례로 c에 대입하여 문자 단위 반복 실행
        if c != '.' and c != ' ':           # c의 변수값이 '.' 이 아니거나 또는 ' '(공백)이 아닌경우
            str += c                        # if문의 조건이 참 'True'이면 str에 문자 c를 더한다
    size = len(str)                         # str 문자열의 길이를 미리 계산
    for i in range(size // 2):              # 펠린드롬 판단 / 리스트의 마지막 요소는 [size -1]
        if str[i] != str[size - 1 - i]:     # i변수는 str 리스트의 요소번호로 사용
            return False                    # 전달받은 문자열이 팰린드롬이 아니다.
    return True                             # 전달받은 문자열이 팰린드롬이다.


#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래 코드는 잘못된 부분이 없으니, solution함수만 수정하세요.
sentence1 = "never odd or even."
ret1 = solution(sentence1)
print(ret1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")
    
sentence2 = "palindrome"
ret2 = solution(sentence2)
print(ret2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")