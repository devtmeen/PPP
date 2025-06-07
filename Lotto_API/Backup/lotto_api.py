import requests
from bs4 import BeautifulSoup
from time import sleep
import sys
import json
from datetime import datetime
import subprocess

_TH_ABBR_MONTHS = [
    "มกราคม",
    "กุมภาพันธ์",
    "มีนาคม",
    "เมษายน",
    "พฤษภาคม",
    "มิถุนายน",
    "กรกฎาคม",
    "สิงหาคม",
    "กันยายน",
    "ตุลาคม",
    "พฤศจิกายน",
    "ธันวาคม",
]

def check_update():
    DAY = datetime.today().strftime('%d')
    MONTH = _TH_ABBR_MONTHS[int(datetime.today().strftime('%m'))-1]
    YEAR = datetime.today().strftime('%Y')

    
    with open("หวยฮานอย.json", "r", encoding="utf-8") as jsonFile:
        DB = json.load(jsonFile)
    with open("หวยรัฐบาล.json", "r", encoding="utf-8") as jsonFile:
        DB2 = json.load(jsonFile)
    with open("หวยลาว.json", "r", encoding="utf-8") as jsonFile:
        DB3 = json.load(jsonFile)

    '''
    print(DB["body"]["contents"][0]["text"]) #วันที่

    print(DB["body"]["contents"][1]["contents"][0]["contents"][0]["contents"][4]["contents"][0]["contents"][1]["text"]) #ฮานอยพิเศษ 3 ตัวบน
    print(DB["body"]["contents"][1]["contents"][0]["contents"][0]["contents"][4]["contents"][3]["contents"][1]["text"]) #ฮานอยพิเศษ 2 ตัวล่าง

    print(DB["body"]["contents"][2]["contents"][4]["contents"][0]["contents"][1]["text"]) #ฮานอยปกติ 3 ตัวบน
    print(DB["body"]["contents"][2]["contents"][4]["contents"][3]["contents"][1]["text"]) #ฮานอยปกติ 2 ตัวล่าง
        
    print(DB["body"]["contents"][4]["contents"][0]["contents"][0]["contents"][3]["contents"][0]["text"]) #ฮานอย VIP 3 ตัวบน
    print(DB["body"]["contents"][4]["contents"][0]["contents"][0]["contents"][3]["contents"][3]["text"]) #ฮานอย VIP 2 ตัวล่าง    
    print(DB["body"]["contents"][1]["contents"][0]["contents"][0]["contents"][0]["contents"][0]["text"]) #ฮานอยพิเศษ
    print(DB["body"]["contents"][2]["contents"][0]["contents"][0]["text"]) #ฮานอยปกติ
    print(DB["body"]["contents"][4]["contents"][0]["contents"][0]["contents"][0]["contents"][0]["text"]) #ฮานอยวีไอพี

    print(DB3["body"]["contents"][1]["contents"][0]["contents"][0]["contents"][1]["text"])
    print(DB3["body"]["contents"][2]["contents"][0]["contents"][1]["text"])
    print(DB3["body"]["contents"][2]["contents"][4]["contents"][1]["text"])
    print(DB3["body"]["contents"][3]["contents"][0]["contents"][0]["contents"][1]["contents"][0]["text"])
    print(DB3["body"]["contents"][3]["contents"][0]["contents"][0]["contents"][1]["contents"][1]["text"])
    print(DB3["body"]["contents"][3]["contents"][0]["contents"][0]["contents"][1]["contents"][2]["text"])
    print(DB3["body"]["contents"][3]["contents"][0]["contents"][0]["contents"][1]["contents"][3]["text"])
    

    print(DB3["body"]["contents"][1]["contents"][0]["contents"][0]["contents"][1]["text"])
    print(DB3["body"]["contents"][2]["contents"][0]["contents"][1]["text"])
    print(DB3["body"]["contents"][2]["contents"][4]["contents"][1]["text"])
    print(DB3["body"]["contents"][3]["contents"][0]["contents"][0]["contents"][1]["contents"][0]["text"])
    print(DB3["body"]["contents"][3]["contents"][0]["contents"][0]["contents"][1]["contents"][1]["text"])
    print(DB3["body"]["contents"][3]["contents"][0]["contents"][0]["contents"][1]["contents"][2]["text"])
    print(DB3["body"]["contents"][3]["contents"][0]["contents"][0]["contents"][1]["contents"][3]["text"])
    '''
    # ลาว
    url = "https://graph.sanook.com/?operationName=recentLaoLotto&variables=%7B%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%227efb55895d9a4330ccabe0d15ac7fb9be6533a207d0a1527443422dcfd764a83%22%7D%7D"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()

        if data["data"]["recentLaoLotto"]["prizeResult"]["last4Prize"] == "":
            data["data"]["recentLaoLotto"]["prizeResult"]["last4Prize"] = "xxxx"
        if data["data"]["recentLaoLotto"]["prizeResult"]["last3Prize1"] == "":
            data["data"]["recentLaoLotto"]["prizeResult"]["last3Prize1"] = "xxx"
        if data["data"]["recentLaoLotto"]["prizeResult"]["last3Prize2"] == "":
            data["data"]["recentLaoLotto"]["prizeResult"]["last3Prize2"] = "xx"

        if data["data"]["recentLaoLotto"]["prizeResult"]["devNumberSet"][0] == "" or data["data"]["recentLaoLotto"]["prizeResult"]["devNumberSet"][0] == "xx":
            data["data"]["recentLaoLotto"]["prizeResult"]["devNumberSet"][0] = "xx"
        if data["data"]["recentLaoLotto"]["prizeResult"]["devNumberSet"][1] == "" or data["data"]["recentLaoLotto"]["prizeResult"]["devNumberSet"][1] == "xx":
            data["data"]["recentLaoLotto"]["prizeResult"]["devNumberSet"][1] = "xx"
        if data["data"]["recentLaoLotto"]["prizeResult"]["devNumberSet"][2] == "" or data["data"]["recentLaoLotto"]["prizeResult"]["devNumberSet"][2] == "xx":
            data["data"]["recentLaoLotto"]["prizeResult"]["devNumberSet"][2] = "xx"
        if data["data"]["recentLaoLotto"]["prizeResult"]["devNumberSet"][3] == "" or data["data"]["recentLaoLotto"]["prizeResult"]["devNumberSet"][3] == "xx":
            data["data"]["recentLaoLotto"]["prizeResult"]["devNumberSet"][3] = "xx"
        if data["data"]["recentLaoLotto"]["prizeResult"]["devNumberSet"][4] == "" or data["data"]["recentLaoLotto"]["prizeResult"]["devNumberSet"][4] == "xx":
            data["data"]["recentLaoLotto"]["prizeResult"]["devNumberSet"][4] = "xx"
        

        DB3["body"]["contents"][1]["contents"][0]["contents"][0]["contents"][1]["text"] = data["data"]["recentLaoLotto"]["prizeResult"]["last4Prize"]
        DB3["body"]["contents"][2]["contents"][0]["contents"][1]["text"] = data["data"]["recentLaoLotto"]["prizeResult"]["last3Prize1"]
        DB3["body"]["contents"][2]["contents"][4]["contents"][1]["text"] = data["data"]["recentLaoLotto"]["prizeResult"]["last3Prize2"]
        DB3["body"]["contents"][3]["contents"][0]["contents"][0]["contents"][1]["contents"][0]["text"] = data["data"]["recentLaoLotto"]["prizeResult"]["devNumberSet"][0]
        DB3["body"]["contents"][3]["contents"][0]["contents"][0]["contents"][1]["contents"][1]["text"] = data["data"]["recentLaoLotto"]["prizeResult"]["devNumberSet"][1]
        DB3["body"]["contents"][3]["contents"][0]["contents"][0]["contents"][1]["contents"][2]["text"] = data["data"]["recentLaoLotto"]["prizeResult"]["devNumberSet"][2]
        DB3["body"]["contents"][3]["contents"][0]["contents"][0]["contents"][1]["contents"][3]["text"] = data["data"]["recentLaoLotto"]["prizeResult"]["devNumberSet"][3]
        DB3["body"]["contents"][3]["contents"][0]["contents"][0]["contents"][1]["contents"][4]["text"] = data["data"]["recentLaoLotto"]["prizeResult"]["devNumberSet"][4]
        DB3["body"]["contents"][0]["text"] = data["data"]["recentLaoLotto"]["fullDate"]

    url = "https://api.taladhuay.online/info/getResult/"+datetime.today().strftime('%Y%m%d')
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        DB["body"]["contents"][0]["text"] = '{} {} {}'.format(DAY, MONTH, YEAR)
        DB["body"]["contents"][1]["contents"][0]["contents"][0]["contents"][0]["contents"][0]["text"] = "ฮานอยพิเศษ"
        DB["body"]["contents"][2]["contents"][0]["contents"][0]["text"] = "ฮานอยปกติ"
        DB["body"]["contents"][4]["contents"][0]["contents"][0]["contents"][0]["contents"][0]["text"] = "ฮานอยวีไอพี"

        for i in data["info"]:
            if i["productId"] == 23: # หวยฮานอย พิเศษ
                '''
                if i["award1"] != "xxx" and i["award1"] != DB["body"]["contents"][1]["contents"][0]["contents"][0]["contents"][4]["contents"][0]["contents"][1]["text"]:
                    lineNotify("ฮานอยพิเศษ 3 ตัวบน : " + i["award1"])
                if i["award2"] != "xx" and i["award2"] != DB["body"]["contents"][1]["contents"][0]["contents"][0]["contents"][4]["contents"][3]["contents"][1]["text"]:
                    lineNotify("ฮานอยพิเศษ 2 ตัวล่าง : " + i["award2"])
                '''
                DB["body"]["contents"][1]["contents"][0]["contents"][0]["contents"][4]["contents"][0]["contents"][1]["text"] = i["award1"]
                DB["body"]["contents"][1]["contents"][0]["contents"][0]["contents"][4]["contents"][3]["contents"][1]["text"] = i["award2"]
            
            if i["productId"] == 3: # หวยฮานอย ปกติ
                DB["body"]["contents"][2]["contents"][4]["contents"][0]["contents"][1]["text"] = i["award1"]
                DB["body"]["contents"][2]["contents"][4]["contents"][3]["contents"][1]["text"] = i["award2"]

            if i["productId"] == 6: # หวยฮานอย VIP
                DB["body"]["contents"][4]["contents"][0]["contents"][0]["contents"][3]["contents"][0]["text"] = i["award1"]
                DB["body"]["contents"][4]["contents"][0]["contents"][0]["contents"][3]["contents"][3]["text"] = i["award2"]


            if i["productId"] == 1: # หวยรัฐบาลไทย
                d = i["periodName"].split(" ")[1].split("/")[0]
                m = i["periodName"].split(" ")[1].split("/")[1]
                y = i["periodName"].split(" ")[1].split("/")[2]

                DB2["body"]["contents"][0]["text"] = d + " " + _TH_ABBR_MONTHS[int(m)-1] +" 25"+ y # วันที่
                DB2["body"]["contents"][1]["contents"][0]["contents"][0]["contents"][1]["text"] = i["award1"] # รางวัลที่ 1
                DB2["body"]["contents"][2]["contents"][0]["contents"][1]["text"] = i["award3"].replace(",", "") # เลขหน้า 3 ตัว
                DB2["body"]["contents"][2]["contents"][4]["contents"][1]["text"] = i["award2"] # เลขท้าย 2 ตัว
                DB2["body"]["contents"][4]["contents"][0]["contents"][0]["contents"][3]["contents"][0]["text"] = i["award4"].split(", ")[0] # เลขท้าย 3 ตัว
                DB2["body"]["contents"][4]["contents"][0]["contents"][0]["contents"][3]["contents"][3]["text"] = i["award4"].split(", ")[1] # เลขท้าย 3 ตัว                

        with open('หวยฮานอย.json', 'w', encoding='utf-8') as json_file:
            json.dump(DB, json_file, ensure_ascii=False, indent=4)
        with open('หวยรัฐบาล.json', 'w', encoding='utf-8') as json_file:
            json.dump(DB2, json_file, ensure_ascii=False, indent=4)
        with open('หวยลาว.json', 'w', encoding='utf-8') as json_file:
            json.dump(DB3, json_file, ensure_ascii=False, indent=4)

def lineNotify(message):
    url = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': 'Bearer ' + line_token}
    payload = {'message': message}
    r = requests.post(url, headers=headers, data=payload)

while True:
    check_update()
    p = subprocess.Popen(["powershell.exe", "C:\\Users\\Administrator\\Desktop\\Lotto_API\\copy.ps1"], stdout=sys.stdout)
    p.communicate()
    sleep(300) # 10 Minute