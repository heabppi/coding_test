# 콜라츠 추측
def solution(num):
    n = 0

    while num != 1:
        if n >= 500:
            return -1
        if num % 2 == 0:
            num //= 2
        else:
            num = num * 3 + 1
        n += 1

    return n

# 나누어 떨어지는 숫자 배열
def solution(arr, divisor):

    answer = []
    for ar in arr:
        if ar % divisor == 0:
            answer.append(ar)

    if answer:
        answer.sort()

    else:
        answer = [-1]
    return answer

