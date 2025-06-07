from random import randint
import sys
import json
import subprocess

def random_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return str(randint(range_start, range_end))

def update_THAILOTTOS(): #หวยรัฐบาลเปลี่ยนหลัง1กับ16หลัง17.00
    ran_dig2 = random_digits(2)
    ran_dig3 = random_digits(3)
    FileName = "THAILOTTOS"
    with open(f"{FileName}.json", "r", encoding="utf-8") as jsonFile:
        DB = json.load(jsonFile)

        # 2 ตัว
        DB["body"]["contents"][3]["contents"][0]["contents"][1]["contents"][1]["url"] = "https://piggy.services/image/"+ran_dig2[0]+".png"
        DB["body"]["contents"][3]["contents"][0]["contents"][1]["contents"][2]["url"] = "https://piggy.services/image/"+ran_dig2[1]+".png"
        # 3 ตัว
        DB["body"]["contents"][2]["contents"][0]["contents"][1]["contents"][1]["url"] = "https://piggy.services/image/"+ran_dig3[0]+".png"
        DB["body"]["contents"][2]["contents"][0]["contents"][1]["contents"][2]["url"] = "https://piggy.services/image/"+ran_dig3[1]+".png"
        DB["body"]["contents"][2]["contents"][0]["contents"][1]["contents"][3]["url"] = "https://piggy.services/image/"+ran_dig3[2]+".png"
    with open(f"{FileName}.json", 'w', encoding='utf-8') as json_file:
        json.dump(DB, json_file, ensure_ascii=False, indent=4)

def update_GSBLOTTOS(): #หวยออมสินเปลี่ยนทุกวันที่1เดือนเปลี่ยน12.00
    ran_dig2 = random_digits(2)
    ran_dig3 = random_digits(3)
    FileName = "GSBLOTTOS"
    with open(f"{FileName}.json", "r", encoding="utf-8") as jsonFile:
        DB = json.load(jsonFile)

        # 2 ตัว
        DB["body"]["contents"][3]["contents"][0]["contents"][1]["contents"][1]["url"] = "https://piggy.services/image/"+ran_dig2[0]+".png"
        DB["body"]["contents"][3]["contents"][0]["contents"][1]["contents"][2]["url"] = "https://piggy.services/image/"+ran_dig2[1]+".png"
        # 3 ตัว
        DB["body"]["contents"][2]["contents"][0]["contents"][1]["contents"][1]["url"] = "https://piggy.services/image/"+ran_dig3[0]+".png"
        DB["body"]["contents"][2]["contents"][0]["contents"][1]["contents"][2]["url"] = "https://piggy.services/image/"+ran_dig3[1]+".png"
        DB["body"]["contents"][2]["contents"][0]["contents"][1]["contents"][3]["url"] = "https://piggy.services/image/"+ran_dig3[2]+".png"
    with open(f"{FileName}.json", 'w', encoding='utf-8') as json_file:
        json.dump(DB, json_file, ensure_ascii=False, indent=4)

def update_LAOLOTTOS(): #หวยลาวเปลี่ยนจัน พุธ ศุกร์ หลัง21.00ทุกอาทิต
    ran_dig4 = random_digits(4)
    FileName = "LAOLOTTOS"
    with open(f"{FileName}.json", "r", encoding="utf-8") as jsonFile:
        DB = json.load(jsonFile)
        # 4 ตัว
        DB["body"]["contents"][2]["contents"][0]["contents"][1]["contents"][1]["url"] = "https://piggy.services/image/"+ran_dig4[0]+".png"
        DB["body"]["contents"][2]["contents"][0]["contents"][1]["contents"][2]["url"] = "https://piggy.services/image/"+ran_dig4[1]+".png"
        DB["body"]["contents"][2]["contents"][0]["contents"][1]["contents"][3]["url"] = "https://piggy.services/image/"+ran_dig4[2]+".png"
        DB["body"]["contents"][2]["contents"][0]["contents"][1]["contents"][4]["url"] = "https://piggy.services/image/"+ran_dig4[3]+".png"
    with open(f"{FileName}.json", 'w', encoding='utf-8') as json_file:
        json.dump(DB, json_file, ensure_ascii=False, indent=4)

