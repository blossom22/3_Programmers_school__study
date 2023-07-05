# Programmers Lv1_021_가운데 글자 가져오기 

def solution(s):
    a = len(s)
    b = a//2
    if a%2==1:
        return s[b]
    else:
        return s[b-1:b+1]