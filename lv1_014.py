# Programmers Lv1_014_콜라츠 추측 

def solution(num):
    a = 0
    while num != 1:
        if a >= 500:
            return -1

        if num % 2 == 0:
            num //= 2
        else:
            num = num * 3 + 1
        a += 1
    return a