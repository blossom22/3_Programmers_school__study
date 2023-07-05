# Programmers Lv1_022_수박수박수박수박수박수?  

def solution(n):
    a="수박"
    if n%2==0:
        return a*(n//2)
    else:
        return a*(n//2)+"수"
    

# 아니면 이렇게 풀 수도 있다
def solution(n):
    return "수박"*(n//2) + "수"*(n%2)   