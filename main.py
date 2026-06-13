# 파일이름 : 4차과제 코드 작성
# 작 성 자 : 김강민

chicken_database = []

def load_from_file():
    global chicken_database

    try:
        with open("chicken_data.txt", "r", encoding="utd-8) as f:
            for line in f:
                data = line.strip().split(",")
                chicken_database.append([data[0], int(data[1]), float(data[2]), int(data[3])])
        print("📂기존에 저장된 데이터를 불러왔습니다.")
    except FileNotFoundError:
        print("📢저장된 데이터 파일이 없습니다. 새로운 식단을 시작합니다.")

def input_chicken():
    global chicken_database
    print("\--- [1] 닭가슴살 정보 입력 ---")

    try:
        name = input("제품명을 입력하세요: ")
        weight = int(input("중량(g)을 입력하세요: ")
        protein = float(input("총 단백질 함량(g)을 입력하세요: ")
        price = int(input("가격을 입력하세요(원): ")

        chicken_database.append([name, weight, protein, price])
        print(f" ✅ '{name}' 제품이 성공적으로 식단에 등록되었습니다.")
    except ValueError: 
        print(" ❌ 입력 오류: 중량, 단백질, 가격은 숫자만 입력해야합니다!")

def show_all_chickens():
    print("\n--- [2] 전체 식단 목록 조회 ---")

    if not chicken_database:
        print("📢 등록된 닭가슴살 데이터가 없습니다. 먼저 데이터를 입력해 주세요.")
        return
    
    total_price = 0
    print("-" * 50)          

    for i in range(len(chicken_database)):
        print(f"{i+1}번 제품 데이터 ➔ ", end="")
        for j in range(len(chicken_database[i])):
            print(f"[{chicken_database[i][j]}] ", end="")
        print()
        total_price += chicken_database[i][3]

    print("-" * 50)
    print(f" 💰 현재까지 등록된 닭가슴살 총 구매 비용 : {total_price}원")

def calculate_efficiency(product_info):
    efficiency = product_info[3] / product_info[2]
    return efficiency

def run_diet_analysis():
    print("\n--- [3] 영양 성분 및 가성비 종합 분석 ---")


        
             
