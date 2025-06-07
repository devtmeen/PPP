import configparser

# อ่านค่าจากไฟล์ config.ini
config = configparser.ConfigParser()
config.read('config.ini')

# ดึงค่า Name_Web และ Game_List จาก config
Name_Web = config['Config']['Name_Web']
Game_List = int(config['Config']['Game_List'])
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

    # อ่านข้อมูลจากไฟล์ WM_casino.json
    with open('WM_casino.json', 'r', encoding='utf-8') as json_file:
        WM_casino = json.load(json_file)

    # สร้างเซ็ตเพื่อเก็บเปอร์เซ็นต์ที่สร้างขึ้นแล้ว
    used_percentages = set()
    used_data = set()
    used_percen_splins = set()
    used_percen_game = set()

    # สร้างข้อความ message_percen และตรวจสอบเปอร์เซ็นต์ในเซ็ต
    def generate_unique_percentage():
        while True:
            global percentage
            percentage = random.uniform(20, 70)
            message_percen = f"{percentage:.2f}%"

            # ตรวจสอบเปอร์เซ็นต์ในทั้งหมดของ "BONUSTIME" และ bubbles
            if message_percen not in used_percentages:
                used_percentages.add(message_percen)
                return message_percen
            
    def generate_unique_percen_splin():
        while True:
            global percentage
            print(percentage)
            percen_splin = 100-percentage
            message_percen_splin = f"{percen_splin:.2f}%"

            # ตรวจสอบเปอร์เซ็นต์ในทั้งหมดของ "BONUSTIME" และ bubbles
            if message_percen_splin not in used_percen_splins:
                used_percen_splins.add(message_percen_splin)
                return message_percen_splin
    
    # สร้างข้อความ message_percen และตรวจสอบเปอร์เซ็นต์ในเซ็ต
    def generate_unique_percentage_game():
        while True:
            percentage_game = random.randint(5, 12)
            percentage_game2 = random.randint(100, 999)
            message_percen_game = f"{percentage_game},{percentage_game2}"

            # ตรวจสอบเปอร์เซ็นต์ในเซ็ต
            if message_percen_game not in used_percen_game:
                used_percen_game.add(message_percen_game)
                return message_percen_game

    Bonustime_Update = formatted_time + ":00 - " + str(num) + ":00 น."
    # สร้าง JSON data
    for _ in range(Game_List):
        game = random.choice(WM_casino)
        
        # สร้างข้อมูลแบบไม่ซ้ำกัน
        while True:
            bg_color = f"{game['bg_color']}"
            bg1_color = f"{game['bg1_color']}"
            bg_image = f"{game['bg_image']}"
            image = f"{game['image']}"
            name = f"{game['name']}"
            
            data_tuple = (bg1_color, bg_color, bg_image, image, name)
            
            if data_tuple not in used_data:
                used_data.add(data_tuple)
                break
            else:
                game = random.choice(WM_casino)

        message_percen = generate_unique_percentage()
        message_percen_splin = generate_unique_percen_splin()
        message_percen_game = generate_unique_percentage_game()
    data = {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://lh3.googleusercontent.com/d/1sufVPRRBIG7x6_q5My483Uc8B2zsCUc4",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "image",
                "url": "https://img2.pic.in.th/pic/WMe689eb001c04c9ca.png",
                "align": "start",
                "size": "xs"
              },
              {
                "type": "text",
                "text": "อัตราการชนะของบาคาร่า",
                "size": "10px",
                "color": "#ffffff",
                "offsetStart": "80px",
                "offsetTop": "-2px",
                "position": "absolute"
              },
              {
                "type": "text",
                "text": name,
                "size": "17px",
                "color": "#ffffff",
                "weight": "bold",
                "position": "absolute",
                "offsetStart": "80px",
                "offsetTop": "15px"
              },
              {
                "type": "text",
                "text": "สูตรมาจากสถิติลูกค้าเล่นจริง",
                "size": "10px",
                "color": "#ffffff",
                "position": "absolute",
                "offsetStart": "80px",
                "offsetTop": "42px"
              }
            ],
            "offsetStart": "-5px",
            "offsetTop": "-10px"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "เพลย์เยอร์ชนะ",
                "size": "10px",
                "color": "#ffffff",
                "offsetStart": "none",
                "offsetTop": "none",
                "margin": "10px"
              },
              {
                "type": "text",
                "text": "แบงค์เกอร์ชนะ",
                "size": "10px",
                "color": "#ffffff",
                "align": "center",
                "weight": "bold"
              },
              {
                "type": "text",
                "text": "ผู้เล่นออนไลน์",
                "size": "10px",
                "color": "#ffffff",
                "align": "center",
                "weight": "bold"
              }
            ],
            "margin": "lg"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": message_percen,
                "size": "lg",
                "color": "#006eff",
                "weight": "bold",
                "margin": "20px",
                "offsetStart": "-10px"
              },
              {
                "type": "text",
                "text": message_percen_splin,
                "size": "lg",
                "color": "#ff0000",
                "align": "center",
                "weight": "bold",
                "offsetStart": "-5px"
              },
              {
                "type": "text",
                "text": message_percen_game,
                "size": "lg",
                "color": "#ffffff",
                "align": "center",
                "weight": "bold"
              }
            ],
            "margin": "lg"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://img5.pic.in.th/file/secure-sv1/the-online-casino-product-from-wm-casino-gamingsoft.png",
                "position": "absolute",
                "size": "45px",
                "offsetStart": "35px",
                "offsetTop": "0px"
              },
              {
                "type": "image",
                "position": "absolute",
                "size": "120px",
                "url": Logo_Web,
                "offsetStart": "100px",
                "offsetTop": "-30px"
              },
              {
                "type": "image",
                "url": "https://img5.pic.in.th/file/secure-sv1/Pngtreethailand-icon-circle_5144221c437c8106b7a102d4f1e4787a2f3d641.png",
                "position": "absolute",
                "offsetTop": "0px",
                "size": "45px",
                "offsetStart": "230px"
              }
            ],
            "offsetTop": "150px",
            "position": "absolute",
            "width": "400px",
            "height": "400px",
            "offsetStart": "-5px"
          },
          {
            "type": "text",
            "text": "ใบรับรอง",
            "size": "10px",
            "margin": "30px",
            "color": "#ffffff",
            "offsetTop": "xl",
            "offsetStart": "lg"
          },
          {
            "type": "text",
            "text": "รองรับภาษา",
            "color": "#ffffff",
            "size": "10px",
            "offsetStart": "200px",
            "offsetTop": "xs"
          }
        ],
        "backgroundColor": "#893900",
        "height": "220px",
        "background": {
          "type": "linearGradient",
          "angle": "180deg",
          "startColor": "#01172b",
          "endColor": "#172240",
          "centerColor": "#01172b"
        }
      }
    }
  ]
}

    # สร้าง bubbles และเพิ่มลงใน data
    for _ in range(Game_List):
        game = random.choice(WM_casino)
        
        # สร้างข้อมูลแบบไม่ซ้ำกัน
        while True:
            bg_color = f"{game['bg_color']}"
            bg1_color = f"{game['bg1_color']}"
            bg_image = f"{game['bg_image']}"
            image = f"{game['image']}"
            name = f"{game['name']}"
            
            data_tuple = (bg1_color, bg_color, bg_image, image, name)
            
            if data_tuple not in used_data:
                used_data.add(data_tuple)
                break
            else:
                game = random.choice(WM_casino)

        message_percen = generate_unique_percentage()
        message_percen_splin = generate_unique_percen_splin()
        message_percen_game = generate_unique_percentage_game()

        bubble =    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://lh3.googleusercontent.com/d/1sufVPRRBIG7x6_q5My483Uc8B2zsCUc4",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "image",
                "url": "https://img2.pic.in.th/pic/WMe689eb001c04c9ca.png",
                "align": "start",
                "size": "xs"
              },
              {
                "type": "text",
                "text": "อัตราการชนะของบาคาร่า",
                "size": "10px",
                "color": "#ffffff",
                "offsetStart": "80px",
                "offsetTop": "-2px",
                "position": "absolute"
              },
              {
                "type": "text",
                "text": name,
                "size": "17px",
                "color": "#ffffff",
                "weight": "bold",
                "position": "absolute",
                "offsetStart": "80px",
                "offsetTop": "15px"
              },
              {
                "type": "text",
                "text": "สูตรมาจากสถิติลูกค้าเล่นจริง",
                "size": "10px",
                "color": "#ffffff",
                "position": "absolute",
                "offsetStart": "80px",
                "offsetTop": "42px"
              }
            ],
            "offsetStart": "-5px",
            "offsetTop": "-10px"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "เพลย์เยอร์ชนะ",
                "size": "10px",
                "color": "#ffffff",
                "offsetStart": "none",
                "offsetTop": "none",
                "margin": "10px"
              },
              {
                "type": "text",
                "text": "แบงค์เกอร์ชนะ",
                "size": "10px",
                "color": "#ffffff",
                "align": "center",
                "weight": "bold"
              },
              {
                "type": "text",
                "text": "ผู้เล่นออนไลน์",
                "size": "10px",
                "color": "#ffffff",
                "align": "center",
                "weight": "bold"
              }
            ],
            "margin": "lg"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": message_percen,
                "size": "lg",
                "color": "#006eff",
                "weight": "bold",
                "margin": "20px",
                "offsetStart": "-10px"
              },
              {
                "type": "text",
                "text": message_percen_splin,
                "size": "lg",
                "color": "#ff0000",
                "align": "center",
                "weight": "bold",
                "offsetStart": "-5px"
              },
              {
                "type": "text",
                "text": message_percen_game,
                "size": "lg",
                "color": "#ffffff",
                "align": "center",
                "weight": "bold"
              }
            ],
            "margin": "lg"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://img5.pic.in.th/file/secure-sv1/the-online-casino-product-from-wm-casino-gamingsoft.png",
                "position": "absolute",
                "size": "45px",
                "offsetStart": "35px",
                "offsetTop": "0px"
              },
              {
                "type": "image",
                "position": "absolute",
                "size": "120px",
                "url": Logo_Web,
                "offsetStart": "100px",
                "offsetTop": "-30px"
              },
              {
                "type": "image",
                "url": "https://img5.pic.in.th/file/secure-sv1/Pngtreethailand-icon-circle_5144221c437c8106b7a102d4f1e4787a2f3d641.png",
                "position": "absolute",
                "offsetTop": "0px",
                "size": "45px",
                "offsetStart": "230px"
              }
            ],
            "offsetTop": "150px",
            "position": "absolute",
            "width": "400px",
            "height": "400px",
            "offsetStart": "-5px"
          },
          {
            "type": "text",
            "text": "ใบรับรอง",
            "size": "10px",
            "margin": "30px",
            "color": "#ffffff",
            "offsetTop": "xl",
            "offsetStart": "lg"
          },
          {
            "type": "text",
            "text": "รองรับภาษา",
            "color": "#ffffff",
            "size": "10px",
            "offsetStart": "200px",
            "offsetTop": "xs"
          }
        ],
        "backgroundColor": "#893900",
        "height": "220px",
        "background": {
          "type": "linearGradient",
          "angle": "180deg",
          "startColor": "#01172b",
          "endColor": "#172240",
          "centerColor": "#01172b"
        }
      }
    }
    

        

        


        # เพิ่ม bubble ใน data
        data["contents"].append(bubble)

    # Save data to a JSON file
    with open('flex_message/BONUSTIME_WM.json', 'w', encoding='utf-8') as json_file:
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