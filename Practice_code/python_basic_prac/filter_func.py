#  [10, 20, 30, 40, 50]에서 30보다 큰 수만 필터링하세요. 
#         (filter 함수 사용)

def over30(x):
    return x > 30

numlist = [10,20,30,40,50]
filtering = list(filter(over30, numlist))
print(filtering)