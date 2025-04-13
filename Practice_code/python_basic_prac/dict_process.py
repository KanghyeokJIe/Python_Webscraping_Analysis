# 질문: {"name": "John", "age": 30} 딕셔너리에서 "age"의 값을 출력하세요.
#              {"math": 90, "science": 85, "history": 78} 딕셔너리에서 모든 과목명을 출력하세요.
#              딕셔너리 {'apple': 3, 'banana': 5}에서 apple의 값을 2 증가시키세요.



a = {"name": "John", "age": 30}
b = {"math": 90, "science": 85, "history": 78}
c = {'apple': 3, 'banana': 5}

keys_list = list(b.keys())  # 출력시 dict_keys 삭제하고 list형태로 저장 질문문
c.update({"apple":5})

print("나이:", a.get("age"))
print("과목들:", keys_list)
print(c)