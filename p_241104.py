# 내적
def solution(a, b):
    return sum(a_ * b_ for a_, b_ in zip(a,b))

# 가운데 글자 가져오기
def solution(s):
    if len(s) % 2 == 0:
        center = len(s) // 2
        return s[center-1:center+1]
    else:
        center = len(s) // 2
        return s[center]
    
# 좋았다고 생각되는 코드
def string_middle(str):
    return str[(len(str)-1)//2 : len(str)//2+1]
