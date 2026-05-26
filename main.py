# 파일이름 : 3차과제 코드 작성
# 작 성 자 : 김강민

chicken_database = []

def input_chicken() :
    global chicken_database
    print("\n---[1] 닭가슴살 정보 입력 ---")

    name = input("제품명을 입력하세요: ")
    weight = int(input("중량(g)을 입력하세요: "))
    protein = float(input("총 단백질 함량(g)을 입력하세요: "))
    price = int(input("가격을 입력하세요(원): "))
    
    chicken_database.append([name, weight, protein, price])
    print(f" ✅ '{name}' 제품이 성공적으로 식단에 등록되었습니다.")

def show_all_chickens():
    print("\n--- [2] 전체 식단 목록 조회 ---")
    
    if not chicken_database:
        print("📢 등록된 닭가슴살 데이터가 없습니다. 먼저 데이터를 입력해 주세요.")
        return
        
    total_price = 0
    print("-" * 50)

    for i in range(len(chicken_database)):
        product = chicken_database[i]
        print(f"{i+1}번 제품: {product[0]} ({product[1]}g) | 단백질: {product[2]}g | 가격: {product[3]}원")
        total_price += product[3]

    print("-" * 50)
    print(f" 💰 현재까지 등록된 닭가슴살 총 구매 비용 : {total_price}원")

def calculate_efficiency(product_info):
    efficiency = product_info[3] / product_info[2]
    return efficiency

def run_diet_analysis():
    print("\n--- [3] 영양 성분 및 가성비 종합 분석 ---")

    if not chicken_database:
        print(" 📢 분석할 데이터가 없습니다. 먼저 데이터를 입력해주세요.")
        return

    for product in chicken_database:
        if product[2] < 15.0 :
            print(f" ⚠️ [{product[0]}] 제품은 단백질이 너무 적어 가성비 분석에서 제외(스킵)합니다.")
            continue

        eff_value = calculate_efficiency(product)
        grade = ""
        title = ""

        if eff_value <= 60 and product[2] >= 25:
            grade = "S등급"
            title = " 🏆 [득근 마스터] 갓성비와 고단백을 모두 잡았습니다!!"
        elif eff_value <= 75:
            grade = "A등급"
            title = " 👍 [훌륭한 선택] 가성비가 아주 좋습니다."
        elif eff_value <= 100:
            grade = "B등급"
            title = "🙂 [무난함] 평범한 수준의 닭가슴살입니다."
        else:
            grade = "C등급"
            title = "💸 [텅장 주의] 단백질 대비 가격이 다소 비쌉니다."

        print(f" ▶ [{product[0]}] 단백질 1g당 가격: {eff_value:.1f}원 -> {grade} | {title}")


while True:
    print("\n========== 🍗 닭가슴살 식단 관리 플랫폼 V3.0 ==========")
    print(" 1. 닭가슴살 입력 2. 전체 식단 조회 3. 영양 가성비 분석 4. 프로그램 종료")
    print("========================================================")

    menu_choice = input("원하는 메뉴 번호를 선택하세요 (1-4): ")
    
    if menu_choice == "1":
        input_chicken()
    elif menu_choice == "2":
        show_all_chickens()
    elif menu_choice == "3":
        run_diet_analysis()
    elif menu_choice == "4":
        print("\n 👋 프로그램을 종료합니다. 오늘도 오운완! 💪")
        break
    else:
        print(" ❌ 잘못된 입력입니다. 1부터 4 사이의 숫자가 아닙니다."
