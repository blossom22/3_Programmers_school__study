# Programmers Lv1_025_문자열 내림차순으로 배치하기 
# 아스키코드를 사용하는 방법
def solution(s):
    a = []
    b = []
    for i in s:
        a.append(ord(i))
    a = sorted(a, reverse=True)
    for i in a:
        b.append(chr(i))
    return ''.join(b)

# 문자열도 정렬이 되므로, 이렇게 하면 훨씬 간단하다
def solution(s):
    return ''.join(sorted(s, reverse=True))
print(solution("Zbcdefg"))
