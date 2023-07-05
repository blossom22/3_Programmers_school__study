# Programmers Lv1_024_약수의 개수와 덧셈 

def solution(left,right):
    b=0
    for i in range(left,right+1):
        a=0
        for j in range(1,i+1):
            if i%j==0:
                a+=1
        if a%2==0:
            b+=i
        else:
            b-=i
    return b

# 위 코드를 더 간결하게 해보았다
def solution(left, right):
    total = 0
    for i in range(left, right+1):
        if int(i**0.5) == i**0.5:   # 만약 i의 제곱근이 정수로 나누어떨어지면, 약수는 홀수개이다
            total -= i
        else:
            total += i
    return total