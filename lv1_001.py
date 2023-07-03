# Programmers Lv1_1_나머지가 1이 되는 수 찾기
def solution(n):
    x = 1
    while True:
        if n%x == 1:
            return x
            break
        else:
            x+=1