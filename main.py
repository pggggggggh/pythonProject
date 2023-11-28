# 코드 작성
class Phone:
    def __init__(self, brand, battery):
        self.brand = brand
        self.battery = battery

# 채점시 아래와 비슷한 형식의 코드가 실행됩니다
phone1 = Phone("우주폰", 100)
phone2 = Phone("사과폰", 50)

print(phone1.brand, phone1.battery)
print(phone2.brand, phone2.battery)