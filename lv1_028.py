# Programmers Lv1_028_행렬의 덧셈 

def solution(arr1, arr2):
    a = []
    for i in range(len(arr1)):
        b = []
        for j in range(len(arr1[i] )):
            b.append(arr1[i][j] + arr2[i][j])
        a.append(b)
    return a