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
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://lh3.googleusercontent.com/d/1-H6iM_bNdBdJKGN-abIgzA6TfLd9Txh0",
        "size": "full",
        "aspectRatio": "4:2.5",
        "aspectMode": "fit"
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
                "type": "image",
                "url": "https://img2.pic.in.th/pic/5e9bedf89a52092b4d5615e211eab7aa9959717cc5fd2798da2a85005ae46a4f.png",
                "position": "absolute",
                "size": "full",
                "aspectRatio": "3:4.2",
                "aspectMode": "cover",
                "animated": True,
                "offsetTop": "-50px"
              }
            ],
            "position": "absolute",
            "width": "300px",
            "height": "430px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://lh3.googleusercontent.com/d/11-ui2nISzzgHwS5R5FVIWOcF8InSoIye",
                "position": "absolute",
                "size": "85px"
              }
            ],
            "paddingAll": "none",
            "action": {
              "type": "message",
              "label": "action",
              "text": "/BONUSTIME_PG"
            },
            "position": "absolute",
            "height": "90px",
            "offsetStart": "10px",
            "offsetTop": "10px",
            "width": "90px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://lh3.googleusercontent.com/d/1FmRGIj6Su3ZiR8L9MNCEe9v9SiYF0qml",
                "position": "absolute",
                "size": "85px"
              }
            ],
            "position": "absolute",
            "height": "90px",
            "width": "90px",
            "offsetTop": "10px",
            "offsetStart": "108px",
            "paddingAll": "none",
            "action": {
              "type": "message",
              "label": "action",
              "text": "/BONUSTIME_PP"
            }
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://lh3.googleusercontent.com/d/1y_gKwbp-fvZHr8hJRiLhth8RC8Z4Owpn",
                "position": "absolute",
                "size": "85px"
              }
            ],
            "position": "absolute",
            "height": "90px",
            "width": "90px",
            "offsetTop": "10px",
            "offsetStart": "205px",
            "paddingAll": "none",
            "action": {
              "type": "message",
              "label": "action",
              "text": "/BONUSTIME_JK"
            }
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://lh3.googleusercontent.com/d/1qLNPkggx5633bJ1GJeu616e-ZMK5L0g2",
                "position": "absolute",
                "size": "85px"
              }
            ],
            "position": "absolute",
            "height": "90px",
            "width": "90px",
            "offsetTop": "105px",
            "offsetStart": "10px",
            "paddingAll": "none",
            "action": {
              "type": "message",
              "label": "action",
              "text": "/BONUSTIME_MG"
            }
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://lh3.googleusercontent.com/d/13U5H1r_YF9SS4Seo8B4HN6xSDcAoHcNC",
                "position": "absolute",
                "size": "85px"
              }
            ],
            "position": "absolute",
            "height": "90px",
            "width": "90px",
            "offsetTop": "105px",
            "offsetStart": "108px",
            "paddingAll": "none",
            "action": {
              "type": "message",
              "label": "action",
              "text": "/BONUSTIME_JL"
            }
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://lh3.googleusercontent.com/d/1ZZCw9JgTGBY79ucajTwEDhp0B1fbY3HW",
                "position": "absolute",
                "size": "85px"
              }
            ],
            "position": "absolute",
            "height": "90px",
            "width": "90px",
            "offsetTop": "105px",
            "offsetStart": "205px",
            "paddingAll": "none",
            "action": {
              "type": "message",
              "label": "action",
              "text": "/BONUSTIME_SN"
            }
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://lh3.googleusercontent.com/d/1lls_tJRe_QiQJ2pAanvjoQ5B1c5An4eo",
                "position": "absolute",
                "size": "85px"
              }
            ],
            "position": "absolute",
            "height": "90px",
            "width": "90px",
            "offsetTop": "200px",
            "offsetStart": "205px",
            "paddingAll": "none",
            "action": {
              "type": "message",
              "label": "action",
              "text": "/BONUSTIME_AMB"
            }
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://lh3.googleusercontent.com/d/1YFCqEYL3UG3HbRyJCENm6PTrNYTOo9Gz",
                "position": "absolute",
                "size": "85px"
              }
            ],
            "position": "absolute",
            "height": "90px",
            "width": "90px",
            "offsetTop": "200px",
            "offsetStart": "108px",
            "paddingAll": "none",
            "action": {
              "type": "message",
              "label": "action",
              "text": "/BONUSTIME_NL"
            }
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://lh3.googleusercontent.com/d/1sDlTK7owSyfI0ABI767d9g4W1XB-JqBb",
                "position": "absolute",
                "size": "85px"
              }
            ],
            "position": "absolute",
            "height": "90px",
            "width": "90px",
            "offsetTop": "200px",
            "offsetStart": "10px",
            "paddingAll": "none",
            "action": {
              "type": "message",
              "label": "action",
              "text": "/BONUSTIME_NE"
            }
          }
        ],
        "paddingTop": "none",
        "paddingBottom": "none",
        "paddingStart": "none",
        "paddingEnd": "none",
        "height": "300px",
        "backgroundColor": "#545454",
        "maxWidth": "300px"
      },
      "styles": {
        "hero": {
          "backgroundColor": "#000000"
        }
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://lh3.googleusercontent.com/d/1-H6iM_bNdBdJKGN-abIgzA6TfLd9Txh0",
        "size": "full",
        "aspectRatio": "4:2.5",
        "aspectMode": "fit"
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
                "type": "image",
                "url": "https://img2.pic.in.th/pic/5e9bedf89a52092b4d5615e211eab7aa9959717cc5fd2798da2a85005ae46a4f.png",
                "position": "absolute",
                "size": "full",
                "aspectRatio": "3:4.2",
                "aspectMode": "cover",
                "animated": True,
                "offsetTop": "-50px"
              }
            ],
            "position": "absolute",
            "width": "300px",
            "height": "430px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://lh3.googleusercontent.com/d/1qcW23uDO5KW9yNV5zXlb-IAWvBwzvofM",
                "position": "absolute",
                "size": "85px"
              }
            ],
            "paddingAll": "none",
            "action": {
              "type": "message",
              "label": "action",
              "text": "/BONUSTIME_AMBS"
            },
            "position": "absolute",
            "height": "90px",
            "offsetStart": "10px",
            "offsetTop": "10px",
            "width": "90px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://lh3.googleusercontent.com/d/1PBmISkgv0pny12NXf--QlhTkksPu8UFC",
                "position": "absolute",
                "size": "85px"
              }
            ],
            "position": "absolute",
            "height": "90px",
            "width": "90px",
            "offsetTop": "10px",
            "offsetStart": "108px",
            "paddingAll": "none",
            "action": {
              "type": "message",
              "label": "action",
              "text": "/BONUSTIME_CQ9"
            }
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://lh3.googleusercontent.com/d/1tXW3Kou84zan6TnDvEQWuRMxm2MC02zx",
                "position": "absolute",
                "size": "85px"
              }
            ],
            "position": "absolute",
            "height": "90px",
            "width": "90px",
            "offsetTop": "10px",
            "offsetStart": "205px",
            "paddingAll": "none",
            "action": {
              "type": "message",
              "label": "action",
              "text": "/BONUSTIME_EVO"
            }
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://lh3.googleusercontent.com/d/1lQMVAREptoNsJrcYjlchErZk6Ms_5DU9",
                "position": "absolute",
                "size": "85px"
              }
            ],
            "position": "absolute",
            "height": "90px",
            "width": "90px",
            "offsetTop": "105px",
            "offsetStart": "10px",
            "paddingAll": "none",
            "action": {
              "type": "message",
              "label": "action",
              "text": "/BONUSTIME_RTG"
            }
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://lh3.googleusercontent.com/d/1v838zeAjgJSnXQBida8nesDW4aILkq6C",
                "position": "absolute",
                "size": "85px"
              }
            ],
            "position": "absolute",
            "height": "90px",
            "width": "90px",
            "offsetTop": "105px",
            "offsetStart": "108px",
            "paddingAll": "none",
            "action": {
              "type": "message",
              "label": "action",
              "text": "/BONUSTIME_HBE"
            }
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://lh3.googleusercontent.com/d/14Qmb-CVIGhhaeDRAc1mfpe8eL9a08oPK",
                "position": "absolute",
                "size": "85px"
              }
            ],
            "position": "absolute",
            "height": "90px",
            "width": "90px",
            "offsetTop": "105px",
            "offsetStart": "205px",
            "paddingAll": "none",
            "action": {
              "type": "message",
              "label": "action",
              "text": "/BONUSTIME_FKG"
            }
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://lh3.googleusercontent.com/d/1MRZiQcaTifrO7hLq-H0Cjc4XDjME5_O2",
                "position": "absolute",
                "size": "85px"
              }
            ],
            "position": "absolute",
            "height": "90px",
            "width": "90px",
            "offsetTop": "200px",
            "offsetStart": "205px",
            "paddingAll": "none",
            "action": {
              "type": "message",
              "label": "action",
              "text": "/BONUSTIME_SMP"
            }
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://lh3.googleusercontent.com/d/16CGZ7yEFi59Z45T3Ost9rEv4rcFMC-Xw",
                "position": "absolute",
                "size": "85px"
              }
            ],
            "position": "absolute",
            "height": "90px",
            "width": "90px",
            "offsetTop": "200px",
            "offsetStart": "108px",
            "paddingAll": "none",
            "action": {
              "type": "message",
              "label": "action",
              "text": "/BONUSTIME_SXO"
            }
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://lh3.googleusercontent.com/d/1vt9rRkembOFCi8o_j98bLjVRfFgI9r16",
                "position": "absolute",
                "size": "85px"
              }
            ],
            "position": "absolute",
            "height": "90px",
            "width": "90px",
            "offsetTop": "200px",
            "offsetStart": "10px",
            "paddingAll": "none",
            "action": {
              "type": "message",
              "label": "action",
              "text": "/BONUSTIME_YGG"
            }
          }
        ],
        "paddingTop": "none",
        "paddingBottom": "none",
        "paddingStart": "none",
        "paddingEnd": "none",
        "height": "300px",
        "backgroundColor": "#545454",
        "maxWidth": "300px"
      },
      "styles": {
        "hero": {
          "backgroundColor": "#000000"
        }
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://lh3.googleusercontent.com/d/1-H6iM_bNdBdJKGN-abIgzA6TfLd9Txh0",
        "size": "full",
        "aspectRatio": "4:2.5",
        "aspectMode": "fit"
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
                "type": "image",
                "url": "https://lh3.googleusercontent.com/d/1c74jRK2j0GMCUwiaHa5gYSVwCi4Yu6bn",
                "position": "absolute",
                "size": "full",
                "aspectRatio": "3:4.2",
                "aspectMode": "cover",
                "animated": True,
                "offsetTop": "-50px"
              }
            ],
            "position": "absolute",
            "width": "300px",
            "height": "430px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://lh3.googleusercontent.com/d/1KLS6XFzdZtg4XoS32fXW3xg9WIX-LHuf",
                "position": "absolute",
                "size": "85px"
              }
            ],
            "paddingAll": "none",
            "action": {
              "type": "message",
              "label": "action",
              "text": "/BONUSTIME_AG"
            },
            "position": "absolute",
            "height": "90px",
            "offsetStart": "10px",
            "offsetTop": "10px",
            "width": "90px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://lh3.googleusercontent.com/d/1ZGAeh9y6udDYOopR256hOLW5oum_Sfgj",
                "position": "absolute",
                "size": "85px"
              }
            ],
            "position": "absolute",
            "height": "90px",
            "width": "90px",
            "offsetTop": "10px",
            "offsetStart": "108px",
            "paddingAll": "none",
            "action": {
              "type": "message",
              "label": "action",
              "text": "/BONUSTIME_SA"
            }
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://lh3.googleusercontent.com/d/1bz9XLGi6jBf774CgAz5y9YY6TmPg3woq",
                "position": "absolute",
                "size": "85px"
              }
            ],
            "position": "absolute",
            "height": "90px",
            "width": "90px",
            "offsetTop": "10px",
            "offsetStart": "205px",
            "paddingAll": "none",
            "action": {
              "type": "message",
              "label": "action",
              "text": "/BONUSTIME_AE"
            }
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://lh3.googleusercontent.com/d/13E1eqIiWPMWQ0DkIAbLxsmazPc-KG0AF",
                "position": "absolute",
                "size": "85px"
              }
            ],
            "position": "absolute",
            "height": "90px",
            "width": "90px",
            "offsetTop": "105px",
            "offsetStart": "10px",
            "paddingAll": "none",
            "action": {
              "type": "message",
              "label": "action",
              "text": "/BONUSTIME_WM"
            }
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://lh3.googleusercontent.com/d/1_LMerLx40Le94YfuHdg-1FHl8DinMFTs",
                "position": "absolute",
                "size": "85px"
              }
            ],
            "position": "absolute",
            "height": "90px",
            "width": "90px",
            "offsetTop": "105px",
            "offsetStart": "108px",
            "paddingAll": "none",
            "action": {
              "type": "message",
              "label": "action",
              "text": "/BONUSTIME_BG"
            }
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://lh3.googleusercontent.com/d/1Gp1gHerhAMK7rj8cxv3RcupRfE54YnR8",
                "position": "absolute",
                "size": "85px"
              }
            ],
            "position": "absolute",
            "height": "90px",
            "width": "90px",
            "offsetTop": "105px",
            "offsetStart": "205px",
            "paddingAll": "none",
            "action": {
              "type": "message",
              "label": "action",
              "text": "/BONUSTIME_AB"
            }
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://lh3.googleusercontent.com/d/1s3CBNB_Y3zd2qqmxu3XoZ7wtWUnyH10g",
                "position": "absolute",
                "size": "85px"
              }
            ],
            "position": "absolute",
            "height": "90px",
            "width": "90px",
            "offsetTop": "200px",
            "offsetStart": "205px",
            "paddingAll": "none",
            "action": {
              "type": "message",
              "label": "action",
              "text": "/BONUSTIME_mt"
            }
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://lh3.googleusercontent.com/d/1tBfKBYhkCkXjaRWTYeBNJjiXRxJNt9La",
                "position": "absolute",
                "size": "85px"
              }
            ],
            "position": "absolute",
            "height": "90px",
            "width": "90px",
            "offsetTop": "200px",
            "offsetStart": "108px",
            "paddingAll": "none",
            "action": {
              "type": "message",
              "label": "action",
              "text": "/BONUSTIME_WR"
            }
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://lh3.googleusercontent.com/d/1nCpr0Q5fQQ8BhPEn9N0TRU6c0CL_L0k4",
                "position": "absolute",
                "size": "85px"
              }
            ],
            "position": "absolute",
            "height": "90px",
            "width": "90px",
            "offsetTop": "200px",
            "offsetStart": "10px",
            "paddingAll": "none",
            "action": {
              "type": "message",
              "label": "action",
              "text": "/BONUSTIME_XPG"
            }
          }
        ],
        "paddingTop": "none",
        "paddingBottom": "none",
        "paddingStart": "none",
        "paddingEnd": "none",
        "height": "300px",
        "backgroundColor": "#545454",
        "maxWidth": "300px"
      },
      "styles": {
        "hero": {
          "backgroundColor": "#000000"
        }
      }
    }
  ]
}
    



        # เพิ่ม bubble ใน data
   
    # Save data to a JSON file
    with open('flex_message/BONUSTIME.json', 'w', encoding='utf-8') as json_file:
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