def update_YEEKEELOTTOS(): #หวยยี่กี่เปลี่ยทุกๆ15นาทีตั้งแต่6เช้าถึงตี4ทุกๆวัน(6.00-6.16-6.31-6.46-7.00)
    ran_dig2 = random_digits(2)
    ran_dig3 = random_digits(3)
    FileName = "YEEKEELOTTOS"
    with open(f"{FileName}.json", "r", encoding="utf-8") as jsonFile:
        DB = json.load(jsonFile)

        # 2 ตัว
        DB["body"]["contents"][3]["contents"][0]["contents"][1]["contents"][1]["url"] = "https://piggy.services/image/"+ran_dig2[0]+".png"
        DB["body"]["contents"][3]["contents"][0]["contents"][1]["contents"][2]["url"] = "https://piggy.services/image/"+ran_dig2[1]+".png"
        # 3 ตัว
        DB["body"]["contents"][2]["contents"][0]["contents"][1]["contents"][1]["url"] = "https://piggy.services/image/"+ran_dig3[0]+".png"
        DB["body"]["contents"][2]["contents"][0]["contents"][1]["contents"][2]["url"] = "https://piggy.services/image/"+ran_dig3[1]+".png"
        DB["body"]["contents"][2]["contents"][0]["contents"][1]["contents"][3]["url"] = "https://piggy.services/image/"+ran_dig3[2]+".png"
    with open(f"{FileName}.json", 'w', encoding='utf-8') as json_file:
        json.dump(DB, json_file, ensure_ascii=False, indent=4)

def update_HANOINORMALLOTTOS(): #หวยฮานอยปกติเปลี่ยนทุกวันหลัง19.00
    ran_dig2 = random_digits(2)
    ran_dig3 = random_digits(3)
    ran_dig4 = random_digits(4)
    FileName = "HANOINORMALLOTTOS"
    with open(f"{FileName}.json", "r", encoding="utf-8") as jsonFile:
        DB = json.load(jsonFile)

        # 2 ตัว
        DB["body"]["contents"][4]["contents"][0]["contents"][1]["contents"][1]["url"] = "https://piggy.services/image/" + ran_dig2[0] + ".png"
        DB["body"]["contents"][4]["contents"][0]["contents"][1]["contents"][2]["url"] = "https://piggy.services/image/" + ran_dig2[1] + ".png"
        
        # 3 ตัว
        DB["body"]["contents"][3]["contents"][0]["contents"][1]["contents"][1]["url"] = "https://piggy.services/image/"+ran_dig3[0]+".png"
        DB["body"]["contents"][3]["contents"][0]["contents"][1]["contents"][2]["url"] = "https://piggy.services/image/"+ran_dig3[1]+".png"
        DB["body"]["contents"][3]["contents"][0]["contents"][1]["contents"][3]["url"] = "https://piggy.services/image/"+ran_dig3[2]+".png"
        # 4 ตัว
        DB["body"]["contents"][2]["contents"][0]["contents"][1]["contents"][1]["url"] = "https://piggy.services/image/"+ran_dig4[0]+".png"
        DB["body"]["contents"][2]["contents"][0]["contents"][1]["contents"][2]["url"] = "https://piggy.services/image/"+ran_dig4[1]+".png"
        DB["body"]["contents"][2]["contents"][0]["contents"][1]["contents"][3]["url"] = "https://piggy.services/image/"+ran_dig4[2]+".png"
        DB["body"]["contents"][2]["contents"][0]["contents"][1]["contents"][4]["url"] = "https://piggy.services/image/"+ran_dig4[3]+".png"
    with open(f"{FileName}.json", 'w', encoding='utf-8') as json_file:
        json.dump(DB, json_file, ensure_ascii=False, indent=4)

