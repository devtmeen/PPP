import configparser
import json
import os
import random
import sys
from datetime import datetime
import time
from pathlib import Path
import logging

debug = 1

start_time = time.time()

def BONUSTIME_AG(api_folder):
    # ดึงเวลาปัจจุบัน
    now = datetime.now()

    # แปลงเวลาเป็นรูปแบบ "00:00"
    formatted_time = now.strftime("%H")
    # แปลงเวลาเป็น integer ก่อนที่จะบวก
    num = int(formatted_time) + 1

    # อ่านข้อมูลจากไฟล์ AG_casino.json
    with open(api_folder +'/AG_casino.json', 'r', encoding='utf-8') as json_file:
        AG_casino = json.load(json_file)

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
            percen_splin = 100-percentage
            message_percen_splin = f"{percen_splin:.2f}%"

            # ตรวจสอบเปอร์เซ็นต์ในทั้งหมดของ "BONUSTIME" และ bubbles
            if message_percen_splin not in used_percen_splins:
                used_percen_splins.add(message_percen_splin)
                return message_percen_splin
    
    # สร้างข้อความ message_percen และตรวจสอบเปอร์เซ็นต์ในเซ็ต
    def generate_unique_percentage_game():
        while True:
            percentage_game = random.randint(2, 12)
            percentage_game2 = random.randint(100, 999)
            message_percen_game = f"{percentage_game},{percentage_game2}"

            # ตรวจสอบเปอร์เซ็นต์ในเซ็ต
            if message_percen_game not in used_percen_game:
                used_percen_game.add(message_percen_game)
                return message_percen_game

    Bonustime_Update = formatted_time + ":00 - " + str(num) + ":00 น."
    # สร้าง JSON data
    for _ in range(4):
        game = random.choice(AG_casino)
        
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
                game = random.choice(AG_casino)

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
        "url": "https://lh3.googleusercontent.com/d/1-L3ePMsVuLky0mkXOgWYWD1O_FHA67TV",
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
                "url": "https://img2.pic.in.th/pic/AG.png",
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
                "url": "https://img2.pic.in.th/pic/logo-asiagaming.png",
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
          "startColor": "#02397d",
          "endColor": "#002047",
          "centerColor": "#00295c"
        }
      }
    }
  ]
}

    # สร้าง bubbles และเพิ่มลงใน data
    for _ in range(Game_List):
        game = random.choice(AG_casino)
        
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
                game = random.choice(AG_casino)

        message_percen = generate_unique_percentage()
        message_percen_splin = generate_unique_percen_splin()
        message_percen_game = generate_unique_percentage_game()

        bubble =    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://lh3.googleusercontent.com/d/1-L3ePMsVuLky0mkXOgWYWD1O_FHA67TV",
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
                "url": "https://img2.pic.in.th/pic/AG.png",
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
                "url": "https://img2.pic.in.th/pic/logo-asiagaming.png",
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
          "startColor": "#02397d",
          "endColor": "#002047",
          "centerColor": "#00295c"
        }
      }
    }
    

        # เพิ่ม bubble ใน data
        data["contents"].append(bubble)

    # Save data to a JSON file
    with open(api_folder + '/flex_message/BONUSTIME_AG.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)
    if debug:
      print(api_folder + '/flex_message/BONUSTIME_AG.json')

def BONUSTIME_CDG(api_folder):
    # ดึงเวลาปัจจุบัน
    now = datetime.now()

    # แปลงเวลาเป็นรูปแบบ "00:00"
    formatted_time = now.strftime("%H")
    # แปลงเวลาเป็น integer ก่อนที่จะบวก
    num = int(formatted_time) + 1

    # อ่านข้อมูลจากไฟล์ AG_casino.json
    with open(api_folder +'/CDG_casino.json', 'r', encoding='utf-8') as json_file:
        CDG_casino = json.load(json_file)

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
            percen_splin = 100-percentage
            message_percen_splin = f"{percen_splin:.2f}%"

            # ตรวจสอบเปอร์เซ็นต์ในทั้งหมดของ "BONUSTIME" และ bubbles
            if message_percen_splin not in used_percen_splins:
                used_percen_splins.add(message_percen_splin)
                return message_percen_splin
    
    # สร้างข้อความ message_percen และตรวจสอบเปอร์เซ็นต์ในเซ็ต
    def generate_unique_percentage_game():
        while True:
            percentage_game = random.randint(2, 12)
            percentage_game2 = random.randint(100, 999)
            message_percen_game = f"{percentage_game},{percentage_game2}"

            # ตรวจสอบเปอร์เซ็นต์ในเซ็ต
            if message_percen_game not in used_percen_game:
                used_percen_game.add(message_percen_game)
                return message_percen_game

    Bonustime_Update = formatted_time + ":00 - " + str(num) + ":00 น."
    # สร้าง JSON data
    for _ in range(Game_List):
        game = random.choice(CDG_casino)
        
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
                game = random.choice(CDG_casino)

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
        "url": "https://lh3.googleusercontent.com/d/1qwMT5nnuZplCyBElxr9f-907z8gECEAE",
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
                "url": "https://i.postimg.cc/g02WhfgG/WM-1662377333.png",
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
                "url": "https://img2.pic.in.th/pic/dreamgaming-logo1.webp",
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
          "startColor": "#321f01",
          "endColor": "#211404",
          "centerColor": "#321f01"
        }
      }
    }
  ]
}

    # สร้าง bubbles และเพิ่มลงใน data
    for _ in range(Game_List):
        game = random.choice(CDG_casino)
        
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
                game = random.choice(CDG_casino)

        message_percen = generate_unique_percentage()
        message_percen_splin = generate_unique_percen_splin()
        message_percen_game = generate_unique_percentage_game()

        bubble =    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://lh3.googleusercontent.com/d/1qwMT5nnuZplCyBElxr9f-907z8gECEAE",
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
                "url": "https://i.postimg.cc/g02WhfgG/WM-1662377333.png",
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
                "url": "https://img2.pic.in.th/pic/dreamgaming-logo1.webp",
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
          "startColor": "#321f01",
          "endColor": "#211404",
          "centerColor": "#321f01"
        }
      }
    }
    

        # เพิ่ม bubble ใน data
        data["contents"].append(bubble)

    # Save data to a JSON file
    with open(api_folder + '/flex_message/BONUSTIME_CDG.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)
    if debug:
      print(api_folder + '/flex_message/BONUSTIME_CDG.json')

def BONUSTIME_SA(api_folder):
    # ดึงเวลาปัจจุบัน
    now = datetime.now()

    # แปลงเวลาเป็นรูปแบบ "00:00"
    formatted_time = now.strftime("%H")
    # แปลงเวลาเป็น integer ก่อนที่จะบวก
    num = int(formatted_time) + 1

    # อ่านข้อมูลจากไฟล์ SA_casino.json
    with open(api_folder + '/SA_casino.json', 'r', encoding='utf-8') as json_file:
        SA_casino = json.load(json_file)

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
        game = random.choice(SA_casino)
        
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
                game = random.choice(SA_casino)

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
        "url": "https://lh3.googleusercontent.com/d/1rA_iUxYPgolcwNfK1dW5MzksloZors5Q",
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
                "url": "https://img2.pic.in.th/pic/SAba04d3047dc70ddd.png",
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
                "url": "https://sa-gaming.info/wp-content/uploads/2024/08/sagaming.png",
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
          "startColor": "#0c2212",
          "endColor": "#193e23",
          "centerColor": "#0e2514"
        }
      }
    }
  ]
}

    # สร้าง bubbles และเพิ่มลงใน data
    for _ in range(Game_List):
        game = random.choice(SA_casino)
        
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
                game = random.choice(SA_casino)

        message_percen = generate_unique_percentage()
        message_percen_splin = generate_unique_percen_splin()
        message_percen_game = generate_unique_percentage_game()

        bubble =    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://lh3.googleusercontent.com/d/1rA_iUxYPgolcwNfK1dW5MzksloZors5Q",
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
                "url": "https://img2.pic.in.th/pic/SAba04d3047dc70ddd.png",
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
                "url": "https://sa-gaming.info/wp-content/uploads/2024/08/sagaming.png",
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
          "startColor": "#0c2212",
          "endColor": "#193e23",
          "centerColor": "#0e2514"
        }
      }
    }
    

        

        


        # เพิ่ม bubble ใน data
        data["contents"].append(bubble)

    # Save data to a JSON file
    with open(api_folder + '/flex_message/BONUSTIME_SA.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)
    if debug:
      print(api_folder + '/flex_message/BONUSTIME_SA.json')

def BONUSTIME_AE(api_folder):
    # ดึงเวลาปัจจุบัน
    now = datetime.now()

    # แปลงเวลาเป็นรูปแบบ "00:00"
    formatted_time = now.strftime("%H")
    # แปลงเวลาเป็น integer ก่อนที่จะบวก
    num = int(formatted_time) + 1

    # อ่านข้อมูลจากไฟล์ AE_casino.json
    with open(api_folder + '/AE_casino.json', 'r', encoding='utf-8') as json_file:
        AE_casino = json.load(json_file)

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
        game = random.choice(AE_casino)
        
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
                game = random.choice(AE_casino)

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
        "url": "https://lh3.googleusercontent.com/d/1KTlKejYW2pv7g6dC2qF_ZKZqpDQARiqg",
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
                "url": "https://img5.pic.in.th/file/secure-sv1/a4d9a96fe0a40af63a363b71e4cec1b2.png",
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
                "url": "https://img5.pic.in.th/file/secure-sv1/ae-sexy-logo.webp",
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
            "startColor": "#670942",
            "endColor": "#7d1754",
            "centerColor": "#670942"
        }
      }
    }
  ]
}

    # สร้าง bubbles และเพิ่มลงใน data
    for _ in range(Game_List):
        game = random.choice(AE_casino)
        
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
                game = random.choice(AE_casino)

        message_percen = generate_unique_percentage()
        message_percen_splin = generate_unique_percen_splin()
        message_percen_game = generate_unique_percentage_game()

        bubble =    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://lh3.googleusercontent.com/d/1KTlKejYW2pv7g6dC2qF_ZKZqpDQARiqg",
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
                "url": "https://img5.pic.in.th/file/secure-sv1/a4d9a96fe0a40af63a363b71e4cec1b2.png",
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
                "url": "https://img5.pic.in.th/file/secure-sv1/ae-sexy-logo.webp",
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
            "startColor": "#670942",
            "endColor": "#7d1754",
            "centerColor": "#670942"
        }
      }
    }
    

        

        


        # เพิ่ม bubble ใน data
        data["contents"].append(bubble)

    # Save data to a JSON file
    with open(api_folder + '/flex_message/BONUSTIME_AE.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)
    if debug:
      print(api_folder + '/flex_message/BONUSTIME_AE.json')

def BONUSTIME_WM(api_folder):
    # ดึงเวลาปัจจุบัน
    now = datetime.now()

    # แปลงเวลาเป็นรูปแบบ "00:00"
    formatted_time = now.strftime("%H")
    # แปลงเวลาเป็น integer ก่อนที่จะบวก
    num = int(formatted_time) + 1

    # อ่านข้อมูลจากไฟล์ WM_casino.json
    with open(api_folder + '/WM_casino.json', 'r', encoding='utf-8') as json_file:
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
    with open(api_folder + '/flex_message/BONUSTIME_WM.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)
    if debug:
      print(api_folder + '/flex_message/BONUSTIME_WM.json')

def BONUSTIME_BG(api_folder):
    # ดึงเวลาปัจจุบัน
    now = datetime.now()

    # แปลงเวลาเป็นรูปแบบ "00:00"
    formatted_time = now.strftime("%H")
    # แปลงเวลาเป็น integer ก่อนที่จะบวก
    num = int(formatted_time) + 1

    # อ่านข้อมูลจากไฟล์ BG_casino.json
    with open(api_folder + '/BG_casino.json', 'r', encoding='utf-8') as json_file:
        BG_casino = json.load(json_file)

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
        game = random.choice(BG_casino)
        
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
                game = random.choice(BG_casino)

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
        "url": "https://lh3.googleusercontent.com/d/12yXRN2T03DK0qQi0vu8orJvXEtPL-J7r",
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
                "url": "https://img5.pic.in.th/file/secure-sv1/BGee65888f9d82a72a.png",
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
                "url": "https://img2.pic.in.th/pic/filters_no_upscale.webp",
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
          "startColor": "#2e154f",
          "endColor": "#5e278b",
          "centerColor": "#2e154f"
        }
      }
    }
  ]
}

    # สร้าง bubbles และเพิ่มลงใน data
    for _ in range(Game_List):
        game = random.choice(BG_casino)
        
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
                game = random.choice(BG_casino)

        message_percen = generate_unique_percentage()
        message_percen_splin = generate_unique_percen_splin()
        message_percen_game = generate_unique_percentage_game()

        bubble =    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://lh3.googleusercontent.com/d/12yXRN2T03DK0qQi0vu8orJvXEtPL-J7r",
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
                "url": "https://img5.pic.in.th/file/secure-sv1/BGee65888f9d82a72a.png",
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
                "url": "https://img2.pic.in.th/pic/filters_no_upscale.webp",
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
          "startColor": "#2e154f",
          "endColor": "#5e278b",
          "centerColor": "#2e154f"
        }
      }
    }
    

        

        


        # เพิ่ม bubble ใน data
        data["contents"].append(bubble)

    # Save data to a JSON file
    with open(api_folder + '/flex_message/BONUSTIME_BG.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)
    if debug:
      print(api_folder + '/flex_message/BONUSTIME_BG.json')
  
def BONUSTIME_AB(api_folder):
    # ดึงเวลาปัจจุบัน
    now = datetime.now()

    # แปลงเวลาเป็นรูปแบบ "00:00"
    formatted_time = now.strftime("%H")
    # แปลงเวลาเป็น integer ก่อนที่จะบวก
    num = int(formatted_time) + 1

    # อ่านข้อมูลจากไฟล์ AB_casino.json
    with open(api_folder + '/AB_casino.json', 'r', encoding='utf-8') as json_file:
        AB_casino = json.load(json_file)

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
        game = random.choice(AB_casino)
        
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
                game = random.choice(AB_casino)

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
        "url": "https://lh3.googleusercontent.com/d/1-YOsU7hQPpNzcn9TYTVnw0GbQl4rKLjZ",
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
                "url": "https://img5.pic.in.th/file/secure-sv1/AB.png",
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
                "url": "https://img2.pic.in.th/pic/the-online-casino-product-from-allbet-gamingsoft.png",
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
            "startColor": "#201713",
            "endColor": "#43291e",
            "centerColor": "#271b16"
        }
      }
    }
  ]
}

    # สร้าง bubbles และเพิ่มลงใน data
    for _ in range(Game_List):
        game = random.choice(AB_casino)
        
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
                game = random.choice(AB_casino)

        message_percen = generate_unique_percentage()
        message_percen_splin = generate_unique_percen_splin()
        message_percen_game = generate_unique_percentage_game()

        bubble =    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://lh3.googleusercontent.com/d/1-YOsU7hQPpNzcn9TYTVnw0GbQl4rKLjZ",
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
                "url": "https://img5.pic.in.th/file/secure-sv1/AB.png",
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
                "url": "https://img2.pic.in.th/pic/the-online-casino-product-from-allbet-gamingsoft.png",
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
            "startColor": "#201713",
            "endColor": "#43291e",
            "centerColor": "#271b16"
        }
      }
    }
    

        

        


        # เพิ่ม bubble ใน data
        data["contents"].append(bubble)

    # Save data to a JSON file
    with open(api_folder + '/flex_message/BONUSTIME_AB.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)
    if  debug:
      print(api_folder + '/flex_message/BONUSTIME_AB.json')
  
def BONUSTIME_XPG(api_folder):
    # ดึงเวลาปัจจุบัน
    now = datetime.now()

    # แปลงเวลาเป็นรูปแบบ "00:00"
    formatted_time = now.strftime("%H")
    # แปลงเวลาเป็น integer ก่อนที่จะบวก
    num = int(formatted_time) + 1

    # อ่านข้อมูลจากไฟล์ XPG_casino.json
    with open(api_folder + '/XPG_casino.json', 'r', encoding='utf-8') as json_file:
        XPG_casino = json.load(json_file)

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
        game = random.choice(XPG_casino)
        
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
                game = random.choice(XPG_casino)

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
        "url": "https://lh3.googleusercontent.com/d/1gdSE6FbqJJah5DTJ67lz1XIAJTTg9jEy",
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
                "url": "https://img2.pic.in.th/pic/XPG.png",
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
                "url": "https://img5.pic.in.th/file/secure-sv1/xpg.webp",
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
            "startColor": "#201713",
            "endColor": "#43291e",
            "centerColor": "#271b16"
        }
      }
    }
  ]
}

    # สร้าง bubbles และเพิ่มลงใน data
    for _ in range(Game_List):
        game = random.choice(XPG_casino)
        
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
                game = random.choice(XPG_casino)

        message_percen = generate_unique_percentage()
        message_percen_splin = generate_unique_percen_splin()
        message_percen_game = generate_unique_percentage_game()

        bubble =    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://lh3.googleusercontent.com/d/1gdSE6FbqJJah5DTJ67lz1XIAJTTg9jEy",
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
                "url": "https://img2.pic.in.th/pic/XPG.png",
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
                "url": "https://img5.pic.in.th/file/secure-sv1/xpg.webp",
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
            "startColor": "#201713",
            "endColor": "#43291e",
            "centerColor": "#271b16"
        }
      }
    }
    

        

        


        # เพิ่ม bubble ใน data
        data["contents"].append(bubble)

    # Save data to a JSON file
    with open(api_folder + '/flex_message/BONUSTIME_XPG.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)
    if  debug:
      print(api_folder + '/flex_message/BONUSTIME_XPG.json')
  
def BONUSTIME_WR(api_folder):
    # ดึงเวลาปัจจุบัน
    now = datetime.now()

    # แปลงเวลาเป็นรูปแบบ "00:00"
    formatted_time = now.strftime("%H")
    # แปลงเวลาเป็น integer ก่อนที่จะบวก
    num = int(formatted_time) + 1

    # อ่านข้อมูลจากไฟล์ WR_casino.json
    with open(api_folder + '/WR_casino.json', 'r', encoding='utf-8') as json_file:
        WR_casino = json.load(json_file)

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
        game = random.choice(WR_casino)
        
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
                game = random.choice(WR_casino)

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
        "url": "https://lh3.googleusercontent.com/d/1yLD5INc-T9IJECOOBw-5QKdE5wTJI7A4",
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
                "url": "https://img5.pic.in.th/file/secure-sv1/WR.png",
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
                "url": "https://img5.pic.in.th/file/secure-sv1/1695407357472cc6d.png",
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
            "startColor": "#0c142a",
            "endColor": "#172240",
            "centerColor": "#0c142a"
        }
      }
    }
  ]
}

    # สร้าง bubbles และเพิ่มลงใน data
    for _ in range(Game_List):
        game = random.choice(WR_casino)
        
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
                game = random.choice(WR_casino)

        message_percen = generate_unique_percentage()
        message_percen_splin = generate_unique_percen_splin()
        message_percen_game = generate_unique_percentage_game()

        bubble =    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://lh3.googleusercontent.com/d/1yLD5INc-T9IJECOOBw-5QKdE5wTJI7A4",
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
                "url": "https://img5.pic.in.th/file/secure-sv1/WR.png",
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
                "url": "https://img5.pic.in.th/file/secure-sv1/1695407357472cc6d.png",
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
            "startColor": "#0c142a",
            "endColor": "#172240",
            "centerColor": "#0c142a"
        }
      }
    }
    
        # เพิ่ม bubble ใน data
        data["contents"].append(bubble)

    # Save data to a JSON file
    with open(api_folder + '/flex_message/BONUSTIME_WR.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)
    if debug:
      print(api_folder + '/flex_message/BONUSTIME_WR.json')

def BONUSTIME_MT(api_folder):
    # ดึงเวลาปัจจุบัน
    now = datetime.now()

    # แปลงเวลาเป็นรูปแบบ "00:00"
    formatted_time = now.strftime("%H")
    # แปลงเวลาเป็น integer ก่อนที่จะบวก
    num = int(formatted_time) + 1

    # อ่านข้อมูลจากไฟล์ MT_casino.json
    with open(api_folder + '/MT_casino.json', 'r', encoding='utf-8') as json_file:
        MT_casino = json.load(json_file)

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
        game = random.choice(MT_casino)
        
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
                game = random.choice(MT_casino)

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
        "url": "https://lh3.googleusercontent.com/d/1AMAv0CIWpZHx1eHz4fZQ-bHTo5tOfNkK",
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
                "url": "https://img2.pic.in.th/pic/MT234cdcdc82f2311f.png",
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
                "url": "https://img5.pic.in.th/file/secure-sv1/mt_logo_thumb_152_54.png",
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
          "startColor": "#561504",
          "endColor": "#6d1c08",
          "centerColor": "#561504"
        }
      }
    }
  ]
}

    # สร้าง bubbles และเพิ่มลงใน data
    for _ in range(Game_List):
        game = random.choice(MT_casino)
        
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
                game = random.choice(MT_casino)

        message_percen = generate_unique_percentage()
        message_percen_splin = generate_unique_percen_splin()
        message_percen_game = generate_unique_percentage_game()

        bubble =    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://lh3.googleusercontent.com/d/1AMAv0CIWpZHx1eHz4fZQ-bHTo5tOfNkK",
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
                "url": "https://img2.pic.in.th/pic/MT234cdcdc82f2311f.png",
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
                "url": "https://img5.pic.in.th/file/secure-sv1/mt_logo_thumb_152_54.png",
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
          "startColor": "#561504",
          "endColor": "#6d1c08",
          "centerColor": "#561504"
        }
      }
    }
    

        

        


        # เพิ่ม bubble ใน data
        data["contents"].append(bubble)

    # Save data to a JSON file
    with open(api_folder + '/flex_message/BONUSTIME_MT.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)
    if debug:
      print(api_folder + '/flex_message/BONUSTIME_MT.json')

configDefault = configparser.ConfigParser()
configDefault.read(['config.ini'])
patch = os.getenv("PATCH_DIR", configDefault.get("Config", "patch"))
folder_list = json.loads(configDefault.get("Config", "folder_list"))

logging.basicConfig(level=logging.INFO)

for folder in folder_list:
    folder_path = Path(patch) / folder
    if not folder_path.is_dir():
        logging.warning("Folder %s does not exist, skipping", folder_path)
        continue

    config = configparser.ConfigParser()
    config.read(folder_path / 'config.ini')
    if not config.has_section('Config'):
        logging.warning("Config section missing in %s", folder_path / 'config.ini')
        continue

    Name_Web = config['Config']['Name_Web']
    Game_List = int(config['Config']['Game_List'])
    Logo_Web = config['Config']['Logo_Web']
    Logo_menu = config['Config']['Logo_menu']
    Link_Web = config['Config']['Link_Web']
    port = config['Config']['port']

    folder_str = str(folder_path)

    print(folder + " | " + Name_Web + " | " + port)
    try:
      BONUSTIME_AG(folder_str)
      BONUSTIME_SA(folder_str)
      BONUSTIME_CDG(folder_str)
      BONUSTIME_AE(folder_str)
      BONUSTIME_WM(folder_str)
      BONUSTIME_BG(folder_str)
      BONUSTIME_AB(folder_str)
      BONUSTIME_XPG(folder_str)
      BONUSTIME_WR(folder_str)
      BONUSTIME_MT(folder_str)
    except Exception as e:
        logging.exception("Error processing %s", folder_str)
        continue
    if debug:
        print("\n")
    time.sleep(0.4)
print("--- %s seconds ---" % (time.time() - start_time))