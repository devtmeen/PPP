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

    # ลาว
    url = "https://graph.sanook.com/?operationName=recentLaoLotto&variables=%7B%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%227efb55895d9a4330ccabe0d15ac7fb9be6533a207d0a1527443422dcfd764a83%22%7D%7D"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()

        if data["data"]["recentLaoLotto"]["prizeResult"]["last4Prize"] == "":
            data["data"]["recentLaoLotto"]["prizeResult"]["last4Prize"] = "x"
        if data["data"]["recentLaoLotto"]["prizeResult"]["last3Prize1"] == "":
            data["data"]["recentLaoLotto"]["prizeResult"]["last3Prize1"] = "x"
        if data["data"]["recentLaoLotto"]["prizeResult"]["last3Prize2"] == "":
            data["data"]["recentLaoLotto"]["prizeResult"]["last3Prize2"] = "x"

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
        
        
        '''
        DB3["body"]["contents"][1]["contents"][0]["contents"][0]["contents"][1]["text"] = data["data"]["recentLaoLotto"]["prizeResult"]["last4Prize"]
        DB3["body"]["contents"][2]["contents"][0]["contents"][1]["text"] = data["data"]["recentLaoLotto"]["prizeResult"]["last3Prize1"]
        DB3["body"]["contents"][2]["contents"][4]["contents"][1]["text"] = data["data"]["recentLaoLotto"]["prizeResult"]["last3Prize2"]
        DB3["body"]["contents"][3]["contents"][0]["contents"][0]["contents"][1]["contents"][0]["text"] = data["data"]["recentLaoLotto"]["prizeResult"]["devNumberSet"][0]
        DB3["body"]["contents"][3]["contents"][0]["contents"][0]["contents"][1]["contents"][1]["text"] = data["data"]["recentLaoLotto"]["prizeResult"]["devNumberSet"][1]
        DB3["body"]["contents"][3]["contents"][0]["contents"][0]["contents"][1]["contents"][2]["text"] = data["data"]["recentLaoLotto"]["prizeResult"]["devNumberSet"][2]
        DB3["body"]["contents"][3]["contents"][0]["contents"][0]["contents"][1]["contents"][3]["text"] = data["data"]["recentLaoLotto"]["prizeResult"]["devNumberSet"][3]
        DB3["body"]["contents"][3]["contents"][0]["contents"][0]["contents"][1]["contents"][4]["text"] = data["data"]["recentLaoLotto"]["prizeResult"]["devNumberSet"][4]
        DB3["body"]["contents"][0]["text"] = data["data"]["recentLaoLotto"]["fullDate"]
        '''

        #print(DB3["hero"]["contents"][0]["contents"][0]["contents"][4]["contents"][1]["contents"][1]["url"])
        #print(DB3["hero"]["contents"][0]["contents"][0]["contents"][4]["contents"][1]["contents"][2]["url"])
        #print(DB3["hero"]["contents"][0]["contents"][0]["contents"][4]["contents"][1]["contents"][3]["url"])
        #print(DB3["hero"]["contents"][0]["contents"][0]["contents"][4]["contents"][1]["contents"][4]["url"])

        if data["data"]["recentLaoLotto"]["prizeResult"]["last4Prize"] == "" or data["data"]["recentLaoLotto"]["prizeResult"]["last4Prize"] == "x":
            DB3["hero"]["contents"][0]["contents"][0]["contents"][4]["contents"][1]["contents"][1]["url"] = "https://piggy.services/image/x.png"
            DB3["hero"]["contents"][0]["contents"][0]["contents"][4]["contents"][1]["contents"][2]["url"] = "https://piggy.services/image/x.png"
            DB3["hero"]["contents"][0]["contents"][0]["contents"][4]["contents"][1]["contents"][3]["url"] = "https://piggy.services/image/x.png"
            DB3["hero"]["contents"][0]["contents"][0]["contents"][4]["contents"][1]["contents"][4]["url"] = "https://piggy.services/image/x.png"
        else:
            DB3["hero"]["contents"][0]["contents"][0]["contents"][4]["contents"][1]["contents"][1]["url"] = "https://piggy.services/image/" + data["data"]["recentLaoLotto"]["prizeResult"]["last4Prize"][0] + ".png"
            DB3["hero"]["contents"][0]["contents"][0]["contents"][4]["contents"][1]["contents"][2]["url"] = "https://piggy.services/image/" + data["data"]["recentLaoLotto"]["prizeResult"]["last4Prize"][1] + ".png"
            DB3["hero"]["contents"][0]["contents"][0]["contents"][4]["contents"][1]["contents"][3]["url"] = "https://piggy.services/image/" + data["data"]["recentLaoLotto"]["prizeResult"]["last4Prize"][2] + ".png"
            DB3["hero"]["contents"][0]["contents"][0]["contents"][4]["contents"][1]["contents"][4]["url"] = "https://piggy.services/image/" + data["data"]["recentLaoLotto"]["prizeResult"]["last4Prize"][3] + ".png"


        
        
        '''
        DB3["hero"]["contents"][0]["contents"][0]["contents"][4]["contents"][1]["contents"][1]["url"] = "https://piggy.services/image/" + data["data"]["recentLaoLotto"]["prizeResult"]["last4Prize"][0] + ".png"
        DB3["hero"]["contents"][0]["contents"][0]["contents"][4]["contents"][1]["contents"][2]["url"] = "https://piggy.services/image/" + data["data"]["recentLaoLotto"]["prizeResult"]["last4Prize"][1] + ".png"
        DB3["hero"]["contents"][0]["contents"][0]["contents"][4]["contents"][1]["contents"][3]["url"] = "https://piggy.services/image/" + data["data"]["recentLaoLotto"]["prizeResult"]["last4Prize"][2] + ".png"
        DB3["hero"]["contents"][0]["contents"][0]["contents"][4]["contents"][1]["contents"][4]["url"] = "https://piggy.services/image/" + data["data"]["recentLaoLotto"]["prizeResult"]["last4Prize"][3] + ".png"
        '''

        #print(DB3["hero"]["contents"][1]["contents"][0]["contents"][0]["contents"][1]["contents"][1]["url"])
        #print(DB3["hero"]["contents"][1]["contents"][0]["contents"][0]["contents"][1]["contents"][2]["url"])
        #print(DB3["hero"]["contents"][1]["contents"][0]["contents"][0]["contents"][1]["contents"][3]["url"])


        if data["data"]["recentLaoLotto"]["prizeResult"]["last3Prize1"] == "" or data["data"]["recentLaoLotto"]["prizeResult"]["last3Prize1"] == "x":
            DB3["hero"]["contents"][1]["contents"][0]["contents"][0]["contents"][1]["contents"][1]["url"] = "https://piggy.services/image/x.png"
            DB3["hero"]["contents"][1]["contents"][0]["contents"][0]["contents"][1]["contents"][2]["url"] = "https://piggy.services/image/x.png"
            DB3["hero"]["contents"][1]["contents"][0]["contents"][0]["contents"][1]["contents"][3]["url"] = "https://piggy.services/image/x.png"
        else:
            DB3["hero"]["contents"][1]["contents"][0]["contents"][0]["contents"][1]["contents"][1]["url"] = "https://piggy.services/image/" + data["data"]["recentLaoLotto"]["prizeResult"]["last3Prize1"][0] + ".png"
            DB3["hero"]["contents"][1]["contents"][0]["contents"][0]["contents"][1]["contents"][2]["url"] = "https://piggy.services/image/" + data["data"]["recentLaoLotto"]["prizeResult"]["last3Prize1"][1] + ".png"
            DB3["hero"]["contents"][1]["contents"][0]["contents"][0]["contents"][1]["contents"][3]["url"] = "https://piggy.services/image/" + data["data"]["recentLaoLotto"]["prizeResult"]["last3Prize1"][2] + ".png"


        #print(DB3["hero"]["contents"][1]["contents"][1]["contents"][1]["contents"][1]["url"])
        #print(DB3["hero"]["contents"][1]["contents"][1]["contents"][1]["contents"][2]["url"])

        if data["data"]["recentLaoLotto"]["prizeResult"]["last3Prize2"] == "" or data["data"]["recentLaoLotto"]["prizeResult"]["last3Prize2"] == "x":
            DB3["hero"]["contents"][1]["contents"][1]["contents"][1]["contents"][1]["url"] = "https://piggy.services/image/x.png"
            DB3["hero"]["contents"][1]["contents"][1]["contents"][1]["contents"][2]["url"] = "https://piggy.services/image/x.png"
        else:
            DB3["hero"]["contents"][1]["contents"][1]["contents"][1]["contents"][1]["url"] = "https://piggy.services/image/" + data["data"]["recentLaoLotto"]["prizeResult"]["last3Prize2"][0] + ".png"
            DB3["hero"]["contents"][1]["contents"][1]["contents"][1]["contents"][2]["url"] = "https://piggy.services/image/" + data["data"]["recentLaoLotto"]["prizeResult"]["last3Prize2"][1] + ".png"



        #print(DB3["hero"]["contents"][2]["contents"][0]["contents"][0]["contents"][1]["contents"][1]["url"])
        #print(DB3["hero"]["contents"][2]["contents"][0]["contents"][0]["contents"][1]["contents"][2]["url"])

        #print(DB3["hero"]["contents"][2]["contents"][0]["contents"][0]["contents"][1]["contents"][4]["url"])
        #print(DB3["hero"]["contents"][2]["contents"][0]["contents"][0]["contents"][1]["contents"][5]["url"])

        #print(DB3["hero"]["contents"][2]["contents"][0]["contents"][0]["contents"][1]["contents"][7]["url"])
        #print(DB3["hero"]["contents"][2]["contents"][0]["contents"][0]["contents"][1]["contents"][8]["url"])

        #print(DB3["hero"]["contents"][2]["contents"][0]["contents"][0]["contents"][1]["contents"][10]["url"])
        #print(DB3["hero"]["contents"][2]["contents"][0]["contents"][0]["contents"][1]["contents"][11]["url"])

        #print(DB3["hero"]["contents"][2]["contents"][0]["contents"][0]["contents"][1]["contents"][13]["url"])
        #print(DB3["hero"]["contents"][2]["contents"][0]["contents"][0]["contents"][1]["contents"][14]["url"])
        
        DB3["hero"]["contents"][2]["contents"][0]["contents"][0]["contents"][1]["contents"][1]["url"] = "https://piggy.services/image/" + data["data"]["recentLaoLotto"]["prizeResult"]["devNumberSet"][0][0] + ".png"
        DB3["hero"]["contents"][2]["contents"][0]["contents"][0]["contents"][1]["contents"][2]["url"] = "https://piggy.services/image/" + data["data"]["recentLaoLotto"]["prizeResult"]["devNumberSet"][0][1] + ".png"

        DB3["hero"]["contents"][2]["contents"][0]["contents"][0]["contents"][1]["contents"][4]["url"] = "https://piggy.services/image/" + data["data"]["recentLaoLotto"]["prizeResult"]["devNumberSet"][1][0] + ".png"
        DB3["hero"]["contents"][2]["contents"][0]["contents"][0]["contents"][1]["contents"][5]["url"] = "https://piggy.services/image/" + data["data"]["recentLaoLotto"]["prizeResult"]["devNumberSet"][1][1] + ".png"

        DB3["hero"]["contents"][2]["contents"][0]["contents"][0]["contents"][1]["contents"][7]["url"] = "https://piggy.services/image/" + data["data"]["recentLaoLotto"]["prizeResult"]["devNumberSet"][2][0] + ".png"
        DB3["hero"]["contents"][2]["contents"][0]["contents"][0]["contents"][1]["contents"][8]["url"] = "https://piggy.services/image/" + data["data"]["recentLaoLotto"]["prizeResult"]["devNumberSet"][2][1] + ".png"

        DB3["hero"]["contents"][2]["contents"][0]["contents"][0]["contents"][1]["contents"][10]["url"] = "https://piggy.services/image/" + data["data"]["recentLaoLotto"]["prizeResult"]["devNumberSet"][3][0] + ".png"
        DB3["hero"]["contents"][2]["contents"][0]["contents"][0]["contents"][1]["contents"][11]["url"] = "https://piggy.services/image/" + data["data"]["recentLaoLotto"]["prizeResult"]["devNumberSet"][3][1] + ".png"

        DB3["hero"]["contents"][2]["contents"][0]["contents"][0]["contents"][1]["contents"][13]["url"] = "https://piggy.services/image/" + data["data"]["recentLaoLotto"]["prizeResult"]["devNumberSet"][4][0] + ".png"
        DB3["hero"]["contents"][2]["contents"][0]["contents"][0]["contents"][1]["contents"][14]["url"] = "https://piggy.services/image/" + data["data"]["recentLaoLotto"]["prizeResult"]["devNumberSet"][4][1] + ".png"
        

        DB3["hero"]["contents"][0]["contents"][0]["contents"][0]["contents"][0]["text"] = data["data"]["recentLaoLotto"]["fullDate"] # วันที่


    # ฮานอย
    url = "https://api.taladhuay.online/info/getResult/"+datetime.today().strftime('%Y%m%d')
    url = "https://api.xn--l3cb4bklx1c.online/info/getResult/"+datetime.today().strftime('%Y%m%d')

    print(url)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()

        for i in data["info"]:
            if i["productId"] == 23: # หวยฮานอย พิเศษ
                DB["hero"]["contents"][0]["contents"][0]["contents"][0]["contents"][0]["text"] = i["periodName"] # วันที่

                #หวยฮานอย พิเศษ
                #print(DB["hero"]["contents"][1]["contents"][0]["contents"][2]["contents"][0]["url"])
                #print(DB["hero"]["contents"][1]["contents"][0]["contents"][2]["contents"][1]["url"])
                #print(DB["hero"]["contents"][1]["contents"][0]["contents"][2]["contents"][2]["url"])

                #print(DB["hero"]["contents"][1]["contents"][0]["contents"][2]["contents"][4]["url"])
                #print(DB["hero"]["contents"][1]["contents"][0]["contents"][2]["contents"][5]["url"])
                

                DB["hero"]["contents"][1]["contents"][0]["contents"][2]["contents"][0]["url"] = "https://piggy.services/image/" + i["award1"][0] + ".png"
                DB["hero"]["contents"][1]["contents"][0]["contents"][2]["contents"][1]["url"] = "https://piggy.services/image/" + i["award1"][1] + ".png"
                DB["hero"]["contents"][1]["contents"][0]["contents"][2]["contents"][2]["url"] = "https://piggy.services/image/" + i["award1"][2] + ".png"

                DB["hero"]["contents"][1]["contents"][0]["contents"][2]["contents"][4]["url"] = "https://piggy.services/image/" + i["award2"][0] + ".png"
                DB["hero"]["contents"][1]["contents"][0]["contents"][2]["contents"][5]["url"] = "https://piggy.services/image/" + i["award2"][1] + ".png"

            
            if i["productId"] == 3: # หวยฮานอย ปกติ
                #print(DB["hero"]["contents"][1]["contents"][1]["contents"][0]["contents"][2]["contents"][0]["url"])
                #print(DB["hero"]["contents"][1]["contents"][1]["contents"][0]["contents"][2]["contents"][1]["url"])
                #print(DB["hero"]["contents"][1]["contents"][1]["contents"][0]["contents"][2]["contents"][2]["url"])

                #print(DB["hero"]["contents"][1]["contents"][1]["contents"][0]["contents"][2]["contents"][4]["url"])
                #print(DB["hero"]["contents"][1]["contents"][1]["contents"][0]["contents"][2]["contents"][5]["url"])

                DB["hero"]["contents"][1]["contents"][1]["contents"][0]["contents"][2]["contents"][0]["url"] = "https://piggy.services/image/" + i["award1"][0] + ".png"
                DB["hero"]["contents"][1]["contents"][1]["contents"][0]["contents"][2]["contents"][1]["url"] = "https://piggy.services/image/" + i["award1"][1] + ".png"
                DB["hero"]["contents"][1]["contents"][1]["contents"][0]["contents"][2]["contents"][2]["url"] = "https://piggy.services/image/" + i["award1"][2] + ".png"

                DB["hero"]["contents"][1]["contents"][1]["contents"][0]["contents"][2]["contents"][4]["url"] = "https://piggy.services/image/" + i["award2"][0] + ".png"
                DB["hero"]["contents"][1]["contents"][1]["contents"][0]["contents"][2]["contents"][5]["url"] = "https://piggy.services/image/" + i["award2"][1] + ".png"
                

            if i["productId"] == 6: # หวยฮานอย VIP
                #print(DB["hero"]["contents"][1]["contents"][2]["contents"][0]["contents"][2]["contents"][0]["url"])
                #print(DB["hero"]["contents"][1]["contents"][2]["contents"][0]["contents"][2]["contents"][1]["url"])
                #print(DB["hero"]["contents"][1]["contents"][2]["contents"][0]["contents"][2]["contents"][2]["url"])

                #print(DB["hero"]["contents"][1]["contents"][2]["contents"][0]["contents"][2]["contents"][4]["url"])
                #print(DB["hero"]["contents"][1]["contents"][2]["contents"][0]["contents"][2]["contents"][5]["url"])

                DB["hero"]["contents"][1]["contents"][2]["contents"][0]["contents"][2]["contents"][0]["url"] = "https://piggy.services/image/" + i["award1"][0] + ".png"
                DB["hero"]["contents"][1]["contents"][2]["contents"][0]["contents"][2]["contents"][1]["url"] = "https://piggy.services/image/" + i["award1"][1] + ".png"
                DB["hero"]["contents"][1]["contents"][2]["contents"][0]["contents"][2]["contents"][2]["url"] = "https://piggy.services/image/" + i["award1"][2] + ".png"

                DB["hero"]["contents"][1]["contents"][2]["contents"][0]["contents"][2]["contents"][4]["url"] = "https://piggy.services/image/" + i["award2"][0] + ".png"
                DB["hero"]["contents"][1]["contents"][2]["contents"][0]["contents"][2]["contents"][5]["url"] = "https://piggy.services/image/" + i["award2"][1] + ".png"



            if i["productId"] == 1: # หวยรัฐบาลไทย
                #DB2["hero"]["contents"][0]["contents"][0]["contents"][0]["contents"][0]["text"] = i["periodName"] # วันที่

                #print(DB2["hero"]["contents"][0]["contents"][0]["contents"][5]["contents"][0])
                #print(DB2["hero"]["contents"][0]["contents"][0]["contents"][5]["contents"][1])
                #print(DB2["hero"]["contents"][0]["contents"][0]["contents"][5]["contents"][2])
                #print(DB2["hero"]["contents"][0]["contents"][0]["contents"][5]["contents"][3])
                #print(DB2["hero"]["contents"][0]["contents"][0]["contents"][5]["contents"][4])
                #print(DB2["hero"]["contents"][0]["contents"][0]["contents"][5]["contents"][5])

                # 6 ตัว
                DB2["hero"]["contents"][0]["contents"][0]["contents"][5]["contents"][0]["url"] = "https://piggy.services/image/" + i["award1"][0] + ".png"
                DB2["hero"]["contents"][0]["contents"][0]["contents"][5]["contents"][1]["url"] = "https://piggy.services/image/" + i["award1"][1] + ".png"
                DB2["hero"]["contents"][0]["contents"][0]["contents"][5]["contents"][2]["url"] = "https://piggy.services/image/" + i["award1"][2] + ".png"
                DB2["hero"]["contents"][0]["contents"][0]["contents"][5]["contents"][3]["url"] = "https://piggy.services/image/" + i["award1"][3] + ".png"
                DB2["hero"]["contents"][0]["contents"][0]["contents"][5]["contents"][4]["url"] = "https://piggy.services/image/" + i["award1"][4] + ".png"
                DB2["hero"]["contents"][0]["contents"][0]["contents"][5]["contents"][5]["url"] = "https://piggy.services/image/" + i["award1"][5] + ".png"
                
                # 3 ตัวหน้า
                #print(DB2["hero"]["contents"][1]["contents"][0]["contents"][1]["contents"][0])
                #print(DB2["hero"]["contents"][1]["contents"][0]["contents"][1]["contents"][1])
                #print(DB2["hero"]["contents"][1]["contents"][0]["contents"][1]["contents"][2])

                #print(DB2["hero"]["contents"][1]["contents"][0]["contents"][1]["contents"][4])
                #print(DB2["hero"]["contents"][1]["contents"][0]["contents"][1]["contents"][5])
                #print(DB2["hero"]["contents"][1]["contents"][0]["contents"][1]["contents"][6])

                DB2["hero"]["contents"][1]["contents"][0]["contents"][1]["contents"][0]["url"] = "https://piggy.services/image/" + i["award3"].replace(",", "").replace(" ", "")[0] + ".png"
                DB2["hero"]["contents"][1]["contents"][0]["contents"][1]["contents"][1]["url"] = "https://piggy.services/image/" + i["award3"].replace(",", "").replace(" ", "")[1] + ".png"
                DB2["hero"]["contents"][1]["contents"][0]["contents"][1]["contents"][2]["url"] = "https://piggy.services/image/" + i["award3"].replace(",", "").replace(" ", "")[2] + ".png"

                DB2["hero"]["contents"][1]["contents"][0]["contents"][1]["contents"][4]["url"] = "https://piggy.services/image/" + i["award3"].replace(",", "").replace(" ", "")[3] + ".png"
                DB2["hero"]["contents"][1]["contents"][0]["contents"][1]["contents"][5]["url"] = "https://piggy.services/image/" + i["award3"].replace(",", "").replace(" ", "")[4] + ".png"
                DB2["hero"]["contents"][1]["contents"][0]["contents"][1]["contents"][6]["url"] = "https://piggy.services/image/" + i["award3"].replace(",", "").replace(" ", "")[5] + ".png"

                # 3 ตัวล่าง
                #print(DB2["hero"]["contents"][1]["contents"][0]["contents"][2]["contents"][1]["contents"][0])
                #print(DB2["hero"]["contents"][1]["contents"][0]["contents"][2]["contents"][1]["contents"][1])
                #print(DB2["hero"]["contents"][1]["contents"][0]["contents"][2]["contents"][1]["contents"][2])

                #print(DB2["hero"]["contents"][1]["contents"][0]["contents"][2]["contents"][1]["contents"][4])
                #print(DB2["hero"]["contents"][1]["contents"][0]["contents"][2]["contents"][1]["contents"][5])
                #print(DB2["hero"]["contents"][1]["contents"][0]["contents"][2]["contents"][1]["contents"][6])

                DB2["hero"]["contents"][1]["contents"][0]["contents"][2]["contents"][1]["contents"][0]["url"] = "https://piggy.services/image/" + i["award4"].replace(",", "").replace(" ", "")[0] + ".png"
                DB2["hero"]["contents"][1]["contents"][0]["contents"][2]["contents"][1]["contents"][1]["url"] = "https://piggy.services/image/" + i["award4"].replace(",", "").replace(" ", "")[1] + ".png"
                DB2["hero"]["contents"][1]["contents"][0]["contents"][2]["contents"][1]["contents"][2]["url"] = "https://piggy.services/image/" + i["award4"].replace(",", "").replace(" ", "")[2] + ".png"

                DB2["hero"]["contents"][1]["contents"][0]["contents"][2]["contents"][1]["contents"][4]["url"] = "https://piggy.services/image/" + i["award4"].replace(",", "").replace(" ", "")[3] + ".png"
                DB2["hero"]["contents"][1]["contents"][0]["contents"][2]["contents"][1]["contents"][5]["url"] = "https://piggy.services/image/" + i["award4"].replace(",", "").replace(" ", "")[4] + ".png"
                DB2["hero"]["contents"][1]["contents"][0]["contents"][2]["contents"][1]["contents"][6]["url"] = "https://piggy.services/image/" + i["award4"].replace(",", "").replace(" ", "")[5] + ".png"

                # 2 ตัวล่าง

                #print(DB2["hero"]["contents"][1]["contents"][1]["contents"][1]["contents"][0])
                #print(DB2["hero"]["contents"][1]["contents"][1]["contents"][1]["contents"][1])

                DB2["hero"]["contents"][1]["contents"][1]["contents"][1]["contents"][0]["url"] = "https://piggy.services/image/" + i["award2"][0] + ".png"
                DB2["hero"]["contents"][1]["contents"][1]["contents"][1]["contents"][1]["url"] = "https://piggy.services/image/" + i["award2"][1] + ".png"

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