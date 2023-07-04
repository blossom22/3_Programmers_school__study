# Programmers Lv1_009_정수 제곱근 판별

def solution(n):
    import math
    m = math.isqrt(n)       # isqrt는 루트를 씌운 값에서 정수값만 출력한다
    if m**2 == n:
        return (m+1)**2
    else:
        return -1