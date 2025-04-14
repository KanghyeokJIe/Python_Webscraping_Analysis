# 리스트 [1, 2, 3, 4, 5]의 각 요소를 제곱한 새 리스트를 생성하세요.    
#         (List Comprehension 사용)

nums = [1,2,3,4,5]
nums2 = [x * x for x in nums]
print(nums2)