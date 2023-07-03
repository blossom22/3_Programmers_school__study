# Programmers Lv1_005_약수의 합

def solution(n):
    a = 0
    for i in range(1,n+1):
        if n%i==0:
            a+=i
    return a


# 아래처럼 간결하게 표현할 수 있다. 
def solution(n):
    return sum(i for i in range(1, n+1) if n % i == 0)