# Programmers Lv1_007_문자열 내 p와 y의 개수 

def solution(s):
    a = 0
    b = 0
    for i in range(len(s)):
        if s[i] == "p" or s[i] == "P":
            a+=1
        elif s[i] == "y" or s[i] == "Y":
            b+=1 
    if a==0 and b==0:
        return True
    elif a==b:
        return True
    else:
        return False
    

# 굳이 위처럼 대문자 소문자 따로 볼 필요는 없다. 그냥 다 소문자로 바꿔놓고 봐도 된다. 중요한 건, p와 y 각각의 개수이니까 가능한 풀이다. 
def solution(s):
    s = s.lower()
    return s.count('p') == s.count('y')