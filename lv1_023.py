# Programmers Lv1_023_내적 

def solution(a, b):
    c = len(a)
    d = 0
    for i in range(c):
        d += a[i]*b[i]
    return d

# zip 내장함수로 해결가능하다
def solution(a, b):
    return sum(x*y for x,y in zip(a,b))
# zip()함수는 iterable 객체를 인자로 받고, 각 객체의 원소를 튜플형태로 반환한다 
