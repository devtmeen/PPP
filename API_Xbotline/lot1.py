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

    # อ่านข้อมูลจากไฟล์ FB_game.json
    with open('FB_game.json', 'r', encoding='utf-8') as json_file:
        FB_game = json.load(json_file)

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

    # การ์ด 1
    data = {
  "type": "bubble",
  "size": "giga",
  "hero": {
    "type": "image",
    "url": "https://image.tnews.co.th/uploads/images/md/2024/02/xmWhUt7pRtPWFRCgu6sS.webp?x-image-process=style/LG",
    "size": "full",
    "aspectRatio": "9:4",
    "aspectMode": "cover"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "18 ตุลาคม 2567",
        "align": "center",
        "color": "#ffff00",
        "size": "xl",
        "weight": "bold",
        "offsetTop": "-5px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "text",
                        "text": "ฮานอยพิเศษ 18 ตุลาคม 2567",
                        "align": "center",
                        "color": "#ffffff",
                        "size": "md"
                      }
                    ]
                  },
                  {
                    "type": "separator"
                  },
                  {
                    "type": "separator"
                  },
                  {
                    "type": "separator"
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
                            "type": "text",
                            "text": "สามตัวบน",
                            "align": "center",
                            "color": "#ffffff",
                            "size": "md"
                          },
                          {
                            "type": "text",
                            "text": "938",
                            "align": "center",
                            "color": "#ffffff",
                            "size": "xxl",
                            "weight": "bold"
                          }
                        ]
                      },
                      {
                        "type": "separator"
                      },
                      {
                        "type": "separator"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "2 ตัวล่าง",
                            "align": "center",
                            "color": "#ffffff",
                            "size": "md"
                          },
                          {
                            "type": "text",
                            "text": "47",
                            "align": "center",
                            "color": "#ffffff",
                            "size": "xxl",
                            "weight": "bold"
                          }
                        ]
                      }
                    ]
                  }
                ],
                "backgroundColor": "#e22426",
                "cornerRadius": "none",
                "paddingAll": "none",
                "margin": "none"
              }
            ]
          }
        ],
        "spacing": "xs",
        "margin": "xs",
        "cornerRadius": "xxl",
        "height": "100px",
        "offsetTop": "none",
        "position": "relative"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "ฮานอยปกติ 18 ตุลาคม 2567",
                "align": "center",
                "color": "#ffffff",
                "size": "md",
                "offsetTop": "7px"
              }
            ],
            "height": "30px"
          },
          {
            "type": "separator"
          },
          {
            "type": "separator"
          },
          {
            "type": "separator"
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
                    "type": "text",
                    "text": "3 ตัวบน",
                    "align": "center",
                    "color": "#ffffff",
                    "size": "md"
                  },
                  {
                    "type": "text",
                    "text": "972",
                    "align": "center",
                    "color": "#ffffff",
                    "size": "xxl",
                    "weight": "bold"
                  }
                ],
                "backgroundColor": "#0258a5",
                "cornerRadius": "md",
                "paddingAll": "none",
                "margin": "none"
              },
              {
                "type": "separator"
              },
              {
                "type": "separator"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "2 ตัวล่าง",
                    "align": "center",
                    "color": "#ffffff",
                    "size": "md"
                  },
                  {
                    "type": "text",
                    "text": "08",
                    "align": "center",
                    "color": "#ffffff",
                    "size": "xxl",
                    "weight": "bold"
                  }
                ],
                "backgroundColor": "#0258a5",
                "cornerRadius": "md",
                "paddingAll": "none",
                "margin": "none"
              }
            ],
            "backgroundColor": "#0258a5",
            "cornerRadius": "none",
            "margin": "xs",
            "offsetTop": "none"
          }
        ],
        "backgroundColor": "#0258a5",
        "cornerRadius": "none",
        "margin": "xxl",
        "offsetTop": "-30px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "separator"
          },
          {
            "type": "separator"
          },
          {
            "type": "separator"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [],
            "backgroundColor": "#00a65a",
            "cornerRadius": "none",
            "paddingAll": "none",
            "margin": "none"
          }
        ],
        "spacing": "none",
        "margin": "none"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                      {
                        "type": "text",
                        "text": "ฮานอยวีไอพี 18 ตุลาคม 2567",
                        "align": "center",
                        "color": "#ffffff",
                        "size": "md"
                      }
                    ],
                    "backgroundColor": "#eb951a"
                  },
                  {
                    "type": "separator"
                  },
                  {
                    "type": "separator"
                  },
                  {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                      {
                        "type": "text",
                        "text": "587",
                        "align": "center",
                        "color": "#ffffff",
                        "size": "xxl",
                        "weight": "bold"
                      },
                      {
                        "type": "separator"
                      },
                      {
                        "type": "separator"
                      },
                      {
                        "type": "text",
                        "text": "85",
                        "align": "center",
                        "color": "#ffffff",
                        "size": "xxl",
                        "weight": "bold"
                      }
                    ],
                    "backgroundColor": "#eb951a",
                    "cornerRadius": "none",
                    "paddingAll": "none",
                    "margin": "none",
                    "height": "50px"
                  }
                ],
                "backgroundColor": "#eb951a",
                "cornerRadius": "none",
                "paddingAll": "none",
                "margin": "none",
                "offsetEnd": "none",
                "offsetTop": "30px",
                "offsetBottom": "none",
                "paddingTop": "xs"
              }
            ],
            "height": "100px",
            "offsetTop": "-20px"
          }
        ],
        "spacing": "none",
        "margin": "none",
        "cornerRadius": "xxl",
        "height": "90px",
        "offsetTop": "-45px",
        "position": "relative",
        "offsetBottom": "sm",
        "paddingTop": "md"
      },
      {
        "type": "text",
        "text": "ข้อมูลจาก: สมาคมสลากกินแบ่งถูมิภาคเอเชียแปซิฟิก",
        "align": "end",
        "color": "#ffffff",
        "size": "xs",
        "offsetTop": "-35px"
      },
      {
        "type": "text",
        "text": "อ้างอิง : สมาคมสลากกินแบ่งโลก",
        "align": "end",
        "color": "#ffffff",
        "size": "xs",
        "offsetTop": "-35px"
      }
    ],
    "backgroundColor": "#162c43",
    "paddingAll": "20px",
    "height": "380px",
    "background": {
      "type": "linearGradient",
      "angle": "180deg",
      "startColor": "#690004",
      "endColor": "#690004",
      "centerColor": "#4d0001"
    }
  }
}
    



        # เพิ่ม bubble ใน data
   
    # Save data to a JSON file
    with open('flex_message/หวยฮานอย.json', 'w', encoding='utf-8') as json_file:
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