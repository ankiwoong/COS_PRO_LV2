'''
1. 문제 분석
- 직전 : 바로 전(이미 실행한) / 현재 : 지금 당장(이제 막 실행하려는)
- 바로 전에 저장한 값이 3이면 현재 값은 3
- 문자 'e'를 저장하려고 하는데 바로 직전에 저장한 문자가 'e' 중복이라면 건너띈다.
- 리스트에 [0]번 부터 시작하여 [3]번 까지 저장한 상태라면 [1]번 요소의 직전은 [0]번 요소이며, [2]번 요소의 직전은 [1]번 요소이다.
  현재 저장하려는 요소의 번호가 [i]번이면 직전 요소의 번호는 [i-1]이 된다.
2. 실행 예상
- result에 첫 문자를 저장해 두었다. characters의 [0]번 문자는 이미 저장햇다.
- range 함수를 characters로 바꾸면 for 문을 전부 수정해야 한다.
- i 변수가 0일 때 [i-1]은 마지막 요소이다.
- result에 저장하는 character[i] 번 요소의 직전 요소는 [i-1]번 요소가 맞다.

def solution(characters):
    result = ""
    result += characters[0]
    for i in range(len(characters)):
        if characters[i - 1] != characters[i]:
            result += characters[i]
    return result
'''
def solution(characters):
    result = ""                                     # 빈 문자열을 선언 / solution 함수는 전달받은 문자열을 그대로 반환하는 것이 아니라 문자열에서 일부 문자를 변경 또는 제거 / characters 문자열을 복사 하기 위함
    result += characters[0]                         # 첫 글자이므로 당연히 이전 문자를 판단하지 않고 바로 복사
    for i in range(1, len(characters)):             # i가 1부터 시작하여 1씩 증가 / [0]번 문자는 이미 저장해 둠
        if characters[i - 1] != characters[i]:      # i변수는 characters 리스트의 요소번호로 사용
            result += characters[i]
    return result

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래 코드는 잘못된 부분이 없으니, solution함수만 수정하세요.
characters = "senteeeencccccceeee"
ret = solution(characters)

print(ret)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")