def update_HANOILOTTOS(): #หวยฮานอยเฉพาะกิจเปลี่ยนทุกวัน หลัง17.00
    ran_dig2 = random_digits(2)
    ran_dig3 = random_digits(3)
    ran_dig4 = random_digits(4)
    FileName = "HANOILOTTOS"
    with open(f"{FileName}.json", "r", encoding="utf-8") as jsonFile:
        DB = json.load(jsonFile)

        # 2 ตัว
        DB["body"]["contents"][4]["contents"][0]["contents"][1]["contents"][1]["url"] = "https://piggy.services/image/" + ran_dig2[0] + ".png"
        DB["body"]["contents"][4]["contents"][0]["contents"][1]["contents"][2]["url"] = "https://piggy.services/image/" + ran_dig2[1] + ".png"
        
        # 3 ตัว
        DB["body"]["contents"][3]["contents"][0]["contents"][1]["contents"][1]["url"] = "https://piggy.services/image/"+ran_dig3[0]+".png"
        DB["body"]["contents"][3]["contents"][0]["contents"][1]["contents"][2]["url"] = "https://piggy.services/image/"+ran_dig3[1]+".png"
        DB["body"]["contents"][3]["contents"][0]["contents"][1]["contents"][3]["url"] = "https://piggy.services/image/" + ran_dig3[2] + ".png"
        
        # 4 ตัว
        DB["body"]["contents"][2]["contents"][0]["contents"][1]["contents"][1]["url"] = "https://piggy.services/image/"+ran_dig4[0]+".png"
        DB["body"]["contents"][2]["contents"][0]["contents"][1]["contents"][2]["url"] = "https://piggy.services/image/"+ran_dig4[1]+".png"
        DB["body"]["contents"][2]["contents"][0]["contents"][1]["contents"][3]["url"] = "https://piggy.services/image/"+ran_dig4[2]+".png"
        DB["body"]["contents"][2]["contents"][0]["contents"][1]["contents"][4]["url"] = "https://piggy.services/image/"+ran_dig4[3]+".png"
    with open(f"{FileName}.json", 'w', encoding='utf-8') as json_file:
        json.dump(DB, json_file, ensure_ascii=False, indent=4)

def update_HANOISPECIALLOTTOS(): #หวยฮานอยพิเศษเปลี่ยนทุกวันหลัง18.00
    ran_dig2 = random_digits(2)
    ran_dig3 = random_digits(3)
    ran_dig4 = random_digits(4)
    FileName = "HANOISPECIALLOTTOS"
    with open(f"{FileName}.json", "r", encoding="utf-8") as jsonFile:
        DB = json.load(jsonFile)
        # 2 ตัว
        DB["body"]["contents"][4]["contents"][0]["contents"][1]["contents"][1]["url"] = "https://piggy.services/image/" + ran_dig2[0] + ".png"
        DB["body"]["contents"][4]["contents"][0]["contents"][1]["contents"][2]["url"] = "https://piggy.services/image/" + ran_dig2[1] + ".png"
        
        # 3 ตัว
        DB["body"]["contents"][3]["contents"][0]["contents"][1]["contents"][1]["url"] = "https://piggy.services/image/"+ran_dig3[0]+".png"
        DB["body"]["contents"][3]["contents"][0]["contents"][1]["contents"][2]["url"] = "https://piggy.services/image/"+ran_dig3[1]+".png"
        DB["body"]["contents"][3]["contents"][0]["contents"][1]["contents"][3]["url"] = "https://piggy.services/image/" + ran_dig3[2] + ".png"
        
        # 4 ตัว
        DB["body"]["contents"][2]["contents"][0]["contents"][1]["contents"][1]["url"] = "https://piggy.services/image/"+ran_dig4[0]+".png"
        DB["body"]["contents"][2]["contents"][0]["contents"][1]["contents"][2]["url"] = "https://piggy.services/image/"+ran_dig4[1]+".png"
        DB["body"]["contents"][2]["contents"][0]["contents"][1]["contents"][3]["url"] = "https://piggy.services/image/"+ran_dig4[2]+".png"
        DB["body"]["contents"][2]["contents"][0]["contents"][1]["contents"][4]["url"] = "https://piggy.services/image/"+ran_dig4[3]+".png"
    with open(f"{FileName}.json", 'w', encoding='utf-8') as json_file:
        json.dump(DB, json_file, ensure_ascii=False, indent=4)

