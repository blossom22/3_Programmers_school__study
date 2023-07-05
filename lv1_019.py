# Programmers Lv1_019_없는 숫자 더하기 

def solution(n):
    a = 0
    for i in range(10):
        if i in n:
            pass
        else:
            a+=i
    return a


# 어차피 n의 원소는 0 ~ 9 사이의 수이므로, 원소들의 합 최대값은 45이다.
# 그렇다면 이렇게 45에서 그냥 원소들의 합을 빼면, n에 없는 원소들의 합을 간단히 구할 수 있다
def solution(n):
    return 45 - sum(n)


print(solution([1,2,3,4,6,7,8,0]))