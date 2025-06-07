import requests
from bs4 import BeautifulSoup
from time import sleep
import sys
import re
import json

url = "https://ball7m.com/match_preview"
token = 'xAdNNgc8PMcgUHlm9PpUWINY7Po7Xot8IJUNb6h1Rig'


def check_update():
    with open("FOOTBALL.json", "r", encoding="utf-8") as jsonFile:
        data = json.load(jsonFile)

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    first_match = soup.find_all("div", {"class": "col-12"})[0]
    img = first_match.findAll('img')[0]['src']
    predict_url = first_match.findAll('a')[0]['href']
    if predict_url != data["last_update"]:
        data["last_update"] = predict_url
        lineNotify("มีอัพเดทใหม่", img)
        with open('FOOTBALL.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=2)


def lineNotify(message, img=None):
    url = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': 'Bearer ' + token}
    payload = {'message': message, 'imageThumbnail': img, 'imageFullsize': img}
    r = requests.post(url, headers=headers, data=payload)


while True:
    check_update()
    sleep(300)
