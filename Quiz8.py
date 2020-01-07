'''
1. 문제 분석
- 문자열 내에서 'j'와 'k'를 찾아 처리하는 함수를 완성
- '들어가는' = '포함된'

2. 코드 실행 예상하기

def solution(name_list):
    answer = 0
    for name in name_list:
        for n in name:
            if n == 'j' or n == 'k':
                answer += 1
                continue        # continue는 이 코드에서 의미가 없다.
    return answer
'''
def solution(name_list):
    answer = 0
    for name in name_list:
        for n in name:
            if n == 'j' or n == 'k':
                answer += 1
                break                   # 현재 검사하는 이름의 철자 중'j'또는 'k'를 한번이라도 만나면 사람 수를 1증가 시키고 for를 빠져나가게 하면 되므로 break
    return answer

print(solution(['james', 'luke', 'oliver', 'jack']))