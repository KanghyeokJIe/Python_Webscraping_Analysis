# 질문: 1부터 100까지의 숫자 중 3의 배수의 합을 구하세요.

total = 0
for a in range(1,101):
    if a % 3 == 0:
        total += a
print("3의 배수의 합:",total)