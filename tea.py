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
    tea_types["Pure black"] += tea_type1
    tea_types["Pure green"] += tea_type2
    tea_types["Black fruit"] += tea_type3
    tea_types["Green fruit"] += tea_type4
    json.dump(tea_types, open('types', mode='w'), indent=' ' * 4)
def reset():
    tea_types["Pure black"] = 0
    tea_types["Pure green"] = 0
    tea_types["Black fruit"] = 0
    tea_types["Green fruit"] = 0
    json.dump(tea_types, open('types', mode='w'), indent=' ' * 4)
    tea_total = 0
    json.dump(tea_total, open('total', mode='w'), indent=' ' * 4)
tea_total = json.load(open('total'))
tea_types = json.load(open('types'))

tea_coming = int(input("Enter the total amount of tea drunk: "))
if tea_coming == 0:
    reset()
    print("The number is reset.")
    sys.exit()
if tea_coming == 1000:
        print("")
        print(str(tea_total)+" cups drunk in "+str(time())+ " days.")
        print("Among them:")
        print("Pure black: "+str(tea_types.get("Pure black")))
        print("Pure green: "+str(tea_types.get("Pure green")))
        print("Black fruit: "+str(tea_types.get("Black fruit")))
        print("Green fruit: "+str(tea_types.get("Green fruit")))
        sys.exit()

print("Among them:")
tea_type1 = int(input("Pure black: "))
def fine(tea_total):
    if tea_type1+tea_type2+tea_type3+tea_type4 != tea_coming:
        print("The amount of tea entered is incorrect.")
    else:
        tea_total = tea_total+tea_coming
        json.dump(tea_total, open('total', mode='w'), indent=' ' * 4)
        typ()
        print("")
        print(str(tea_total)+" cups drunk in "+str(time())+ " days.")
        print("Among them:")
        print("Pure black: "+str(tea_types.get("Pure black")))
        print("Pure green: "+str(tea_types.get("Pure green")))
        print("Black fruit: "+str(tea_types.get("Black fruit")))
        print("Green fruit: "+str(tea_types.get("Green fruit")))
if tea_coming != tea_type1:
    tea_type2 = int(input("Pure green: "))
    if tea_coming != tea_type1+tea_type2:
        tea_type3 = int(input("Black fruit: "))
        if tea_coming != tea_type1+tea_type2+tea_type3:
            tea_type4 = int(input("Green fruit: "))
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
