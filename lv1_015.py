# Programmers Lv1_015_서울에서 김서방 찾기 

def solution(seoul):
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            return f'김서방은 {i}에 있다'
        


# 그냥 index를 쓰면 간단하게 해결가능하다
# index는 리스트에서 특정 원소의 인덱스값을 찾아준다
def solution(seoul):
    return '김서방은 {}에 있다'.format(seoul.index('Kim'))