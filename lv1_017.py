# Programmers Lv1_017_음양 더하기 

def solution(a, b):
    c=[]
    for i in range(len(b)):
        if b[i] == False:
            c.append(-a[i])
        else:
            c.append(a[i])
    return sum(c)


# 이렇게 간단히 표현할 수 있다. not을 이용해라
def solution(a, b):
    c = [(-a[i] if not b[i] else a[i]) for i in range(len(b))]
    return sum(c)
