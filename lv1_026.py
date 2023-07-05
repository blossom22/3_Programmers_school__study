# Programmers Lv1_026_부족한 금액 계산하기 

def solution(price, money, count):
    a = price
    for i in range(count):
        price = a * (i+1)
        money -= price
    if money >= 0:
        return 0
    else:
        return abs(money)