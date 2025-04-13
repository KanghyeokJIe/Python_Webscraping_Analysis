# 질문: [70, 85, 90, 55, 78] 리스트에서 합격(60점 이상)한 점수만 출력하세요.

scores = [70, 85, 90, 55, 78]

for cut in scores:
    if cut >= 60:
        print("합격:", cut)