def extract_birthday(id_number):
    birth_date = id_number[:6]  # 주민등록번호의 앞 6자리
    year = int(birth_date[:2])  # 연도 (정수로 변환!)
    month = birth_date[2:4]
    day = birth_date[4:6]
    
    # 성별코드로 1900/2000년대 구분 (7번째 자리: 1,2 → 1900 / 3,4 → 2000)
    gender_code = id_number[7]

    if gender_code in ['1', '2']:
        full_year = 1900 + year
    elif gender_code in ['3', '4']:
        full_year = 2000 + year
    else:
        full_year = 1900 + year  # 예외 처리용 (혹시 모를 경우)

    return f"{full_year}년 {month}월 {day}일"


# 입력 받을 때 문자열로 받기
jumin = input("주민등록번호를 입력하세요 (예: yymmdd-nnnnnnn): ")
print(extract_birthday(jumin))