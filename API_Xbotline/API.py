import requests
from bs4 import BeautifulSoup
from time import sleep
import sys
import re
import json

with open("flex_message/FOOTBALL.json", "r", encoding="utf-8") as jsonFile:
    data = json.load(jsonFile)

'''
print(data["contents"][0]["hero"]["url"])
print(data["contents"][0]["body"]["contents"][0]["contents"][0]["contents"][0]["text"])
print(data["contents"][0]["body"]["contents"][0]["contents"][0]["contents"][1]["text"])
print(data["contents"][0]["body"]["contents"][2]["contents"][0]["text"])
'''

url = "https://ball7m.com/match_preview"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
count = 0
for match_all in soup.find_all("div", {"class": "col-6"}):
    if count > 4:
        break
    images = match_all.findAll('img')[0]['src']  # รูปทีม
    data["contents"][count]["hero"]["url"] = images
    predict_url = "https://ball7m.com/"+match_all.findAll('a')[0]['href']
    sleep(1)

    soup2 = BeautifulSoup(requests.get(predict_url).content, "html.parser")
    match_detail = soup2.find_all("div", {"class": "col-4"})
    TeamA = match_detail[0].text.strip()  # Team A
    TeamB = match_detail[1].text.strip()  # Team B
    data["contents"][count]["body"]["contents"][0]["contents"][0]["contents"][0]["text"] = TeamA
    data["contents"][count]["body"]["contents"][0]["contents"][0]["contents"][0]["text"] = TeamB

    print(str(TeamA) + " vs " + str(TeamB))
    All_predict = soup2.findAll("div", {"class": "card-body"})
    for predict in All_predict:
        if "แนวโน้มเกม" in predict.text:
            # วิเคราะห์
            data["contents"][0]["body"]["contents"][2]["contents"][0]["text"] = predict.text.strip().strip().strip()
    count += 1
# print(json.dumps(data, indent=4))

with open('flex_message/FOOTBALL.json', 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=2)
