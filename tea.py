import json;from datetime import date;import sys

def time():
    start = date(2019, 2, 5)
    today = date.today()
    days = str(today-start)
    days_final = days.split()[0]
    if days_final == "0:00:00":
        days_final = 0
    return str(days_final)

def typ():
    tea_types["Чёрный чистый"] += tea_type1
    tea_types["Зелёный чистый"] += tea_type2
    tea_types["Чёрный фруктовый"] += tea_type3
    tea_types["Зелёный фруктовый"] += tea_type4
    json.dump(tea_types, open(r'F:\documents\tea\types', mode='w'), indent=' ' * 4)
def reset():
    tea_types["Чёрный чистый"] = 0
    tea_types["Зелёный чистый"] = 0
    tea_types["Чёрный фруктовый"] = 0
    tea_types["Зелёный фруктовый"] = 0
    json.dump(tea_types, open(r'F:\documents\tea\types', mode='w'), indent=' ' * 4)
    tea_total = 0
    json.dump(tea_total, open(r'F:\documents\tea\total', mode='w'), indent=' ' * 4)
tea_total = json.load(open(r'F:\documents\tea\total'))
tea_types = json.load(open(r'F:\documents\tea\types'))

tea_coming = int(input("Введите количество выпитого чая: "))
if tea_coming == 0:
    reset()
    print("Количество обнулено.")
    sys.exit()
if tea_coming == 228:
        print("")
        print("Выпито: "+str(tea_total)+" чашек за "+str(time())+" дней.")
        print("Из них:")
        print("Чёрного чистого: "+str(tea_types.get("Чёрный чистый")))
        print("Зелёного чистого: "+str(tea_types.get("Зелёный чистый")))
        print("Чёрного фруктового: "+str(tea_types.get("Чёрный фруктовый")))
        print("Зелёного фруктового: "+str(tea_types.get("Зелёный фруктовый")))
        sys.exit()

print("Из них:")
tea_type1 = int(input("Чёрного чистого чая: "))
def fine(tea_total):
    if tea_type1+tea_type2+tea_type3+tea_type4 != tea_coming:
        print("Количество чая введено неверно.")
    else:
        tea_total = tea_total+tea_coming
        json.dump(tea_total, open(r'F:\documents\tea\total', mode='w'), indent=' ' * 4)
        typ()
        print("")
        print("Выпито: "+str(tea_total)+" чашек за "+str(time())+" дней.")
        print("Из них:")
        print("Чёрного чистого: "+str(tea_types.get("Чёрный чистый")))
        print("Зелёного чистого: "+str(tea_types.get("Зелёный чистый")))
        print("Чёрного фруктового: "+str(tea_types.get("Чёрный фруктовый")))
        print("Зелёного фруктового: "+str(tea_types.get("Зелёный фруктовый")))
if tea_coming != tea_type1:
    tea_type2 = int(input("Зелёного чистого чая: "))
    if tea_coming != tea_type1+tea_type2:
        tea_type3 = int(input("Чёрного фруктового чая: "))
        if tea_coming != tea_type1+tea_type2+tea_type3:
            tea_type4 = int(input("Зелёного фруктового чая: "))
            fine(tea_total)
        else:
            tea_type4 = 0
            fine(tea_total)
    else:
        tea_type3, tea_type4 = 0,0
        fine(tea_total)
else:
    tea_type2, tea_type3, tea_type4 = 0,0,0
    fine(tea_total)
