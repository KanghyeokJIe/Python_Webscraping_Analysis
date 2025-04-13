# 두 수와 연산자(+, -, *, /)를 인자로 받아 계산하는 calculator 함수를 작성하세요.
# calculator() 함수를 선언
#     	def calculator(a, b, op):

# GPT 답변변

def calculator(a, b, op):
    result = []
    for i in range(a, b + 1):
        if op == '+':
            result.append(i + i)
        elif op == '-':
            result.append(i - i)
        elif op == '*':
            result.append(i * i)
        elif op == '/':
            result.append(i / i if i != 0 else '0으로 나눌 수 없음')
        elif op == 'square':  # ** 대신 'square' 연산자 사용
            result.append(i * i)
        else:
            result.append("지원되지 않는 연산자")
    return result

# 테스트 실행
if __name__ == "__main__":
    print(calculator(1, 5, 'square'))  # 출력: [1, 4, 9, 16, 25]

    