# Programmers Lv1_030_최대공약수와 최소공배수  

def solution(n, m):
    a=[]
    b = n
    c = m
    while m != 0:
        n,m = m,n%m
    a.append(n)
    a.append((b*c)//n)
    return a
