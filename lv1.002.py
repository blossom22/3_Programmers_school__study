# Programmers Lv1_002_자릿수 더하기
def solution(n):
    n = str(n)
    a = 0
    for i in range(len(n)):
        a += int(n[i])
    return a


# 그냥 sum으로도 해결가능하다. 
def solution(n):
    a = sum(int(i) for i in str(n))
    return a