# 파일이름 : 2차과제 코드 작성
# 작 성 자 : 김강민

chicken_data = []

print("--- 🍗 닭가슴살 정밀 영양 판독기 V2.0 ---")

product_name = input("제품명을 입력하세요: ")
chicken_data.append(product_name)

weight = int(input("중량(g)을 입력하세요: "))
chicken_data.append(weight)

protein = float(input("총 단백질 함량(g)을 입력하세요: "))
chicken_data.append(protein)

price = int(input("가격을 입력하세요(원): "))
chicken_data.append(price)

efficiency = chicken_data[3] / chicken_data[2]

grade = ""
title = ""

if efficiency <= 60 and chicken_data[2] >= 25:
    # 단백질 1g당 60원 이하이면서 총 단백질이 25g 이상일 때 (최상위 조건)
    grade = "S등급"
    title = "🏆 [득근 마스터] 갓성비와 고단백을 모두 잡았습니다!"
elif efficiency <= 75:
    grade = "A등급"
    title = "👍 [훌륭한 선택] 가성비가 아주 좋습니다."
elif efficiency <= 100:
    grade = "B등급"
    title = "🙂 [무난함] 평범한 닭가슴살입니다."
else:
    grade = "C등급"
    title = "💸 [지갑 주의] 단백질 대비 가격이 다소 비쌉니다."

# 5. 최종 결과 출력
print(f"\n======================================")
print(f"[{chicken_data[0]}] 분석 결과")
print(f"======================================")
print(f"입력된 데이터: {chicken_data}")
print(f"단백질 1g당 가격: {efficiency:.1f}원")
print(f"판정 등급: {grade}")
print(f"코멘트: {title}")
print(f"======================================")
