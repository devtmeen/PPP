import configparser

# อ่านค่าจากไฟล์ config.ini
config = configparser.ConfigParser()
config.read('config.ini')

# ดึงค่า Name_Web และ Game_List1 จาก config
Name_Web = config['Config']['Name_Web']
Game_List1 = int(config['Config']['Game_List1'])
Logo_Web = config['Config']['Logo_Web']
Link_Web = config['Config']['Link_Web']
#Token_LineNotify = config['Config']['Token_LineNotify']
#Logo_pg = config['Config']['Logo_pg']
#Logo_ios = config['Config']['Logo_ios']



import schedule
import json, random, time
from datetime import datetime

import requests

def send_line_notify(message, token):
    url = "https://notify-api.line.me/api/notify"
    headers = {"Authorization": "Bearer " + token}

    payload = {"message": message}
    r = requests.post(url, headers=headers, params=payload)
    
    # Check for any errors
    if r.status_code != 200:
        print(f"Error sending Line Notify: {r.status_code}, {r.text}")
# ใส่ Token ที่ได้จากการสร้างใน Line Notify
#line_notify_token = Token_LineNotify

def job():
    # ดึงเวลาปัจจุบัน
    now = datetime.now()

    # แปลงเวลาเป็นรูปแบบ "00:00"
    formatted_time = now.strftime("%H")
    # แปลงเวลาเป็น integer ก่อนที่จะบวก
    num = int(formatted_time) + 1

    # อ่านข้อมูลจากไฟล์ PP_Game.json
    with open('PP_Game.json', 'r', encoding='utf-8') as json_file:
        PP_Game = json.load(json_file)

    # สร้างเซ็ตเพื่อเก็บเปอร์เซ็นต์ที่สร้างขึ้นแล้ว
    used_percentages = set()
    used_data = set()
    used_percen_splins = set()
    used_percen_game = set()
    used_percen_gamee = set()

    # สร้างข้อความ message_percen และตรวจสอบเปอร์เซ็นต์ในเซ็ต
    def generate_unique_percentage():
        while True:
            percentage = random.uniform(30, 95)
            message_percen = f"{percentage:.2f}%"

            # ตรวจสอบเปอร์เซ็นต์ในทั้งหมดของ "BONUSTIME" และ bubbles
            if message_percen not in used_percentages:
                used_percentages.add(message_percen)
                return message_percen
            
    def generate_unique_percen_splin():
        while True:
            percen_splin = random.uniform(18, 35)
            message_percen_splin = f"{percen_splin:.0f}%"

            # ตรวจสอบเปอร์เซ็นต์ในทั้งหมดของ "BONUSTIME" และ bubbles
            if message_percen_splin not in used_percen_splins:
                used_percen_splins.add(message_percen_splin)
                return message_percen_splin
    
    # สร้างข้อความ message_percen และตรวจสอบเปอร์เซ็นต์ในเซ็ต
    def generate_unique_percentage_game():
        while True:
            percentage_game = random.randint(1, 20)
            message_percen_game = f"x{percentage_game}000"

            # ตรวจสอบเปอร์เซ็นต์ในเซ็ต
            if message_percen_game not in used_percen_game:
                used_percen_game.add(message_percen_game)
                return message_percen_game
              
    # สร้างข้อความ message_percen และตรวจสอบเปอร์เซ็นต์ในเซ็ต
    def generate_unique_percentage_gamee():  
        while True:
             percentage_gamee = random.randint(19, 28)   
             message_percen_gamee = f"-{percentage_gamee}px"
             
             # ตรวจสอบเปอร์เซ็นต์ในเซ็ต
             if message_percen_gamee not in used_percen_gamee:
                used_percen_gamee.add(message_percen_gamee)
                return message_percen_gamee
             
    Bonustime_Update = formatted_time + ":00 - " + str(num) + ":00 น."
    # สร้าง JSON data
    data ={
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [],
    "paddingAll": "0px"
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "image",
        "url": "https://img5.pic.in.th/file/secure-sv1/image2ade59b29ee10cb5.png",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "1:1.11",
        "gravity": "center"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "นาย จิรภา บุญพาสุข",
            "size": "18px",
            "color": "#ffffff",
            "offsetBottom": "-10px"
          },
          {
            "type": "text",
            "text": "xxx-x-x7293-x",
            "size": "lg",
            "color": "#ffffff",
            "offsetStart": "-10px",
            "offsetBottom": "-10px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.postimg.cc/RVBsVdZP/image.png",
                "aspectMode": "fit",
                "size": "xl",
                "action": {
                  "type": "clipboard",
                  "label": "คัดลอก2",
                  "clipboardText": "กรุณาติดต่อแอดมิน @454raxbb"
                },
                "aspectRatio": "4:1"
              }
            ],
            "alignItems": "center",
            "justifyContent": "center",
            "borderWidth": "none",
            "action": {
              "type": "clipboard",
              "label": "คัดลอก2",
              "clipboardText": "กรุณาติดต่อแอดมิน @454raxbb"
            },
            "position": "relative",
            "height": "60px",
            "paddingTop": "10px"
          }
        ],
        "position": "absolute",
        "offsetStart": "30px",
        "paddingStart": "110px",
        "justifyContent": "flex-end",
        "alignItems": "flex-end",
        "paddingTop": "220px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "นาย จิรภา บุญพาสุข",
            "size": "18px",
            "color": "#ffffff",
            "offsetBottom": "-10px"
          },
          {
            "type": "text",
            "text": "xxx-x-x7293-x",
            "size": "lg",
            "color": "#ffffff",
            "offsetStart": "-10px",
            "offsetBottom": "-10px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.postimg.cc/RVBsVdZP/image.png",
                "aspectMode": "fit",
                "size": "xl",
                "action": {
                  "type": "clipboard",
                  "label": "คัดลอก2",
                  "clipboardText": "กรุณาติดต่อแอดมิน @454raxbb"
                },
                "aspectRatio": "4:1"
              }
            ],
            "alignItems": "center",
            "justifyContent": "center",
            "borderWidth": "none",
            "action": {
              "type": "clipboard",
              "label": "คัดลอก2",
              "clipboardText": "กรุณาติดต่อแอดมิน @454raxbb"
            },
            "position": "relative",
            "height": "60px",
            "paddingTop": "5px"
          }
        ],
        "position": "absolute",
        "offsetStart": "30px",
        "paddingStart": "110px",
        "justifyContent": "flex-end",
        "alignItems": "flex-end",
        "paddingTop": "112px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "นาย จิรภา บุญพาสุข",
            "size": "18px",
            "color": "#ffffff",
            "offsetBottom": "-2px"
          },
          {
            "type": "text",
            "text": "xxx-x-x7293-x",
            "size": "lg",
            "color": "#ffffff",
            "offsetStart": "-10px",
            "offsetBottom": "-5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.postimg.cc/RVBsVdZP/image.png",
                "aspectMode": "fit",
                "size": "xl",
                "aspectRatio": "4:1",
                "action": {
                  "type": "clipboard",
                  "label": "คัดลอก2",
                  "clipboardText": "กรุณาติดต่อแอดมิน @454raxbb"
                }
              }
            ],
            "alignItems": "center",
            "justifyContent": "center",
            "borderWidth": "none",
            "action": {
              "type": "clipboard",
              "label": "คัดลอก2",
              "clipboardText": "กรุณาติดต่อแอดมิน @454raxbb"
            },
            "position": "relative",
            "height": "60px",
            "paddingTop": "1px"
          }
        ],
        "position": "absolute",
        "offsetStart": "30px",
        "paddingStart": "110px",
        "justifyContent": "flex-end",
        "alignItems": "flex-end",
        "paddingTop": "sm"
      }
    ],
    "paddingAll": "0px"
  }
}
    



        # เพิ่ม bubble ใน data
   
    # Save data to a JSON file
    with open('flex_message/BANKING.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)

    # ข้อความที่ต้องการส่ง
    notification_message = "Bonustime file created successfully."
    print("Bonustime file created successfully.")
    # ส่งข้อความ
    #send_line_notify(notification_message, line_notify_token)

# กำหนดเวลาที่ต้องการให้งานทำงาน
schedule.every().day.at("00:00").do(job)
schedule.every().day.at("01:00").do(job)
schedule.every().day.at("02:00").do(job)
schedule.every().day.at("03:00").do(job)
schedule.every().day.at("04:00").do(job)
schedule.every().day.at("05:00").do(job)
schedule.every().day.at("06:00").do(job)
schedule.every().day.at("07:00").do(job)
schedule.every().day.at("08:00").do(job)
schedule.every().day.at("09:00").do(job)
schedule.every().day.at("10:00").do(job)
schedule.every().day.at("11:00").do(job)
schedule.every().day.at("12:00").do(job)
schedule.every().day.at("13:00").do(job)
schedule.every().day.at("14:00").do(job)
schedule.every().day.at("15:00").do(job)
schedule.every().day.at("16:00").do(job)
schedule.every().day.at("17:00").do(job)
schedule.every().day.at("18:00").do(job)
schedule.every().day.at("19:00").do(job)
schedule.every().day.at("20:00").do(job)
schedule.every().day.at("21:00").do(job)
schedule.every().day.at("22:00").do(job)
schedule.every().day.at("23:00").do(job)

while True:
    # schedule.run_pending()
    # time.sleep(1)
    job()
    time.sleep(3600)