# Programmers Lv1_031_같은 숫자는 싫어 

# set()을 이용하면 된다. set(리스트)로 set타입으로 변경하면서 중복 제거 > 다시 list형태로 바꾸면된다
def solution(arr):
    a = [arr[0]]
    for i in range(len(arr)-1):
        if arr[i] != arr[i+1]:
            a.append(arr[i+1])
    return a