def update_HANOIVIPLOTTOS(): #หวยฮานอยvipเปลี่ยนทุกวันหลัง20.00
    ran_dig2 = random_digits(2)
    ran_dig3 = random_digits(3)
    ran_dig4 = random_digits(4)
    FileName = "HANOIVIPLOTTOS"
    with open(f"{FileName}.json", "r", encoding="utf-8") as jsonFile:
        DB = json.load(jsonFile)
        # 2 ตัว
        DB["body"]["contents"][4]["contents"][0]["contents"][1]["contents"][1]["url"] = "https://piggy.services/image/" + ran_dig2[0] + ".png"
        DB["body"]["contents"][4]["contents"][0]["contents"][1]["contents"][2]["url"] = "https://piggy.services/image/" + ran_dig2[1] + ".png"
        
        # 3 ตัว
        DB["body"]["contents"][3]["contents"][0]["contents"][1]["contents"][1]["url"] = "https://piggy.services/image/"+ran_dig3[0]+".png"
        DB["body"]["contents"][3]["contents"][0]["contents"][1]["contents"][2]["url"] = "https://piggy.services/image/"+ran_dig3[1]+".png"
        DB["body"]["contents"][3]["contents"][0]["contents"][1]["contents"][3]["url"] = "https://piggy.services/image/" + ran_dig3[2] + ".png"
        
        # 4 ตัว
        DB["body"]["contents"][2]["contents"][0]["contents"][1]["contents"][1]["url"] = "https://piggy.services/image/"+ran_dig4[0]+".png"
        DB["body"]["contents"][2]["contents"][0]["contents"][1]["contents"][2]["url"] = "https://piggy.services/image/"+ran_dig4[1]+".png"
        DB["body"]["contents"][2]["contents"][0]["contents"][1]["contents"][3]["url"] = "https://piggy.services/image/"+ran_dig4[2]+".png"
        DB["body"]["contents"][2]["contents"][0]["contents"][1]["contents"][4]["url"] = "https://piggy.services/image/"+ran_dig4[3]+".png"
    with open(f"{FileName}.json", 'w', encoding='utf-8') as json_file:
        json.dump(DB, json_file, ensure_ascii=False, indent=4)

match sys.argv[1]:
    case "THAILOTTOS":
         update_THAILOTTOS()
    case "GSBLOTTOS":
        update_GSBLOTTOS()
    case "LAOLOTTOS":
        update_LAOLOTTOS()
    case "YEEKEELOTTOS":
        update_YEEKEELOTTOS()        
    case "HANOINORMALLOTTOS": #หวยฮานอยปกติ
        update_HANOINORMALLOTTOS()
    case "HANOILOTTOS": #หวยฮานอย
        update_HANOILOTTOS()
    case "HANOISPECIALLOTTOS": #หวยฮานอยพิเศษ
        update_HANOISPECIALLOTTOS()
    case "HANOIVIPLOTTOS": #หวยฮานอยvip
        update_HANOIVIPLOTTOS()
        
p = subprocess.Popen(["powershell.exe", "C:\\Users\\Administrator\\Desktop\\Lotto_API\\copy.ps1"], stdout=sys.stdout)
p.communicate()



'''
หวยรัฐบาลเปลี่ยนหลัง1กับ16หลัง17.00
หวยออมสินเปลี่ยนทุกวันที่1เดือนเปลี่ยน12.00
หวยลาวเปลี่ยนจัน พุธ ศุกร์ หลัง21.00ทุกอาทิต
หวยยี่กี่เปลี่ยทุกๆ15นาทีตั้งแต่6เช้าถึงตี4ทุกๆวัน(6.00-6.16-6.31-6.46-7.00)

หวยฮานอยปกติเปลี่ยนทุกวันหลัง19.00
หวยฮานอยพิเศษเปลี่ยนทุกวันหลัง18.00
หวยฮานอยvipเปลี่ยนทุกวันหลัง20.00
หวยฮานอยเฉพาะกิจเปลี่ยนทุกวัน หลัง17.00

update_THAILOTTOS()
update_GSBLOTTOS()
update_LAOLOTTOS()
update_YEEKEELOTTOS()
update_HANOILOTTOS()
update_HANOINORMALLOTTOS()
update_HANOISPECIALLOTTOS()
update_HANOIVIPLOTTOS()
'''
