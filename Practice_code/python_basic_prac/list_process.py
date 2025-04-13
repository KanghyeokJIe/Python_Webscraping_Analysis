# 질문: ["apple", "banana", "cherry"] 리스트에 "orange"를 추가하세요.
#              [10, 20, 30] 리스트의 모든 요소의 합을 구하세요.
#              [1, 2, 3, 4, 5] 리스트의 요소들을 역순으로 출력하세요.
#              [5, 2, 8, 1, 9] 리스트를 오름차순으로 정렬하세요.

a = ["apple", "banana", "cherry"]
b = [10, 20, 30]
c = [1, 2, 3, 4, 5]
d = [5, 2, 8, 1, 9]

a.append("orange")
print(a)

total_number = sum(b)   # sum() 함수 질문
print(total_number)

c.sort(reverse=True)
print(c)

d.sort()
print(d)
