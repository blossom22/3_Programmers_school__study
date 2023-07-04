# Programmers Lv1_008_자연수 뒤집어 배열로 만들기

def solution(n):
    n = str(n)
    a=[]
    [a.append(int(n[i])) for i in range(len(n)-1,-1,-1)]
    return a


# 불필요한 변수들을 줄여서 이렇게 줄일 수 있다. 
def solution(n):
    return [int(digit) for digit in str(n)][::-1]