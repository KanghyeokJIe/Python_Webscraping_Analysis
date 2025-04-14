#  ["apple", "banana", "cherry"]에서 각 단어의 길이를 딕셔너리로 만드세요. (딕셔너리 컴프리헨션 사용)
# 출력 : {'apple': 5, 'banana': 6, 'cherry': 6}

a = ["apple", "banana", "cherry"]
a_len = {fruit : len(fruit) for fruit in a}
print(a_len)