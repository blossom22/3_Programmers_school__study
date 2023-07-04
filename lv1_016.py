# Programmers Lv1_016_나누어 떨어지는 숫자 배열

def solution(arr, div):
    a = []
    for i in arr:
        if i % div == 0:
            a.append(i)
    if not a:
        return [-1]
    return sorted(a)


# 여담으로, sort()함수 쓸때 주의할 점이 있다. 
# def solution(arr, div):
#   return [i for i in arr if i%div==0].sort()
# 위의 코드를 사용하면 결과가 None이 된다. 
# sort()는 원래의 리스트를 직접 정렬을 하는게 전부이지, 무언가를 반환하지 않는다.
# 그래서 None이 뜨는 것이다. 이 경우, sorted()함수를 쓰면 원래의 리스트는 변경하지 않고
# 정렬된 새로운 리스트를 반환한다
# 아래가 수정한 코드이다.
def solution(arr, div):
    return sorted([i for i in arr if i % div == 0])