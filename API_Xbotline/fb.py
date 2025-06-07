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
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        # รูปทีมการ์ด 1
        "url": "https://ball7m.com/img/match_preview_img/2024-10-18/6711d59981282.png",
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
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "text",
                     # ชื่อทีม ซ้าย การ์ด 1
                    "text": "อลาเบส",
                    "size": "13px",
                    "color": "#ffffff",
                    "offsetStart": "none",
                    "offsetTop": "none",
                    "margin": "10px",
                    "align": "start"
                  },
                  {
                    "type": "text",
                     # ชื่อทีม ขวา การ์ด 1
                    "text": "เรอัล บายาโดลิด",
                    "size": "13px",
                    "color": "#ffffff",
                    "align": "end",
                    "weight": "bold",
                    "offsetEnd": "10px"
                  }
                ],
                "margin": "none",
                "justifyContent": "center",
                "alignItems": "center"
              },
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "text",
                    # เปอร์เซ็น ซ้าย การ์ด 1
                    "text": "80%",
                    "size": "xl",
                    "color": "#006eff",
                    "weight": "bold",
                    "margin": "20px",
                    "align": "start",
                    "offsetStart": "-10px"
                  },
                  {
                    "type": "text",
                    # เปอร์เซ็น ขวา การ์ด 1
                    "text": "20%",
                    "size": "xl",
                    "color": "#ff0000",
                    "align": "end",
                    "weight": "bold",
                    "margin": "20px",
                    "offsetEnd": "10px"
                  }
                ],
                "margin": "none",
                "justifyContent": "center",
                "alignItems": "center",
                "spacing": "none"
              }
            ],
            "offsetTop": "-15px"
          },
          {
            "type": "image",
            "position": "absolute",
            "size": "100px",
            "url": "https://i.postimg.cc/1XKn3yjT/Pngtree-sports-turnament-versus-vs-background-5997509-1.png",
            "offsetStart": "100px",
            "offsetTop": "-20px",
            "align": "center"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                # วิเคราะห์ การ์ด 1
                "text": " อลาเบส เกมนี้ในบ้านจัดหนักแน่หลังแพ้มาเยอะ เกมนี้เดินหน้าเต็มที่สถิติเจอกันก็ดีกว่าเยอะ  ทีมเยือนเรอัล บายาโดลิด ตอนนี้หวังเสมอก็ยากแล้วเกมนี้มารับเต็มที่  เกมนี้คาดว่า อลาเบส น่าจะกลับมาชนะได้แน่นอน",
                "color": "#ffffff",
                "margin": "md",
                "size": "xxs",
                "wrap": True
              }
            ],
            "offsetTop": "-13px"
          }
        ],
        "backgroundColor": "#893900",
        "background": {
          "type": "linearGradient",
          "angle": "180deg",
          "startColor": "#000000",
          "endColor": "#2e2e2e",
          "centerColor": "#000000"
        }
      }
    },
    # การ์ด 2
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        # รูปทีมการ์ด 2
        "url": "https://ball7m.com/img/match_preview_thumbnail/2024-10-18/6711d56719791.png",
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
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "text",
                     # ชื่อทีม ซ้าย การ์ด 2
                    "text": "ดอร์ทมุนด์",
                    "size": "13px",
                    "color": "#ffffff",
                    "offsetStart": "none",
                    "offsetTop": "none",
                    "margin": "10px",
                    "align": "start"
                  },
                  {
                    "type": "text",
                    # ชื่อทีม ขวา การ์ด 2
                    "text": "ซังค์ เพาลี",
                    "size": "13px",
                    "color": "#ffffff",
                    "align": "end",
                    "weight": "bold",
                    "offsetEnd": "10px"
                  }
                ],
                "margin": "none",
                "justifyContent": "center",
                "alignItems": "center"
              },
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "text",
                    # เปอร์เซ็น ซ้าย การ์ด 2
                    "text": "90%",
                    "size": "xl",
                    "color": "#006eff",
                    "weight": "bold",
                    "margin": "20px",
                    "align": "start",
                    "offsetStart": "-10px"
                  },
                  {
                    "type": "text",
                    # เปอร์เซ็น ขวา การ์ด 2
                    "text": "10%",
                    "size": "xl",
                    "color": "#ff0000",
                    "align": "end",
                    "weight": "bold",
                    "margin": "20px",
                    "offsetEnd": "10px"
                  }
                ],
                "margin": "none",
                "justifyContent": "center",
                "alignItems": "center",
                "spacing": "none"
              }
            ],
            "offsetTop": "-15px"
          },
          {
            "type": "image",
            "position": "absolute",
            "size": "100px",
            "url": "https://i.postimg.cc/1XKn3yjT/Pngtree-sports-turnament-versus-vs-background-5997509-1.png",
            "offsetStart": "100px",
            "offsetTop": "-20px",
            "align": "center"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                # วิเคราะห์ การ์ด 2
                "text": "โบรุสเซีย ดอร์ทมุนด์  ต้องการชนะเพื่อไล่กลุ่มผู้นำ เกมนี้ไล่อัดยับตั้งแต่นาทีแรกแน่นอน ทีมเยือนซังค์ เพาลี  เป็นรองเยอะแถมฟอร์มไม่ดี เกมนี้ เน้นรับหวังเสมอ แต่ดูทรงแล้ว โบรุสเซีย ดอร์ทมุนด์  น่าจะชนะได้ไม่ยาก",
                "color": "#ffffff",
                "margin": "md",
                "size": "xxs",
                "wrap": True
              }
            ],
            "offsetTop": "-13px"
          }
        ],
        "backgroundColor": "#893900",
        "background": {
          "type": "linearGradient",
          "angle": "180deg",
          "startColor": "#000000",
          "endColor": "#2e2e2e",
          "centerColor": "#000000"
        }
      }
    },
    # การ์ด 3
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        # รูปทีมการ์ด 3
        "url": "https://ball7m.com/img/match_preview_thumbnail/2024-10-17/671086d7675b4.png",
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
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "text",
                    # ชื่อทีม ซ้าย การ์ด 3
                    "text": "คอรินเธี่ยนส์ ",
                    "size": "13px",
                    "color": "#ffffff",
                    "offsetStart": "none",
                    "offsetTop": "none",
                    "margin": "10px",
                    "align": "start"
                  },
                  {
                    "type": "text",
                    # ชื่อทีม ขวา การ์ด 3
                    "text": "แอตเลติโก้ ",
                    "size": "13px",
                    "color": "#ffffff",
                    "align": "end",
                    "weight": "bold",
                    "offsetEnd": "10px"
                  }
                ],
                "margin": "none",
                "justifyContent": "center",
                "alignItems": "center"
              },
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "text",
                    # เปอร์เซ็น ซ้าย การ์ด 3
                    "text": "70%",
                    "size": "xl",
                    "color": "#006eff",
                    "weight": "bold",
                    "margin": "20px",
                    "align": "start",
                    "offsetStart": "-10px"
                  },
                  {
                    "type": "text",
                    # เปอร์เซ็น ขวา การ์ด 3
                    "text": "30%",
                    "size": "xl",
                    "color": "#ff0000",
                    "align": "end",
                    "weight": "bold",
                    "margin": "20px",
                    "offsetEnd": "10px"
                  }
                ],
                "margin": "none",
                "justifyContent": "center",
                "alignItems": "center",
                "spacing": "none"
              }
            ],
            "offsetTop": "-15px"
          },
          {
            "type": "image",
            "position": "absolute",
            "size": "100px",
            "url": "https://i.postimg.cc/1XKn3yjT/Pngtree-sports-turnament-versus-vs-background-5997509-1.png",
            "offsetStart": "100px",
            "offsetTop": "-20px",
            "align": "center"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                # วิเคราะห์ การ์ด 3
                "text": "โครินเธี่ยนส์ ฟอร์มไม่ค่อยจะดีในลีก เกมนี้ในบ้านคงต้องการชนะหนีโซนตกชั้น เกมนี้เดินหน้าเกมรุกใส่เต็มที่  ทีมเยือนแอตเลติโก้ พาราเนนเซ่ ฟอร์มทไม่ดีเช่นกันแพ้มารัวๆ เกมนี้มาตั้งรับรอสวนกลับ ในการเจอกันมา เจ้าบ้านเหนือกว่าเยอะ เกมนี้คาดว่า  โครินเธี่ยนส์  น่าจะเอาชนะได้แน่นอน",
                "color": "#ffffff",
                "margin": "md",
                "size": "xxs",
                "wrap": True
              }
            ],
            "offsetTop": "-13px"
          }
        ],
        "backgroundColor": "#893900",
        "background": {
          "type": "linearGradient",
          "angle": "180deg",
          "startColor": "#000000",
          "endColor": "#2e2e2e",
          "centerColor": "#000000"
        }
      }
    },
    # การ์ด 4
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        # รูปทีมการ์ด 4
        "url": "https://ball7m.com/img/match_preview_thumbnail/2024-10-18/6711d534abbcf.png",
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
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "text",
                    # ชื่อทีม ซ้าย การ์ด 4
                    "text": "โมนาโก",
                    "size": "13px",
                    "color": "#ffffff",
                    "offsetStart": "none",
                    "offsetTop": "none",
                    "margin": "10px",
                    "align": "start"
                  },
                  {
                    "type": "text",
                    # ชื่อทีม ขวา การ์ด 4
                    "text": "ลีลล์",
                    "size": "13px",
                    "color": "#ffffff",
                    "align": "end",
                    "weight": "bold",
                    "offsetEnd": "10px"
                  }
                ],
                "margin": "none",
                "justifyContent": "center",
                "alignItems": "center"
              },
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "text",
                    # เปอร์เซ็น ซ้าย การ์ด 4
                    "text": "55%",
                    "size": "xl",
                    "color": "#006eff",
                    "weight": "bold",
                    "margin": "20px",
                    "align": "start",
                    "offsetStart": "-10px"
                  },
                  {
                    "type": "text",
                    # เปอร์เซ็น ขวา การ์ด 4
                    "text": "45%",
                    "size": "xl",
                    "color": "#ff0000",
                    "align": "end",
                    "weight": "bold",
                    "margin": "20px",
                    "offsetEnd": "10px"
                  }
                ],
                "margin": "none",
                "justifyContent": "center",
                "alignItems": "center",
                "spacing": "none"
              }
            ],
            "offsetTop": "-15px"
          },
          {
            "type": "image",
            "position": "absolute",
            "size": "100px",
            "url": "https://i.postimg.cc/1XKn3yjT/Pngtree-sports-turnament-versus-vs-background-5997509-1.png",
            "offsetStart": "100px",
            "offsetTop": "-20px",
            "align": "center"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                # วิเคราะห์ การ์ด 4
                "text": "โมนาโก จ่าฝูง เกมนี้ต้องการชัยชนะอย่างต่อเนื่อง เกมนี้ลุยเต็มที่ ทีมเยือน ลีลล์ เกมนี้เป็นรองพอสมควร เกมเยือนแย่ เกมนี้ตั้งรับรอสวนกลับอย่างเดียว เกมนี้คาดว่า  โมนาโก น่าจะเบียดชนะไปได้ ",
                "color": "#ffffff",
                "margin": "md",
                "size": "xxs",
                "wrap": True
              }
            ],
            "offsetTop": "-13px"
          }
        ],
        "backgroundColor": "#893900",
        "background": {
          "type": "linearGradient",
          "angle": "180deg",
          "startColor": "#000000",
          "endColor": "#2e2e2e",
          "centerColor": "#000000"
        }
      }
    },
    # การ์ด 5
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        # รูปทีมการ์ด 5
        "url": "https://ball7m.com/img/match_preview_thumbnail/2024-10-18/6711d5027d03f.png",
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
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "text",
                    # ชื่อทีม ซ้าย การ์ด 5
                    "text": "ลีดส์ ",
                    "size": "13px",
                    "color": "#ffffff",
                    "offsetStart": "none",
                    "offsetTop": "none",
                    "margin": "10px",
                    "align": "start"
                  },
                  {
                    "type": "text",
                    # ชื่อทีม ขวา การ์ด 5
                    "text": "เชฟฟิลด์",
                    "size": "13px",
                    "color": "#ffffff",
                    "align": "end",
                    "weight": "bold",
                    "offsetEnd": "10px"
                  }
                ],
                "margin": "none",
                "justifyContent": "center",
                "alignItems": "center"
              },
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "text",
                    # เปอร์เซ็น ซ้าย การ์ด 5
                    "text": "47%",
                    "size": "xl",
                    "color": "#006eff",
                    "weight": "bold",
                    "margin": "20px",
                    "align": "start",
                    "offsetStart": "-10px"
                  },
                  {
                    "type": "text",
                    # เปอร์เซ็น ขวา การ์ด 5
                    "text": "53%",
                    "size": "xl",
                    "color": "#ff0000",
                    "align": "end",
                    "weight": "bold",
                    "margin": "20px",
                    "offsetEnd": "10px"
                  }
                ],
                "margin": "none",
                "justifyContent": "center",
                "alignItems": "center",
                "spacing": "none"
              }
            ],
            "offsetTop": "-15px"
          },
          {
            "type": "image",
            "position": "absolute",
            "size": "100px",
            "url": "https://i.postimg.cc/1XKn3yjT/Pngtree-sports-turnament-versus-vs-background-5997509-1.png",
            "offsetStart": "100px",
            "offsetTop": "-20px",
            "align": "center"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                # วิเคราะห์ การ์ด 5
                "text": "ลีดส์ ยูไนเต็ด ไม่ง่ายแน่เกมนี้ ในบ้านคงเแิดเกมรุกแลกเต็มที่หวังจะชนะให้ได้ ทีมเยือนเชฟฟิลด์ ยูไนเต็ดยังไม่เคยแพ้ แต่ยังไม่ประมาท มาประครองเกมรอเกมสวนกลับ เกมนี้คาดว่า เจ้าบ้านราคาต่อเยอะ คิดว่า เชฟฟิลด์ ยูไนเต็ด ไม่นา่แพ้และอาจจะเบียดชนะได้",
                "color": "#ffffff",
                "margin": "md",
                "size": "xxs",
                "wrap": True
              }
            ],
            "offsetTop": "-13px"
          }
        ],
        "backgroundColor": "#893900",
        "background": {
          "type": "linearGradient",
          "angle": "180deg",
          "startColor": "#000000",
          "endColor": "#2e2e2e",
          "centerColor": "#000000"
        }
      }
    }
  ]
}
    



        # เพิ่ม bubble ใน data
   
    # Save data to a JSON file
    with open('flex_message/FOOTBALL.json', 'w', encoding='utf-8') as json_file:
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