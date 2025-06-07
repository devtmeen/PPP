import configparser

# อ่านค่าจากไฟล์ config.ini
config = configparser.ConfigParser()
config.read('config.ini')

# ดึงค่า Name_Web และ Game_List1 จาก config
Name_Web = config['Config']['Name_Web']
Game_List1 = int(config['Config']['Game_List1'])
Logo_Web = config['Config']['Logo_Web']
Logo_menu = config['Config']['Logo_menu']
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
                "layout": "vertical",
                "contents": [
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "image",
                        "url": "https://img5.pic.in.th/file/secure-sv1/fcac8f71acee2c813724974c73dcccb9.png",
                        "aspectMode": "cover",
                        "position": "relative",
                        "size": "full"
                      }
                    ],
                    "height": "40px"
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
                            "url": Logo_menu,
                            "size": "full",
                            "position": "absolute",
                            "aspectRatio": "80:30"
                          }
                        ],
                        "position": "relative"
                      },
                      {
                        "type": "image",
                        "url": "https://img2.pic.in.th/pic/register_button.gif",
                        "gravity": "center",
                        "size": "full",
                        "offsetStart": "-2px",
                        "action": {
                          "type": "uri",
                          "label": "action",
                          "uri": Link_Web
                        }
                      },
                      {
                        "type": "image",
                        "url": "https://img2.pic.in.th/pic/2login_button-joker89-1.gif",
                        "offsetEnd": "sm",
                        "gravity": "center",
                        "action": {
                          "type": "uri",
                          "label": "action",
                          "uri": Link_Web
                        }
                      }
                    ],
                    "position": "absolute",
                    "margin": "lg",
                    "width": "100%",
                    "height": "40px"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": []
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "image",
                            "url": "https://img5.pic.in.th/file/secure-sv1/430f0ddc181554f36f0f26017ee62653.png",
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
                            "url": "https://img2.pic.in.th/pic/30214ec4a8f02d206.png",
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
                            "url": "https://img2.pic.in.th/pic/269c57eb8373230ec.png",
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
                            "url": "https://img5.pic.in.th/file/secure-sv1/1ebd352e676411521.png",
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
                            "url": "https://img2.pic.in.th/pic/531cd1197449196dd.png",
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
                            "url": "https://img5.pic.in.th/file/secure-sv1/43c4dbc68e12917ba.png",
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
                            "url": "https://img5.pic.in.th/file/secure-sv1/6922d0165fb236ba0.png",
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
                            "url": "https://img5.pic.in.th/file/secure-sv1/955eb0e6e56ed2303.png",
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
                            "url": "https://img2.pic.in.th/pic/1138e74e1a54c836c3.png",
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
                            "url": "https://img2.pic.in.th/pic/2293131a7638f05890.png",
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
                    "maxWidth": "300px"
                  }
                ]
              }
            ]
          }
        ],
        "paddingTop": "none",
        "paddingBottom": "none",
        "paddingStart": "none",
        "paddingEnd": "none",
        "height": "340px",
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
                "layout": "vertical",
                "contents": [
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "image",
                        "url": "https://img5.pic.in.th/file/secure-sv1/fcac8f71acee2c813724974c73dcccb9.png",
                        "aspectMode": "cover",
                        "position": "relative",
                        "size": "full"
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
                                "url": Logo_menu,
                                "position": "absolute",
                                "size": "full",
                                "aspectRatio": "80:30"
                              }
                            ],
                            "paddingAll": "none",
                            "action": {
                              "type": "message",
                              "label": "action",
                              "text": "/BONUSTIME_PG"
                            },
                            "position": "relative"
                          },
                          {
                            "type": "image",
                            "url": "https://img2.pic.in.th/pic/register_button.gif",
                            "gravity": "center",
                            "offsetStart": "1px",
                            "size": "full",
                            "action": {
                              "type": "uri",
                              "label": "action",
                              "uri": Link_Web
                            }
                          },
                          {
                            "type": "image",
                            "url": "https://img2.pic.in.th/pic/2login_button-joker89-1.gif",
                            "offsetEnd": "xs",
                            "gravity": "center",
                            "action": {
                              "type": "uri",
                              "label": "action",
                              "uri": Link_Web
                            }
                          }
                        ],
                        "position": "absolute",
                        "width": "100%",
                        "height": "40px",
                        "margin": "lg"
                      }
                    ],
                    "position": "relative",
                    "height": "40px"
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
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                              {
                                "type": "image",
                                "url": "https://img5.pic.in.th/file/secure-sv1/430f0ddc181554f36f0f26017ee62653.png",
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
                                "url": "https://img2.pic.in.th/pic/AMBS.png",
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
                                "url": "https://img5.pic.in.th/file/secure-sv1/CQ92de0fb8d465e6c92.png",
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
                                "url": "https://img2.pic.in.th/pic/EVOb467d713274e870d.png",
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
                                "url": "https://img2.pic.in.th/pic/RTG.png",
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
                                "url": "https://img5.pic.in.th/file/secure-sv1/HBE.png",
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
                                "url": "https://img2.pic.in.th/pic/FKG.png",
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
                                "url": "https://img2.pic.in.th/pic/SMP.png",
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
                                "url": "https://img5.pic.in.th/file/secure-sv1/SXO.png",
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
                                "url": "https://img5.pic.in.th/file/secure-sv1/YGG.png",
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
                        "height": "340px",
                        "backgroundColor": "#545454",
                        "maxWidth": "300px"
                      }
                    ]
                  }
                ],
                "paddingTop": "none",
                "paddingBottom": "none",
                "paddingStart": "none",
                "paddingEnd": "none",
                "height": "340px",
                "backgroundColor": "#545454",
                "maxWidth": "300px"
              }
            ]
          }
        ],
        "paddingTop": "none",
        "paddingBottom": "none",
        "paddingStart": "none",
        "paddingEnd": "none",
        "height": "340px",
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
                "layout": "vertical",
                "contents": [
                  {
                    "type": "image",
                    "aspectMode": "cover",
                    "position": "relative",
                    "size": "full",
                    "url": "https://img5.pic.in.th/file/secure-sv1/fcac8f71acee2c813724974c73dcccb9.png"
                  }
                ],
                "height": "40px"
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
                        "url": Logo_menu,
                        "position": "absolute",
                        "size": "full",
                        "aspectRatio": "80:30"
                      }
                    ],
                    "paddingAll": "none",
                    "action": {
                      "type": "message",
                      "label": "action",
                      "text": "/BONUSTIME_PG"
                    },
                    "position": "relative",
                    "offsetStart": "10px"
                  },
                  {
                    "type": "image",
                    "url": "https://img2.pic.in.th/pic/register_button.gif",
                    "gravity": "center",
                    "offsetStart": "1px",
                    "size": "full",
                    "action": {
                      "type": "uri",
                      "label": "action",
                      "uri": Link_Web
                    }
                  },
                  {
                    "type": "image",
                    "url": "https://img2.pic.in.th/pic/2login_button-joker89-1.gif",
                    "offsetEnd": "xs",
                    "gravity": "center",
                    "action": {
                      "type": "uri",
                      "label": "action",
                      "uri": Link_Web
                    }
                  }
                ],
                "position": "absolute",
                "margin": "lg",
                "width": "100%",
                "height": "40px"
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
                        "type": "image",
                        "url": "https://img5.pic.in.th/file/secure-sv1/430f0ddc181554f36f0f26017ee62653.png",
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
                        "url": "https://img5.pic.in.th/file/secure-sv1/AG35121059b010475a.png",
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
                        "url": "https://img5.pic.in.th/file/secure-sv1/SA.png",
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
                        "url": "https://img5.pic.in.th/file/secure-sv1/AEa29b395b4ed47143.png",
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
                        "url": "https://img2.pic.in.th/pic/WMdf753f11ed0309fe.png",
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
                        "url": "https://img5.pic.in.th/file/secure-sv1/BG34640a292bf52ef3.png",
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
                        "url": "https://img2.pic.in.th/pic/AB.png",
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
                        "url": "https://img2.pic.in.th/pic/MTe9587668d665b0ca.png",
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
                      "text": "/BONUSTIME_MT"
                    }
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "image",
                        "url": "https://img2.pic.in.th/pic/WRcede205fedc25732.png",
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
                      "text": "/BONUSTIME_wr"
                    }
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "image",
                        "url": "https://img5.pic.in.th/file/secure-sv1/XPG.png",
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
              }
            ]
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