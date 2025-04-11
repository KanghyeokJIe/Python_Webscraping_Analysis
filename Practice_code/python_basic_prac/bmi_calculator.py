kg = int(input("체중(kg) :"))
cm = int(input("키(cm) :"))

BMI = round(kg / ((cm * 0.01) ** 2), 1) # 소수점 첫째자리까지 반올림 - GPT 질문
print("BMI 지수 : ", BMI)