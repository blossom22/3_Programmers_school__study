# Programmers Lv1_027_문자열 다루기 기본 

def solution(s):
    if (len(s)==4 or len(s)==6) and s.isdigit():
        return True
    else:
        return False

def solution(s):
    return s.isdigit() and len(s) in [4,6]