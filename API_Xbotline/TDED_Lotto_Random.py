from random import randint
import json

def random_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return str(randint(range_start, range_end))

def update_THAILOTTOS():
    ran_dig2 = random_digits(2)
    ran_dig3 = random_digits(3)
    FileName = "THAILOTTOS"
    with open(f"flex_message/{FileName}.json", "r", encoding="utf-8") as jsonFile:
        DB = json.load(jsonFile)

        # 2 ตัว
        DB["body"]["contents"][3]["contents"][0]["contents"][1]["contents"][1]["url"] = "https://piggy.services/image/"+ran_dig2[0]+".png"
        DB["body"]["contents"][3]["contents"][0]["contents"][1]["contents"][2]["url"] = "https://piggy.services/image/"+ran_dig2[1]+".png"
        # 3 ตัว
        DB["body"]["contents"][2]["contents"][0]["contents"][1]["contents"][1]["url"] = "https://piggy.services/image/"+ran_dig3[0]+".png"
        DB["body"]["contents"][2]["contents"][0]["contents"][1]["contents"][2]["url"] = "https://piggy.services/image/"+ran_dig3[1]+".png"
        DB["body"]["contents"][2]["contents"][0]["contents"][1]["contents"][3]["url"] = "https://piggy.services/image/"+ran_dig3[2]+".png"
    with open(f"flex_message/{FileName}.json", 'w', encoding='utf-8') as json_file:
        json.dump(DB, json_file, ensure_ascii=False, indent=4)

def update_GSBLOTTOS():
    ran_dig2 = random_digits(2)
    ran_dig3 = random_digits(3)
    FileName = "GSBLOTTOS"
    with open(f"flex_message/{FileName}.json", "r", encoding="utf-8") as jsonFile:
        DB = json.load(jsonFile)

        # 2 ตัว
        DB["body"]["contents"][3]["contents"][0]["contents"][1]["contents"][1]["url"] = "https://piggy.services/image/"+ran_dig2[0]+".png"
        DB["body"]["contents"][3]["contents"][0]["contents"][1]["contents"][2]["url"] = "https://piggy.services/image/"+ran_dig2[1]+".png"
        # 3 ตัว
        DB["body"]["contents"][2]["contents"][0]["contents"][1]["contents"][1]["url"] = "https://piggy.services/image/"+ran_dig3[0]+".png"
        DB["body"]["contents"][2]["contents"][0]["contents"][1]["contents"][2]["url"] = "https://piggy.services/image/"+ran_dig3[1]+".png"
        DB["body"]["contents"][2]["contents"][0]["contents"][1]["contents"][3]["url"] = "https://piggy.services/image/"+ran_dig3[2]+".png"
    with open(f"flex_message/{FileName}.json", 'w', encoding='utf-8') as json_file:
        json.dump(DB, json_file, ensure_ascii=False, indent=4)

def update_LAOLOTTOS():
    ran_dig4 = random_digits(4)
    FileName = "LAOLOTTOS"
    with open(f"flex_message/{FileName}.json", "r", encoding="utf-8") as jsonFile:
        DB = json.load(jsonFile)
        # 4 ตัว
        DB["body"]["contents"][2]["contents"][0]["contents"][1]["contents"][1]["url"] = "https://piggy.services/image/"+ran_dig4[0]+".png"
        DB["body"]["contents"][2]["contents"][0]["contents"][1]["contents"][2]["url"] = "https://piggy.services/image/"+ran_dig4[1]+".png"
        DB["body"]["contents"][2]["contents"][0]["contents"][1]["contents"][3]["url"] = "https://piggy.services/image/"+ran_dig4[2]+".png"
        DB["body"]["contents"][2]["contents"][0]["contents"][1]["contents"][4]["url"] = "https://piggy.services/image/"+ran_dig4[3]+".png"
    with open(f"flex_message/{FileName}.json", 'w', encoding='utf-8') as json_file:
        json.dump(DB, json_file, ensure_ascii=False, indent=4)

def update_YEEKEELOTTOS():
    ran_dig2 = random_digits(2)
    ran_dig3 = random_digits(3)
    FileName = "YEEKEELOTTOS"
    with open(f"flex_message/{FileName}.json", "r", encoding="utf-8") as jsonFile:
        DB = json.load(jsonFile)

        # 2 ตัว
        DB["body"]["contents"][3]["contents"][0]["contents"][1]["contents"][1]["url"] = "https://piggy.services/image/"+ran_dig2[0]+".png"
        DB["body"]["contents"][3]["contents"][0]["contents"][1]["contents"][2]["url"] = "https://piggy.services/image/"+ran_dig2[1]+".png"
        # 3 ตัว
        DB["body"]["contents"][2]["contents"][0]["contents"][1]["contents"][1]["url"] = "https://piggy.services/image/"+ran_dig3[0]+".png"
        DB["body"]["contents"][2]["contents"][0]["contents"][1]["contents"][2]["url"] = "https://piggy.services/image/"+ran_dig3[1]+".png"
        DB["body"]["contents"][2]["contents"][0]["contents"][1]["contents"][3]["url"] = "https://piggy.services/image/"+ran_dig3[2]+".png"
    with open(f"flex_message/{FileName}.json", 'w', encoding='utf-8') as json_file:
        json.dump(DB, json_file, ensure_ascii=False, indent=4)

def update_HANOINORMALLOTTOS():
    ran_dig2 = random_digits(2)
    ran_dig3 = random_digits(3)
    ran_dig4 = random_digits(4)
    FileName = "HANOINORMALLOTTOS"
    with open(f"flex_message/{FileName}.json", "r", encoding="utf-8") as jsonFile:
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
    with open(f"flex_message/{FileName}.json", 'w', encoding='utf-8') as json_file:
        json.dump(DB, json_file, ensure_ascii=False, indent=4)

def update_HANOILOTTOS():
    ran_dig2 = random_digits(2)
    ran_dig3 = random_digits(3)
    ran_dig4 = random_digits(4)
    FileName = "HANOILOTTOS"
    with open(f"flex_message/{FileName}.json", "r", encoding="utf-8") as jsonFile:
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
    with open(f"flex_message/{FileName}.json", 'w', encoding='utf-8') as json_file:
        json.dump(DB, json_file, ensure_ascii=False, indent=4)


def update_HANOISPECIALLOTTOS():
    ran_dig2 = random_digits(2)
    ran_dig3 = random_digits(3)
    ran_dig4 = random_digits(4)
    FileName = "HANOISPECIALLOTTOS"
    with open(f"flex_message/{FileName}.json", "r", encoding="utf-8") as jsonFile:
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
    with open(f"flex_message/{FileName}.json", 'w', encoding='utf-8') as json_file:
        json.dump(DB, json_file, ensure_ascii=False, indent=4)

def update_HANOIVIPLOTTOS():
    ran_dig2 = random_digits(2)
    ran_dig3 = random_digits(3)
    ran_dig4 = random_digits(4)
    FileName = "HANOIVIPLOTTOS"
    with open(f"flex_message/{FileName}.json", "r", encoding="utf-8") as jsonFile:
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
    with open(f"flex_message/{FileName}.json", 'w', encoding='utf-8') as json_file:
        json.dump(DB, json_file, ensure_ascii=False, indent=4)


update_THAILOTTOS()
update_GSBLOTTOS()
update_LAOLOTTOS()
update_YEEKEELOTTOS()
update_HANOILOTTOS()
update_HANOINORMALLOTTOS()
update_HANOISPECIALLOTTOS()
update_HANOIVIPLOTTOS()

