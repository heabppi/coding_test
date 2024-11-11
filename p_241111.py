gems = [3, 3, 1, 2, 3, 2, 2, 3, 3, 1]

# 1. gems 리스트에 1이라는 데이터가 존재하는지 여부를 확인하는 로직
# if 1 in gems:
#     print("있다!")
# else:
#     print('없다!')

# for gem in gems:
#     if gem == 1:
#         print("있다!")
#         break
# else:
#     print("없다!")

# for idx in range(len(gems)):
#     if 1 == gems[idx]:
#         print("있다!")
#         break
# else:
#     print("없다")

#####################################################################

# 2. gems의 데이터들을 빈도수대로 집계하는 로직
# 딕셔너리 방법

## 빈 딕셔너리 제작
# counts = {1:0, 2:0, 3:0}

## 반복문을 이용해서 gems를 순회하며 조회하는 데이터를 이용해서
## 딕셔너리에 접근 +1
# for gem in gems:
#     counts[gem] += 1

# print(counts)

# 리스트 방법
## 빈 리스트를 하나 제작한다.
# counts = [0] * 4

# ## 
# for gem in gems:
#     counts[gem] += 1

# print(counts)

###################################################
# 3. nums 리스트에서 가장 큰 수, 가장 작은 수를 뽑는 로직
nums = [-1, 5, 23, 3, 123, 121, 120, 125, 56, -17]

# 최소값, 최대값 설정
# 강사님꺼
# min_num, max_num = -float('INF'), float('INF')

min_num, max_num = 0, 100


# for문을 이용해서 리스트를 순회하며 갱신
for num in nums:
    # 최소값 갱신
    if min_num > num:
        min_num = num
    # 최대값 갱신
    if max_num < num:
        max_num = num
    
print(min_num, max_num)


    