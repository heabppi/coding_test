import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
cnt = 0

# 포인터 초기화(세팅)
l, r = 0, 0
tmp = 0

while True:
    # tmp < M
    if tmp < M:
        # r값이 끝에 도달했다면?
        if r == N:
            # 종료
            break
        # 오른쪽 포인터가 가리키는 값을 tmp에 더하고
        tmp += nums[r]
        # 오른쪽 포인터 이동
        r += 1

    # tmp > M
    elif tmp > M:
        # 왼쪽 포인터가 가리키는 값을 tmp에서 빼고
        tmp -= nums[l]
        # 왼쪽 포인터 이동
        l += 1

    # tmp == M
    elif tmp == M:
        # cnt += 1
        cnt += 1
        # 왼쪽 포인터가 가리키는 값을 tmp에서 빼고
        tmp -= nums[l]
        # 왼쪽 포인터 이동
        l += 1

print(cnt)


###############################################################

# 수열
import sys
input = sys.stdin.readline

N, K = map(int, input.split())
nums = list(map(int, input().split()))

# 일단 첫번째 구간의 합은 구해놓는다
ans = sum(nums[:K])

# N-K+1번 반복
for i in range(N-K):
    # 해당 구간의 합을 구하고
    # tmp = sum(nums[i:i+K])
    tmp = tmp - nums[i] + nums[i+K]
    # 정답을 갱신
    ans = max(ans, tmp)

print(ans)


#########################################################3

# 구간합 구하기

import sys
input = sys.stdin.readline
from itertools import accumulate

nums = [3, 5, 1, 4, 2]
acc = [0]
for num in nums:
    acc.append(acc[-1] + num)

print(acc)

# accumulate는 리스트 0이 없어서
acc2 = [0] + list(accumulate(nums))

print(acc2)