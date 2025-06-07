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

    # อ่านข้อมูลจากไฟล์ `JK_Game.json
    with open('JK_game.json', 'r', encoding='utf-8') as json_file:
        JK_game = json.load(json_file)

    # สร้างเซ็ตเพื่อเก็บเปอร์เซ็นต์ที่สร้างขึ้นแล้ว
    used_percentages = set()
    used_data = set()
    used_percen_splins = set()
    used_percen_game = set()

    # สร้างข้อความ message_percen และตรวจสอบเปอร์เซ็นต์ในเซ็ต
    def generate_unique_percentage():
        while True:
            percentage = random.uniform(70, 98)
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

    Bonustime_Update = formatted_time + ":00 - " + str(num) + ":00 น."
    # สร้าง JSON data
    data = {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "mega",
      "hero": {
        "type": "image",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "action": {
          "type": "uri",
          "uri": Link_Web
        },
        "url": "https://img5.pic.in.th/file/secure-sv1/JK.png",
        "animated": True
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "ตั้งแต่เวลา" +Bonustime_Update,
                "weight": "bold",
                "align": "end",
                "color": "#ffffff",
                "size": "20px",
                "offsetTop": "-5px"
              },
              {
                "type": "image",
                "url": "https://img5.pic.in.th/file/secure-sv1/H103.png",
                "size": "4xl",
                "position": "relative",
                "animated": True,
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": Link_Web
                },
                "offsetTop": "-85px"
              },
              {
                "type": "text",
                "text": "สูตรสล็อตอัตราการชนะเกมจาก",
                "weight": "bold",
                "align": "center",
                "color": "#ffffff",
                "size": "sm",
                "offsetTop": "-165px"
              },
              {
                "type": "text",
                "text": "ค่ายยอดฮิต สถิติจากลูกค้าเล่นจริงถอน",
                "align": "center",
                "color": "#ffffff",
                "size": "sm",
                "weight": "bold",
                "offsetTop": "-165px"
              },
              {
                "type": "text",
                "text": "จริง เราการันตรีเล่นตาม ทำกำไรให้คุณ",
                "weight": "bold",
                "align": "center",
                "color": "#ffffff",
                "size": "sm",
                "offsetTop": "-165px"
              },
              {
                "type": "text",
                "text": "ได้อย่างแน่นอน 100%",
                "weight": "bold",
                "align": "center",
                "color": "#ffffff",
                "size": "sm",
                "offsetTop": "-165px"
              }
            ],
            "paddingAll": "6px"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [],
            "offsetStart": "2px",
            "offsetTop": "-2px"
          },
          {
            "type": "image",
            "url": "https://img2.pic.in.th/pic/register_button.gif",
            "offsetTop": "115px",
            "size": "xl",
            "position": "absolute",
            "offsetStart": "155px",
            "animated": True,
            "action": {
              "type": "uri",
              "label": "action",
              "uri": Link_Web
            }
          },
          {
            "type": "image",
            "url": "https://img2.pic.in.th/pic/2login_button-joker89-1.gif",
            "offsetTop": "115px",
            "size": "xl",
            "position": "absolute",
            "offsetStart": "15px",
            "animated": True,
            "action": {
              "type": "uri",
              "label": "action",
              "uri": Link_Web
            }
          }
        ],
        "backgroundColor": "#000000",
        "height": "210px",
        "action": {
          "type": "uri",
          "label": "action",
          "uri": Link_Web
        }
      }
    }
  ]
}


    # สร้าง bubbles และเพิ่มลงใน data
    for _ in range(Game_List):
        game = random.choice(JK_game)
        
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
                game = random.choice(JK_game)

        message_percen = generate_unique_percentage()
        message_percen_splin = generate_unique_percen_splin()
        message_percen_game = generate_unique_percentage_game()

        bubble =     {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": bg_image,
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "backgroundColor": "#000000"
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
                "url": image,
                "align": "start",
                "size": "xs"
              },
              {
                "type": "text",
                "text": "อัตราการชนะของเกม",
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
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "image",
                    "size": "full",
                    "animated": True,
                    "aspectMode": "fit",
                    "offsetTop": "none",
                    "url": "https://img5.pic.in.th/file/secure-sv1/ezgif.com-effects-14.png",
                    "aspectRatio": "2:1",
                    "position": "absolute"
                  }
                ],
                "width": message_percen,
                "height": "100%",
                "cornerRadius": "xxl",
                "borderWidth": "light",
                "borderColor": "#363636"
              },
              {
                "type": "text",
                "text": message_percen,
                "color": "#000000",
                "size": "md",
                "offsetStart": "110px",
                "weight": "bold",
                "position": "absolute",
                "offsetBottom": "xs"
              }
            ],
            "margin": "sm",
            "height": "25px",
            "cornerRadius": "xl",
            "width": "260px",
            "backgroundColor": "#3a3a3a",
            "borderColor": "#3a3a3a",
            "spacing": "xxl"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "โอกาศชนะ",
                "size": "10px",
                "color": "#ffffff",
                "offsetStart": "none",
                "offsetTop": "none",
                "margin": "10px"
              },
              {
                "type": "text",
                "text": "เข้าฟรีสปิน",
                "size": "10px",
                "color": "#ffffff",
                "align": "center",
                "weight": "bold",
                "offsetStart": "none"
              },
              {
                "type": "text",
                "text": "ตัวคูณสูงสุด",
                "size": "10px",
                "color": "#ffffff",
                "align": "center",
                "weight": "bold"
              }
            ],
            "offsetStart": "2px",
            "offsetTop": "-2px",
            "margin": "lg"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": message_percen,
                "size": "md",
                "color": "#ffffff",
                "offsetEnd": "lg",
                "weight": "bold",
                "margin": "22px"
              },
              {
                "type": "text",
                "text": message_percen_splin,
                "size": "md",
                "color": "#ffffff",
                "align": "center",
                "weight": "bold"
              },
              {
                "type": "text",
                "text": message_percen_game,
                "size": "md",
                "color": "#ffffff",
                "align": "center",
                "weight": "bold"
              }
            ],
            "offsetStart": "2px",
            "offsetTop": "-2px",
            "margin": "xs"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://img5.pic.in.th/file/secure-sv1/joker-gaming-logo.png",
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
            "height": "50px",
            "offsetStart": "-3px"
          },
          {
            "type": "text",
            "text": "ใบรับรอง",
            "size": "10px",
            "margin": "30px",
            "color": "#ffffff",
            "offsetTop": "none",
            "offsetStart": "lg"
          },
          {
            "type": "text",
            "text": "รองรับภาษา",
            "color": "#ffffff",
            "size": "10px",
            "offsetStart": "200px",
            "offsetTop": "-15px"
          }
        ],
        "backgroundColor": bg_color,
        "height": "210px",
        "background": {
          "type": "linearGradient",
          "angle": "180deg",
          "startColor": bg_color,
          "endColor": bg1_color,
          "centerColor": bg_color
        }
      }
    }

    

        

        


        # เพิ่ม bubble ใน data
        data["contents"].append(bubble)

    # Save data to a JSON file
    with open('flex_message/BONUSTIME_JK.json', 'w', encoding='utf-8') as json_file:
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

