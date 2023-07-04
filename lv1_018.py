# Programmers Lv1_018_핸드폰 번호 가리기 

def solution(pn):
    a=list(pn)
    for i in range(len(a[:-4])):
        a[i] = '*'
    return ''.join(a)


# 문자열을 리스트로 만들지 않고, 바로 해결가능하다. 
def solution(pn):
    return '*' * (len(pn) - 4) + pn[-4:]