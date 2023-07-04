# Programmers Lv1_011_정수 내림차순으로 배치하기 

def solution(n):
    a = [int(i) for i in str(n)]
    a.sort(reverse=True)        # sort안에 이렇게 입력하면 내림차순이 된다
    return int(''.join(map(str,a)))