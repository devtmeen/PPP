import configparser
import json
import os
import random
import sys
from datetime import datetime
from time import sleep

debug = 1

def LotteryGuide(api_folder):
  data = {
  "type": "bubble",
  "size": "mega",
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
                "url": "https://img5.pic.in.th/file/secure-sv1/fcac8f71acee2c813724974c73dcccb9.png",
                "size": "full",
                "aspectMode": "cover"
              }
            ],
            "height": "45px"
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
                    "align": "end",
                    "size": "md",
                    "aspectRatio": "80:30",
                    "gravity": "center",
                    "offsetStart": "3px"
                  }
                ],
                "position": "relative",
                "paddingAll": "5px"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "image",
                    "url": "https://img2.pic.in.th/pic/register_button.gif",
                    "action": {
                      "type": "uri",
                      "label": "action",
                      "uri": Link_Web
                    },
                    "gravity": "center",
                    "offsetTop": "-25px",
                    "offsetStart": "-3px"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "image",
                    "url": "https://img2.pic.in.th/pic/2login_button-joker89-1.gif",
                    "gravity": "center",
                    "action": {
                      "type": "uri",
                      "label": "action",
                      "uri": "https://www.google.com/"
                    },
                    "offsetTop": "-25px",
                    "offsetStart": "-3px"
                  }
                ]
              }
            ],
            "position": "absolute",
            "margin": "lg",
            "width": "100%",
            "height": "40px"
          }
        ]
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
                "aspectMode": "cover",
                "aspectRatio": "4:9",
                "animated": True,
                "offsetTop": "-50px"
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
                        "url": "https://i.postimg.cc/xT06g6Pt/LOTTO-7.png",
                        "size": "full",
                        "action": {
                          "type": "message",
                          "label": "action",
                          "text": "/THAILOTTOS"
                        },
                        "aspectMode": "cover"
                      },
                      {
                        "type": "image",
                        "url": "https://i.postimg.cc/YqbbPQnk/LOTTO-8.png",
                        "size": "full",
                        "aspectMode": "cover",
                        "action": {
                          "type": "message",
                          "label": "action",
                          "text": "/YEEKEELOTTOS"
                        }
                      },
                      {
                        "type": "image",
                        "url": "https://i.postimg.cc/wBSWVHWm/LOTTO-2.png",
                        "size": "full",
                        "aspectMode": "cover",
                        "action": {
                          "type": "message",
                          "label": "action",
                          "text": "/HANOISPECIALLOTTOS"
                        }
                      }
                    ],
                    "width": "90px",
                    "offsetStart": "5px",
                    "paddingTop": "5px"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "image",
                        "url": "https://i.postimg.cc/Y0xbMFt6/LOTTO-5.png",
                        "size": "full",
                        "aspectMode": "cover",
                        "action": {
                          "type": "message",
                          "label": "action",
                          "text": "/GSBLOTTOS"
                        }
                      },
                      {
                        "type": "image",
                        "url": "https://i.postimg.cc/RFKgp88b/LOTTO-4.png",
                        "size": "full",
                        "aspectMode": "cover",
                        "action": {
                          "type": "message",
                          "label": "action",
                          "text": "/HANOILOTTOS"
                        }
                      },
                      {
                        "type": "image",
                        "url": "https://i.postimg.cc/mgppP7CV/LOTTO-1.png",
                        "size": "full",
                        "aspectMode": "cover",
                        "action": {
                          "type": "message",
                          "label": "action",
                          "text": "/HANOIVIPLOTTOS"
                        }
                      }
                    ],
                    "width": "90px",
                    "paddingTop": "5px",
                    "offsetStart": "15px"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "image",
                        "url": "https://i.postimg.cc/mZ3dQv7P/LOTTO-6.png",
                        "size": "full",
                        "aspectMode": "cover",
                        "action": {
                          "type": "message",
                          "label": "action",
                          "text": "/LAOLOTTOS"
                        }
                      },
                      {
                        "type": "image",
                        "url": "https://i.postimg.cc/ZnmVGHzY/LOTTO-3.png",
                        "size": "full",
                        "aspectMode": "cover",
                        "action": {
                          "type": "message",
                          "label": "action",
                          "text": "/HANOINORMALLOTTOS"
                        }
                      }
                    ],
                    "width": "90px",
                    "paddingTop": "5px",
                    "offsetStart": "25px"
                  }
                ],
                "width": "350px",
                "height": "300px"
              }
            ],
            "position": "absolute",
            "height": "350px",
            "width": "100%"
          }
        ],
        "alignItems": "flex-start",
        "offsetTop": "none",
        "paddingAll": "none",
        "paddingTop": "none",
        "paddingBottom": "none",
        "paddingStart": "none",
        "paddingEnd": "none",
        "height": "280px"
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
                "aspectRatio": "4:9",
                "aspectMode": "cover",
                "offsetTop": "-50px"
              }
            ],
            "width": "100%",
            "height": "200px",
            "position": "absolute"
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
                    "url": "https://i.postimg.cc/JhPQBrRv/image.png",
                    "size": "full",
                    "aspectRatio": "1282:160",
                    "aspectMode": "cover"
                  }
                ],
                "offsetStart": "none",
                "action": {
                  "type": "message",
                  "label": "action",
                  "text": "/LOTTO"
                }
              }
            ],
            "margin": "sm"
          }
        ],
        "height": "100px"
      }
    ],
    "height": "370px",
    "paddingTop": "none",
    "paddingBottom": "none",
    "paddingStart": "none",
    "paddingEnd": "none"
  }
}
  with open(api_folder + '/flex_message/แนวทางหวย.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)
  if debug:
      print(api_folder + '/flex_message/แนวทางหวย.json')

def LOTTO(api_folder):
    # ดึงเวลาปัจจุบัน
    now = datetime.now()

    # แปลงเวลาเป็นรูปแบบ "00:00"
    formatted_time = now.strftime("%H")
    # แปลงเวลาเป็น integer ก่อนที่จะบวก
    num = int(formatted_time) + 1

    # อ่านข้อมูลจากไฟล์ PP_Game.json
    with open(api_folder + '/PP_Game.json', 'r', encoding='utf-8') as json_file:
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
    data = {
  "type": "bubble",
  "size": "mega",
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
                "url": "https://img5.pic.in.th/file/secure-sv1/fcac8f71acee2c813724974c73dcccb9.png",
                "size": "full",
                "aspectMode": "cover"
              }
            ],
            "height": "45px"
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
                    "align": "end",
                    "size": "md",
                    "aspectRatio": "80:30",
                    "gravity": "center",
                    "offsetStart": "3px"
                  }
                ],
                "position": "relative",
                "paddingAll": "5px"
              },
              {
                "type": "image",
                "url": "https://img2.pic.in.th/pic/register_button.gif",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": Link_Web
                },
                "gravity": "center",
                "offsetEnd": "5px",
                "offsetTop": "2px"
              },
              {
                "type": "image",
                "url": "https://img2.pic.in.th/pic/2login_button-joker89-1.gif",
                "gravity": "center",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": Link_Web
                },
                "offsetTop": "2px",
                "offsetEnd": "2px"
              }
            ],
            "position": "absolute",
            "margin": "lg",
            "width": "100%",
            "height": "40px"
          }
        ]
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
                "aspectMode": "cover",
                "aspectRatio": "4:9",
                "animated": True,
                "offsetTop": "-50px"
              }
            ],
            "position": "absolute",
            "height": "200px",
            "width": "100%"
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
                    "url": "https://i.postimg.cc/xT06g6Pt/LOTTO-7.png",
                    "size": "full",
                    "aspectMode": "cover"
                  }
                ],
                "width": "90px",
                "paddingTop": "5px",
                "position": "relative",
                "offsetStart": "5px",
                "action": {
                  "type": "message",
                  "label": "action",
                  "text": "/หวยรัฐบาล"
                }
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "image",
                    "url": "https://i.postimg.cc/mZ3dQv7P/LOTTO-6.png",
                    "size": "full",
                    "aspectMode": "cover"
                  }
                ],
                "width": "90px",
                "paddingTop": "5px",
                "position": "relative",
                "offsetStart": "15px",
                "action": {
                  "type": "message",
                  "label": "action",
                  "text": "/หวยลาว"
                }
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "image",
                    "url": "https://i.postimg.cc/RFKgp88b/LOTTO-4.png",
                    "size": "full",
                    "aspectMode": "cover"
                  }
                ],
                "width": "90px",
                "position": "relative",
                "paddingTop": "5px",
                "offsetStart": "25px",
                "action": {
                  "type": "message",
                  "label": "action",
                  "text": "/หวยฮานอย"
                }
              }
            ],
            "position": "relative",
            "width": "350px",
            "height": "200px"
          }
        ],
        "alignItems": "flex-start",
        "offsetTop": "none",
        "paddingAll": "none",
        "paddingTop": "none",
        "paddingBottom": "none",
        "paddingStart": "none",
        "paddingEnd": "none",
        "height": "100px"
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
                "aspectMode": "cover",
                "aspectRatio": "4:9",
                "animated": True,
                "offsetTop": "-50px"
              }
            ],
            "position": "absolute",
            "height": "200px",
            "width": "100%"
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
                    "url": "https://i.postimg.cc/Qtyf98jS/image.png",
                    "size": "full",
                    "aspectMode": "cover",
                    "aspectRatio": "1282:160"
                  }
                ],
                "paddingTop": "none",
                "position": "relative",
                "offsetStart": "none",
                "action": {
                  "type": "message",
                  "label": "action",
                  "text": "/แนวทางหวย"
                }
              }
            ],
            "position": "relative",
            "margin": "sm"
          }
        ],
        "alignItems": "flex-start",
        "offsetTop": "none",
        "paddingAll": "none",
        "paddingTop": "none",
        "paddingBottom": "none",
        "paddingStart": "none",
        "paddingEnd": "none",
        "height": "100px"
      }
    ],
    "height": "200px",
    "paddingTop": "none",
    "paddingBottom": "none",
    "paddingStart": "none",
    "paddingEnd": "none"
  }
}

    data = {
  "type": "bubble",
  "size": "mega",
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
                "url": "https://img5.pic.in.th/file/secure-sv1/fcac8f71acee2c813724974c73dcccb9.png",
                "size": "full",
                "aspectMode": "cover"
              }
            ],
            "height": "45px"
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
                    "align": "end",
                    "size": "md",
                    "aspectRatio": "80:30",
                    "gravity": "center",
                    "offsetStart": "3px"
                  }
                ],
                "position": "relative",
                "paddingAll": "5px"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "image",
                    "url": "https://img2.pic.in.th/pic/register_button.gif",
                    "action": {
                      "type": "uri",
                      "label": "action",
                      "uri": Link_Web
                    },
                    "gravity": "center",
                    "offsetTop": "-25px",
                    "offsetStart": "-3px"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "image",
                    "url": "https://img2.pic.in.th/pic/2login_button-joker89-1.gif",
                    "gravity": "center",
                    "action": {
                      "type": "uri",
                      "label": "action",
                      "uri": Link_Web
                    },
                    "offsetTop": "-25px",
                    "offsetStart": "-3px"
                  }
                ]
              }
            ],
            "position": "absolute",
            "margin": "lg",
            "width": "100%",
            "height": "40px"
          }
        ]
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
                "aspectMode": "cover",
                "aspectRatio": "4:9",
                "animated": True,
                "offsetTop": "-50px"
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
                        "url": "https://i.postimg.cc/xT06g6Pt/LOTTO-7.png",
                        "size": "full",
                        "action": {
                          "type": "message",
                          "label": "action",
                          "text": "/หวยรัฐบาล"
                        },
                        "aspectMode": "cover"
                      },
                      {
                        "type": "image",
                        "url": "https://i.postimg.cc/mZ3dQv7P/LOTTO-6.png",
                        "size": "full",
                        "aspectMode": "cover",
                        "action": {
                          "type": "message",
                          "label": "action",
                          "text": "/หวยลาว"
                        }
                      }
                    ],
                    "width": "90px",
                    "offsetStart": "5px",
                    "paddingTop": "5px"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "image",
                        "url": "https://i.postimg.cc/Y0xbMFt6/LOTTO-5.png",
                        "size": "full",
                        "aspectMode": "cover",
                        "action": {
                          "type": "message",
                          "label": "action",
                          "text": "/หวยออมสิน"
                        }
                      },
                      {
                        "type": "image",
                        "url": "https://i.postimg.cc/RFKgp88b/LOTTO-4.png",
                        "size": "full",
                        "aspectMode": "cover",
                        "action": {
                          "type": "message",
                          "label": "action",
                          "text": "/หวยฮานอย"
                        }
                      }
                    ],
                    "width": "90px",
                    "paddingTop": "5px",
                    "offsetStart": "15px"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "image",
                        "url": "https://i.postimg.cc/gcHBgdTN/12.png",
                        "size": "full",
                        "aspectMode": "cover",
                        "action": {
                          "type": "message",
                          "label": "action",
                          "text": "/หวยธกส"
                        }
                      },
                      {
                        "type": "image",
                        "url": "https://i.postimg.cc/ZnH7nFd1/11.png",
                        "size": "full",
                        "aspectMode": "cover",
                        "action": {
                          "type": "message",
                          "label": "action",
                          "text": "/หวยหุ้น"
                        }
                      }
                    ],
                    "width": "90px",
                    "paddingTop": "5px",
                    "offsetStart": "25px"
                  }
                ],
                "width": "350px",
                "height": "300px"
              }
            ],
            "position": "absolute",
            "height": "350px",
            "width": "100%"
          }
        ],
        "alignItems": "flex-start",
        "offsetTop": "none",
        "paddingAll": "none",
        "paddingTop": "none",
        "paddingBottom": "none",
        "paddingStart": "none",
        "paddingEnd": "none",
        "height": "190px"
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
                "aspectRatio": "4:9",
                "aspectMode": "cover",
                "offsetTop": "-50px"
              }
            ],
            "width": "100%",
            "height": "200px",
            "position": "absolute"
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
                    "url": "https://i.postimg.cc/Qtyf98jS/image.png",
                    "size": "full",
                    "aspectRatio": "1282:160",
                    "aspectMode": "cover"
                  }
                ],
                "offsetStart": "none",
                "action": {
                  "type": "message",
                  "label": "action",
                  "text": "/แนวทางหวย"
                }
              }
            ],
            "margin": "sm"
          }
        ],
        "height": "100px"
      }
    ],
    "height": "280px",
    "paddingTop": "none",
    "paddingBottom": "none",
    "paddingStart": "none",
    "paddingEnd": "none"
  }
}
    with open(api_folder + '/flex_message/LOTTO.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)
    if debug:
        print(api_folder + '/flex_message/LOTTO.json')

def BONUSTIME(api_folder):
    # ดึงเวลาปัจจุบัน
    now = datetime.now()

    # แปลงเวลาเป็นรูปแบบ "00:00"
    formatted_time = now.strftime("%H")
    # แปลงเวลาเป็น integer ก่อนที่จะบวก
    num = int(formatted_time) + 1

    # อ่านข้อมูลจากไฟล์ PP_Game.json
    with open(api_folder + '/PP_Game.json', 'r', encoding='utf-8') as json_file:
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
    data = {
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
                            "aspectMode": "cover",
                            "animated": True,
                            "offsetTop": "-50px",
                            "aspectRatio": "3:9"
                          }
                        ],
                        "position": "absolute",
                        "width": "300px",
                        "height": "500px"
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
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "image",
                            "url": "https://i.postimg.cc/RCc8X9fz/HK.png",
                            "position": "absolute",
                            "size": "85px"
                          }
                        ],
                        "position": "absolute",
                        "height": "90px",
                        "width": "90px",
                        "offsetTop": "295px",
                        "offsetStart": "108px",
                        "paddingAll": "none",
                        "action": {
                          "type": "message",
                          "label": "action",
                          "text": "/BONUSTIME_HK"
                        }
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "image",
                            "url": "https://i.postimg.cc/gjP7mtC5/DG.png",
                            "position": "absolute",
                            "size": "85px"
                          }
                        ],
                        "position": "absolute",
                        "height": "90px",
                        "width": "90px",
                        "offsetTop": "295px",
                        "offsetStart": "10px",
                        "paddingAll": "none",
                        "action": {
                          "type": "message",
                          "label": "action",
                          "text": "/BONUSTIME_DGG"
                        }
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "image",
                            "url": "https://i.postimg.cc/BbcV6csv/GO.png",
                            "position": "absolute",
                            "size": "85px"
                          }
                        ],
                        "position": "absolute",
                        "height": "90px",
                        "width": "90px",
                        "offsetTop": "295px",
                        "offsetStart": "205px",
                        "paddingAll": "none",
                        "action": {
                          "type": "message",
                          "label": "action",
                          "text": "/BONUSTIME_GO"
                        }
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "image",
                            "url": "https://i.postimg.cc/BnvVSKzq/SR.png",
                            "position": "absolute",
                            "size": "85px"
                          }
                        ],
                        "position": "absolute",
                        "height": "90px",
                        "width": "90px",
                        "offsetTop": "390px",
                        "offsetStart": "108px",
                        "paddingAll": "none",
                        "action": {
                          "type": "message",
                          "label": "action",
                          "text": "/BONUSTIME_RY"
                        }
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "image",
                            "url": "https://i.postimg.cc/J4xFCqP6/OP.png",
                            "position": "absolute",
                            "size": "85px"
                          }
                        ],
                        "position": "absolute",
                        "height": "90px",
                        "width": "90px",
                        "offsetTop": "390px",
                        "offsetStart": "10px",
                        "paddingAll": "none",
                        "action": {
                          "type": "message",
                          "label": "action",
                          "text": "/BONUSTIME_OP"
                        }
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "image",
                            "url": "https://i.postimg.cc/PrT77czv/R88.png",
                            "position": "absolute",
                            "size": "85px"
                          }
                        ],
                        "position": "absolute",
                        "height": "90px",
                        "width": "90px",
                        "offsetTop": "390px",
                        "offsetStart": "205px",
                        "paddingAll": "none",
                        "action": {
                          "type": "message",
                          "label": "action",
                          "text": "/BONUSTIME_R88"
                        }
                      }
                    ],
                    "paddingTop": "none",
                    "paddingBottom": "none",
                    "paddingStart": "none",
                    "paddingEnd": "none",
                    "height": "500px",
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
        "height": "540px",
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
                                "aspectRatio": "3:6",
                                "aspectMode": "cover",
                                "animated": True,
                                "offsetTop": "-50px"
                              }
                            ],
                            "position": "absolute",
                            "width": "300px",
                            "height": "530px"
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
                          },
                          {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                              {
                                "type": "image",
                                "url": "https://i.postimg.cc/MKchV4wC/ambg.png",
                                "position": "absolute",
                                "size": "85px"
                              }
                            ],
                            "position": "absolute",
                            "height": "90px",
                            "width": "90px",
                            "offsetTop": "295px",
                            "offsetStart": "108px",
                            "paddingAll": "none",
                            "action": {
                              "type": "message",
                              "label": "action",
                              "text": "/BONUSTIME_AMBG"
                            }
                          },
                          {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                              {
                                "type": "image",
                                "url": "https://i.postimg.cc/nc6NkkcC/amp.png",
                                "position": "absolute",
                                "size": "85px"
                              }
                            ],
                            "position": "absolute",
                            "height": "90px",
                            "width": "90px",
                            "offsetTop": "295px",
                            "offsetStart": "10px",
                            "paddingAll": "none",
                            "action": {
                              "type": "message",
                              "label": "action",
                              "text": "/BONUSTIME_AMP"
                            }
                          },
                          {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                              {
                                "type": "image",
                                "url": "https://i.postimg.cc/25YMpSWY/NS.png",
                                "position": "absolute",
                                "size": "85px"
                              }
                            ],
                            "position": "absolute",
                            "height": "90px",
                            "width": "90px",
                            "offsetTop": "295px",
                            "offsetStart": "205px",
                            "paddingAll": "none",
                            "action": {
                              "type": "message",
                              "label": "action",
                              "text": "/BONUSTIME_NS"
                            }
                          },
                          {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                              {
                                "type": "image",
                                "url": "https://i.postimg.cc/DzcD73QX/K9.png",
                                "position": "absolute",
                                "size": "85px"
                              }
                            ],
                            "position": "absolute",
                            "height": "90px",
                            "width": "90px",
                            "offsetTop": "390px",
                            "offsetStart": "108px",
                            "paddingAll": "none",
                            "action": {
                              "type": "message",
                              "label": "action",
                              "text": "/BONUSTIME_K9"
                            }
                          },
                          {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                              {
                                "type": "image",
                                "url": "https://i.postimg.cc/y8ctrZkn/KAGM.png",
                                "position": "absolute",
                                "size": "85px"
                              }
                            ],
                            "position": "absolute",
                            "height": "90px",
                            "width": "90px",
                            "offsetTop": "390px",
                            "offsetStart": "10px",
                            "paddingAll": "none",
                            "action": {
                              "type": "message",
                              "label": "action",
                              "text": "/BONUSTIME_KAGM"
                            }
                          },
                          {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                              {
                                "type": "image",
                                "url": "https://i.postimg.cc/Y9qP9D8y/SPG.png",
                                "position": "absolute",
                                "size": "85px"
                              }
                            ],
                            "position": "absolute",
                            "height": "90px",
                            "width": "90px",
                            "offsetTop": "390px",
                            "offsetStart": "205px",
                            "paddingAll": "none",
                            "action": {
                              "type": "message",
                              "label": "action",
                              "text": "/BONUSTIME_SPG"
                            }
                          }
                        ],
                        "paddingTop": "none",
                        "paddingBottom": "none",
                        "paddingStart": "none",
                        "paddingEnd": "none",
                        "height": "500px",
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
                "height": "540px",
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
                                "aspectRatio": "3:6",
                                "aspectMode": "cover",
                                "animated": True,
                                "offsetTop": "-50px"
                              }
                            ],
                            "position": "absolute",
                            "width": "300px",
                            "height": "530px"
                          },
                          {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                              {
                                "type": "image",
                                "url": "https://i.postimg.cc/SNqVHWrh/5G.png",
                                "position": "absolute",
                                "size": "85px"
                              }
                            ],
                            "paddingAll": "none",
                            "action": {
                              "type": "message",
                              "label": "action",
                              "text": "/BONUSTIME_G5"
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
                                "url": "https://i.postimg.cc/t44k4pwv/ACE333.png",
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
                              "text": "/BONUSTIME_ACE333"
                            }
                          },
                          {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                              {
                                "type": "image",
                                "url": "https://i.postimg.cc/25P7Gv6g/ADP.png",
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
                              "text": "/BONUSTIME_ADP"
                            }
                          },
                          {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                              {
                                "type": "image",
                                "url": "https://i.postimg.cc/DwpgWRKv/BTG.png",
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
                              "text": "/BONUSTIME_BTG"
                            }
                          },
                          {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                              {
                                "type": "image",
                                "url": "https://i.postimg.cc/MGcY1tWy/EXPS.png",
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
                              "text": "/BONUSTIME_EXPS"
                            }
                          },
                          {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                              {
                                "type": "image",
                                "url": "https://i.postimg.cc/Qt1kytKC/GDY.png",
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
                              "text": "/BONUSTIME_GDY"
                            }
                          },
                          {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                              {
                                "type": "image",
                                "url": "https://i.postimg.cc/yxTh7bPz/MNP.png",
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
                              "text": "/BONUSTIME_MNP"
                            }
                          },
                          {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                              {
                                "type": "image",
                                "url": "https://i.postimg.cc/ZYPxPWhD/ODG.png",
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
                              "text": "/BONUSTIME_ODG"
                            }
                          },
                          {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                              {
                                "type": "image",
                                "url": "https://i.postimg.cc/m2bNmTLZ/SW.png",
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
                              "text": "/BONUSTIME_SW"
                            }
                          },
                          {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                              {
                                "type": "image",
                                "url": "https://i.postimg.cc/L6Nk7G5t/WMS.png1",
                                "position": "absolute",
                                "size": "85px"
                              }
                            ],
                            "position": "absolute",
                            "height": "90px",
                            "width": "90px",
                            "offsetTop": "295px",
                            "offsetStart": "108px",
                            "paddingAll": "none",
                            "action": {
                              "type": "message",
                              "label": "action",
                              "text": "/BONUSTIME_WMS"
                            }
                          },
                          {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                              {
                                "type": "image",
                                "url": "https://i.postimg.cc/Qt8GtM9z/BPS.png",
                                "position": "absolute",
                                "size": "85px"
                              }
                            ],
                            "position": "absolute",
                            "height": "90px",
                            "width": "90px",
                            "offsetTop": "295px",
                            "offsetStart": "10px",
                            "paddingAll": "none",
                            "action": {
                              "type": "message",
                              "label": "action",
                              "text": "/BONUSTIME_BPS"
                            }
                          },
                          {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                              {
                                "type": "image",
                                "url": "https://i.postimg.cc/FKgXNSRc/EDPN.png",
                                "position": "absolute",
                                "size": "85px"
                              }
                            ],
                            "position": "absolute",
                            "height": "90px",
                            "width": "90px",
                            "offsetTop": "295px",
                            "offsetStart": "205px",
                            "paddingAll": "none",
                            "action": {
                              "type": "message",
                              "label": "action",
                              "text": "/BONUSTIME_EDPN"
                            }
                          },
                          {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                              {
                                "type": "image",
                                "url": "https://i.postimg.cc/mrGWvjbB/I8.png",
                                "position": "absolute",
                                "size": "85px"
                              }
                            ],
                            "position": "absolute",
                            "height": "90px",
                            "width": "90px",
                            "offsetTop": "390px",
                            "offsetStart": "108px",
                            "paddingAll": "none",
                            "action": {
                              "type": "message",
                              "label": "action",
                              "text": "/BONUSTIME_I8"
                            }
                          },
                          {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                              {
                                "type": "image",
                                "url": "https://i.postimg.cc/Cx8VrXpc/SBOS.png",
                                "position": "absolute",
                                "size": "85px"
                              }
                            ],
                            "position": "absolute",
                            "height": "90px",
                            "width": "90px",
                            "offsetTop": "390px",
                            "offsetStart": "10px",
                            "paddingAll": "none",
                            "action": {
                              "type": "message",
                              "label": "action",
                              "text": "/BONUSTIME_SBOS"
                            }
                          },
                          {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                              {
                                "type": "image",
                                "url": "https://i.postimg.cc/wTZpVHZt/YGR.png",
                                "position": "absolute",
                                "size": "85px"
                              }
                            ],
                            "position": "absolute",
                            "height": "90px",
                            "width": "90px",
                            "offsetTop": "390px",
                            "offsetStart": "205px",
                            "paddingAll": "none",
                            "action": {
                              "type": "message",
                              "label": "action",
                              "text": "/BONUSTIME_YGR"
                            }
                          }
                        ],
                        "paddingTop": "none",
                        "paddingBottom": "none",
                        "paddingStart": "none",
                        "paddingEnd": "none",
                        "height": "500px",
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
                "height": "540px",
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
                "type": "image",
                "url": "https://i.postimg.cc/15gQ0Fs0/1742191510026.webp",
                "size": "full",
                "aspectRatio": "3:1",
                "backgroundColor": "#101010",
                "animated": True,
                "align": "start"
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
                        "aspectRatio": "3:6",
                        "aspectMode": "cover",
                        "animated": True,
                        "offsetTop": "-50px"
                      }
                    ],
                    "position": "absolute",
                    "width": "300px",
                    "height": "500px"
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
                      "text": "/BONUSTIME_WR"
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
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "image",
                        "url": "https://lh3.googleusercontent.com/d/17TqSoU6cvAEiHQLSibKYlM1n9afQXhAa",
                        "position": "absolute",
                        "size": "85px"
                      }
                    ],
                    "position": "absolute",
                    "height": "90px",
                    "width": "90px",
                    "offsetTop": "295px",
                    "offsetStart": "10px",
                    "paddingAll": "none",
                    "action": {
                      "type": "message",
                      "label": "action",
                      "text": "/BONUSTIME_CDG"
                    }
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [],
                    "height": "100px",
                    "width": "280px",
                    "offsetTop": "390px",
                    "offsetStart": "10px",
                    "paddingAll": "none"
                  }
                ],
                "paddingTop": "none",
                "paddingBottom": "none",
                "paddingStart": "none",
                "paddingEnd": "none",
                "height": "500px",
                "backgroundColor": "#545454",
                "maxWidth": "300px",
                "offsetTop": "-5px"
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
    with open(api_folder + '/flex_message/BONUSTIME.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)
        
    if debug:
        print(api_folder + '/flex_message/BONUSTIME.json')

def BONUSTIME_PP(api_folder):

    # ดึงเวลาปัจจุบัน
    now = datetime.now()

    # แปลงเวลาเป็นรูปแบบ "00:00"
    formatted_time = now.strftime("%H")
    # แปลงเวลาเป็น integer ก่อนที่จะบวก
    num = int(formatted_time) + 1

    # อ่านข้อมูลจากไฟล์ PP_Game.json
    with open(api_folder + '/PP_Game.json', 'r', encoding='utf-8') as json_file:
        PP_Game = json.load(json_file)

    # สร้างเซ็ตเพื่อเก็บเปอร์เซ็นต์ที่สร้างขึ้นแล้ว
    used_percentages = set()
    used_data = set()
    used_percen_splins = set()
    used_percen_game = set()

    # สร้างข้อความ message_percen และตรวจสอบเปอร์เซ็นต์ในเซ็ต
    def generate_unique_percentage():
        while True:
            percentage = random.uniform(80, 92)
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
                    "url": "https://img5.pic.in.th/file/secure-sv1/PP00177c9c80275ee8.png",
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
                                    "text": "ตั้งแต่เวลา" + Bonustime_Update,
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
        game = random.choice(PP_Game)

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
                game = random.choice(PP_Game)

        message_percen = generate_unique_percentage()
        message_percen_splin = generate_unique_percen_splin()
        message_percen_game = generate_unique_percentage_game()

        bubble = {
            "type": "bubble",
            "hero": {
                "type": "image",
                "url": bg_image,
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
                                "url": "https://img2.pic.in.th/pic/MicrosoftTeams-image-7.webp",
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
    with open(api_folder + '/flex_message/BONUSTIME_PP.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)
    if debug:
        print(api_folder + '/flex_message/BONUSTIME_PP.json')

def BONUSTIME_AMBG(api_folder):
    # ดึงเวลาปัจจุบัน
    now = datetime.now()

    # แปลงเวลาเป็นรูปแบบ "00:00"
    formatted_time = now.strftime("%H")
    # แปลงเวลาเป็น integer ก่อนที่จะบวก
    num = int(formatted_time) + 1

    # อ่านข้อมูลจากไฟล์ AMBG_Game.json
    with open(api_folder + '/AMBG_Game.json', 'r', encoding='utf-8') as json_file:
        AMBG_Game = json.load(json_file)

    # สร้างเซ็ตเพื่อเก็บเปอร์เซ็นต์ที่สร้างขึ้นแล้ว
    used_percentages = set()
    used_data = set()
    used_percen_splins = set()
    used_percen_game = set()

    # สร้างข้อความ message_percen และตรวจสอบเปอร์เซ็นต์ในเซ็ต
    def generate_unique_percentage():
        while True:
            percentage = random.uniform(70, 95)
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
            percentage_game = random.randint(1, 23)
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
                    "url": "https://i.postimg.cc/0j35ZwbP/ambg1.png",
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
                                    "text": "ตั้งแต่เวลา" + Bonustime_Update,
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
        game = random.choice(AMBG_Game)

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
                game = random.choice(AMBG_Game)

        message_percen = generate_unique_percentage()
        message_percen_splin = generate_unique_percen_splin()
        message_percen_game = generate_unique_percentage_game()

        bubble = {
            "type": "bubble",
            "hero": {
                "type": "image",
                "url": bg_image,
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
                                "url": "https://i.postimg.cc/T1Phtx0q/logo-tp-526.png",
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
    with open(api_folder + '/flex_message/BONUSTIME_AMBG.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)

    if debug:
        print(api_folder + '/flex_message/BONUSTIME_AMBG.json')

def BONUSTIME_AMP(api_folder):
    # ดึงเวลาปัจจุบัน
    now = datetime.now()

    # แปลงเวลาเป็นรูปแบบ "00:00"
    formatted_time = now.strftime("%H")
    # แปลงเวลาเป็น integer ก่อนที่จะบวก
    num = int(formatted_time) + 1

    # อ่านข้อมูลจากไฟล์ AMP_Game.json
    with open(api_folder + '/AMP_Game.json', 'r', encoding='utf-8') as json_file:
        AMP_Game = json.load(json_file)

    # สร้างเซ็ตเพื่อเก็บเปอร์เซ็นต์ที่สร้างขึ้นแล้ว
    used_percentages = set()
    used_data = set()
    used_percen_splins = set()
    used_percen_game = set()

    # สร้างข้อความ message_percen และตรวจสอบเปอร์เซ็นต์ในเซ็ต
    def generate_unique_percentage():
        while True:
            percentage = random.uniform(70, 95)
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
            percentage_game = random.randint(1, 23)
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
                    "url": "https://i.postimg.cc/C1Gb3wb3/amp1.png",
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
                                    "text": "ตั้งแต่เวลา" + Bonustime_Update,
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
        game = random.choice(AMP_Game)

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
                game = random.choice(AMP_Game)

        message_percen = generate_unique_percentage()
        message_percen_splin = generate_unique_percen_splin()
        message_percen_game = generate_unique_percentage_game()

        bubble = {
            "type": "bubble",
            "hero": {
                "type": "image",
                "url": bg_image,
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
                                "url": "https://i.postimg.cc/Wp9dhDp9/logo-tp-9934.webp",
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
    with open(api_folder + '/flex_message/BONUSTIME_AMP.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)
    if debug:
        print(api_folder + '/flex_message/BONUSTIME_AMP.json')

def BONUSTIME_KAGM(api_folder):
    # ดึงเวลาปัจจุบัน
    now = datetime.now()

    # แปลงเวลาเป็นรูปแบบ "00:00"
    formatted_time = now.strftime("%H")
    # แปลงเวลาเป็น integer ก่อนที่จะบวก
    num = int(formatted_time) + 1

    # อ่านข้อมูลจากไฟล์ KAGM_Game.json
    with open(api_folder + '/KAGM_Game.json', 'r', encoding='utf-8') as json_file:
        KAGM_Game = json.load(json_file)

    # สร้างเซ็ตเพื่อเก็บเปอร์เซ็นต์ที่สร้างขึ้นแล้ว
    used_percentages = set()
    used_data = set()
    used_percen_splins = set()
    used_percen_game = set()

    # สร้างข้อความ message_percen และตรวจสอบเปอร์เซ็นต์ในเซ็ต
    def generate_unique_percentage():
        while True:
            percentage = random.uniform(70, 95)
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
            percentage_game = random.randint(1, 23)
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
                    "url": "https://i.postimg.cc/BbsDBRPJ/KAGM1.png",
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
                                    "text": "ตั้งแต่เวลา" + Bonustime_Update,
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
        game = random.choice(KAGM_Game)

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
                game = random.choice(KAGM_Game)

        message_percen = generate_unique_percentage()
        message_percen_splin = generate_unique_percen_splin()
        message_percen_game = generate_unique_percentage_game()

        bubble = {
            "type": "bubble",
            "hero": {
                "type": "image",
                "url": bg_image,
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
                                "url": "https://i.postimg.cc/vTznqX5f/ka-gaming.webp",
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
    with open(api_folder + '/flex_message/BONUSTIME_KAGM.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)
    if debug:
        print(api_folder + '/flex_message/BONUSTIME_KAGM.json')

def BONUSTIME_K9(api_folder):
    # ดึงเวลาปัจจุบัน
    now = datetime.now()

    # แปลงเวลาเป็นรูปแบบ "00:00"
    formatted_time = now.strftime("%H")
    # แปลงเวลาเป็น integer ก่อนที่จะบวก
    num = int(formatted_time) + 1

    # อ่านข้อมูลจากไฟล์ K9_Game.json
    with open(api_folder + '/K9_Game.json', 'r', encoding='utf-8') as json_file:
        K9_Game = json.load(json_file)

    # สร้างเซ็ตเพื่อเก็บเปอร์เซ็นต์ที่สร้างขึ้นแล้ว
    used_percentages = set()
    used_data = set()
    used_percen_splins = set()
    used_percen_game = set()

    # สร้างข้อความ message_percen และตรวจสอบเปอร์เซ็นต์ในเซ็ต
    def generate_unique_percentage():
        while True:
            percentage = random.uniform(70, 95)
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
            percentage_game = random.randint(1, 23)
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
                    "url": "https://i.postimg.cc/vBfvGrwS/K91.png",
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
                                    "text": "ตั้งแต่เวลา" + Bonustime_Update,
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
        game = random.choice(K9_Game)

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
                game = random.choice(K9_Game)

        message_percen = generate_unique_percentage()
        message_percen_splin = generate_unique_percen_splin()
        message_percen_game = generate_unique_percentage_game()

        bubble = {
            "type": "bubble",
            "hero": {
                "type": "image",
                "url": bg_image,
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
                                "url": "https://i.postimg.cc/xC5cG8v1/unnamed-1.png",
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
    with open(api_folder + '/flex_message/BONUSTIME_K9.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)
    if debug:
        print(api_folder + '/flex_message/BONUSTIME_K9.json')

def BONUSTIME_NS(api_folder):
    # ดึงเวลาปัจจุบัน
    now = datetime.now()

    # แปลงเวลาเป็นรูปแบบ "00:00"
    formatted_time = now.strftime("%H")
    # แปลงเวลาเป็น integer ก่อนที่จะบวก
    num = int(formatted_time) + 1

    # อ่านข้อมูลจากไฟล์ NS_Game.json
    with open(api_folder + '/NS_Game.json', 'r', encoding='utf-8') as json_file:
        NS_Game = json.load(json_file)

    # สร้างเซ็ตเพื่อเก็บเปอร์เซ็นต์ที่สร้างขึ้นแล้ว
    used_percentages = set()
    used_data = set()
    used_percen_splins = set()
    used_percen_game = set()

    # สร้างข้อความ message_percen และตรวจสอบเปอร์เซ็นต์ในเซ็ต
    def generate_unique_percentage():
        while True:
            percentage = random.uniform(70, 95)
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
            percentage_game = random.randint(1, 23)
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
                    "url": "https://i.postimg.cc/Fzh0mwZ7/NS1.png",
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
                                    "text": "ตั้งแต่เวลา" + Bonustime_Update,
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
        game = random.choice(NS_Game)

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
                game = random.choice(NS_Game)

        message_percen = generate_unique_percentage()
        message_percen_splin = generate_unique_percen_splin()
        message_percen_game = generate_unique_percentage_game()

        bubble = {
            "type": "bubble",
            "hero": {
                "type": "image",
                "url": bg_image,
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
                                "url": "https://i.postimg.cc/dtpDjzyr/Nextspin.png",
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
    with open(api_folder + '/flex_message/BONUSTIME_NS.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)
    if debug:
        print(api_folder + '/flex_message/BONUSTIME_NS.json')

def BONUSTIME_SPG(api_folder):
    # ดึงเวลาปัจจุบัน
    now = datetime.now()

    # แปลงเวลาเป็นรูปแบบ "00:00"
    formatted_time = now.strftime("%H")
    # แปลงเวลาเป็น integer ก่อนที่จะบวก
    num = int(formatted_time) + 1

    # อ่านข้อมูลจากไฟล์ SPG_Game.json
    with open(api_folder + '/SPG_Game.json', 'r', encoding='utf-8') as json_file:
        SPG_Game = json.load(json_file)

    # สร้างเซ็ตเพื่อเก็บเปอร์เซ็นต์ที่สร้างขึ้นแล้ว
    used_percentages = set()
    used_data = set()
    used_percen_splins = set()
    used_percen_game = set()

    # สร้างข้อความ message_percen และตรวจสอบเปอร์เซ็นต์ในเซ็ต
    def generate_unique_percentage():
        while True:
            percentage = random.uniform(70, 95)
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
            percentage_game = random.randint(1, 23)
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
                    "url": "https://i.postimg.cc/SRVCKVTV/SPG1.png",
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
                                    "text": "ตั้งแต่เวลา" + Bonustime_Update,
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
        game = random.choice(SPG_Game)

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
                game = random.choice(SPG_Game)

        message_percen = generate_unique_percentage()
        message_percen_splin = generate_unique_percen_splin()
        message_percen_game = generate_unique_percentage_game()

        bubble = {
            "type": "bubble",
            "hero": {
                "type": "image",
                "url": bg_image,
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
                                "url": "https://i.postimg.cc/25F6myX7/spadegaming-1.png",
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
    with open(api_folder + '/flex_message/BONUSTIME_SPG.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)
    if debug:
        print(api_folder + '/flex_message/BONUSTIME_SPG.json')

def BONUSTIME_RY(api_folder):
    # ดึงเวลาปัจจุบัน
    now = datetime.now()

    # แปลงเวลาเป็นรูปแบบ "00:00"
    formatted_time = now.strftime("%H")
    # แปลงเวลาเป็น integer ก่อนที่จะบวก
    num = int(formatted_time) + 1

    # อ่านข้อมูลจากไฟล์ RY_Game.json
    with open(api_folder + '/RY_Game.json', 'r', encoding='utf-8') as json_file:
        RY_Game = json.load(json_file)

    # สร้างเซ็ตเพื่อเก็บเปอร์เซ็นต์ที่สร้างขึ้นแล้ว
    used_percentages = set()
    used_data = set()
    used_percen_splins = set()
    used_percen_game = set()

    # สร้างข้อความ message_percen และตรวจสอบเปอร์เซ็นต์ในเซ็ต
    def generate_unique_percentage():
        while True:
            percentage = random.uniform(70, 95)
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
            percentage_game = random.randint(1, 23)
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
                    "url": "https://i.postimg.cc/PxcwNpKB/Royal-Slot.png",
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
                                    "text": "ตั้งแต่เวลา" + Bonustime_Update,
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
        game = random.choice(RY_Game)

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
                game = random.choice(RY_Game)

        message_percen = generate_unique_percentage()
        message_percen_splin = generate_unique_percen_splin()
        message_percen_game = generate_unique_percentage_game()

        bubble = {
            "type": "bubble",
            "hero": {
                "type": "image",
                "url": bg_image,
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
                                "url": "https://i.postimg.cc/nVg5Bnzx/the-online-casino-product-from-royal-slots-game-gamingsoft.png",
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
    with open(api_folder + '/flex_message/BONUSTIME_RY.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)
    if debug:
        print(api_folder + '/flex_message/BONUSTIME_RY.json')

def BONUSTIME_DGG(api_folder):
    # ดึงเวลาปัจจุบัน
    now = datetime.now()

    # แปลงเวลาเป็นรูปแบบ "00:00"
    formatted_time = now.strftime("%H")
    # แปลงเวลาเป็น integer ก่อนที่จะบวก
    num = int(formatted_time) + 1

    # อ่านข้อมูลจากไฟล์ DGG_Game.json
    with open(api_folder + '/DGG_Game.json', 'r', encoding='utf-8') as json_file:
        DGG_Game = json.load(json_file)

    # สร้างเซ็ตเพื่อเก็บเปอร์เซ็นต์ที่สร้างขึ้นแล้ว
    used_percentages = set()
    used_data = set()
    used_percen_splins = set()
    used_percen_game = set()

    # สร้างข้อความ message_percen และตรวจสอบเปอร์เซ็นต์ในเซ็ต
    def generate_unique_percentage():
        while True:
            percentage = random.uniform(70, 95)
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
            percentage_game = random.randint(1, 23)
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
                    "url": "https://i.postimg.cc/NGVDSL89/Dragongaming.png",
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
                                    "text": "ตั้งแต่เวลา" + Bonustime_Update,
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
        game = random.choice(DGG_Game)

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
                game = random.choice(DGG_Game)

        message_percen = generate_unique_percentage()
        message_percen_splin = generate_unique_percen_splin()
        message_percen_game = generate_unique_percentage_game()

        bubble = {
            "type": "bubble",
            "hero": {
                "type": "image",
                "url": bg_image,
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
                                "url": "https://i.postimg.cc/3wKFmGh6/logo-hacksaw-gaming.png",
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
    with open(api_folder + '/flex_message/BONUSTIME_DGG.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)
    if debug:
        print(api_folder + '/flex_message/BONUSTIME_DGG.json')

def BONUSTIME_PG(api_folder):
    # ดึงเวลาปัจจุบัน
    now = datetime.now()

    # แปลงเวลาเป็นรูปแบบ "00:00"
    formatted_time = now.strftime("%H")
    # แปลงเวลาเป็น integer ก่อนที่จะบวก
    num = int(formatted_time) + 1

    # อ่านข้อมูลจากไฟล์ PG_Game.json
    with open(api_folder + '/PG_Game.json', 'r', encoding='utf-8') as json_file:
        PG_Game = json.load(json_file)

    # สร้างเซ็ตเพื่อเก็บเปอร์เซ็นต์ที่สร้างขึ้นแล้ว
    used_percentages = set()
    used_data = set()
    used_percen_splins = set()
    used_percen_game = set()

    # สร้างข้อความ message_percen และตรวจสอบเปอร์เซ็นต์ในเซ็ต
    def generate_unique_percentage():
        while True:
            percentage = random.uniform(70, 95)
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
            percentage_game = random.randint(1, 23)
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
        "url": "https://img5.pic.in.th/file/secure-sv1/ezgif874bd66cc534aff6.png",
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
        game = random.choice(PG_Game)
        
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
                game = random.choice(PG_Game)

        message_percen = generate_unique_percentage()
        message_percen_splin = generate_unique_percen_splin()
        message_percen_game = generate_unique_percentage_game()

        bubble =    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": bg_image,
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
                "url": "https://img2.pic.in.th/pic/nav_common_logo_white2x.063bde329b3c4fac026b978.png",
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
    with open(api_folder + '/flex_message/BONUSTIME_PG.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)
    if debug:
        print(api_folder + '/flex_message/BONUSTIME_PG.json')

def BONUSTIME_HK(api_folder):
    # ดึงเวลาปัจจุบัน
    now = datetime.now()

    # แปลงเวลาเป็นรูปแบบ "00:00"
    formatted_time = now.strftime("%H")
    # แปลงเวลาเป็น integer ก่อนที่จะบวก
    num = int(formatted_time) + 1

    # อ่านข้อมูลจากไฟล์ HK_Game.json
    with open(api_folder + '/HK_Game.json', 'r', encoding='utf-8') as json_file:
        HK_Game = json.load(json_file)

    # สร้างเซ็ตเพื่อเก็บเปอร์เซ็นต์ที่สร้างขึ้นแล้ว
    used_percentages = set()
    used_data = set()
    used_percen_splins = set()
    used_percen_game = set()

    # สร้างข้อความ message_percen และตรวจสอบเปอร์เซ็นต์ในเซ็ต
    def generate_unique_percentage():
        while True:
            percentage = random.uniform(70, 95)
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
            percentage_game = random.randint(1, 23)
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
        "url": "https://i.postimg.cc/RhPkxmRC/Hacksaw.png",
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
        game = random.choice(HK_Game)
        
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
                game = random.choice(HK_Game)

        message_percen = generate_unique_percentage()
        message_percen_splin = generate_unique_percen_splin()
        message_percen_game = generate_unique_percentage_game()

        bubble =    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": bg_image,
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
                "url": "https://i.postimg.cc/h4pWd8BF/logo-hacksaw-gaming.png",
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
    with open(api_folder + '/flex_message/BONUSTIME_HK.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)
    if debug:
        print(api_folder + '/flex_message/BONUSTIME_HK.json')

def BONUSTIME_OP(api_folder):
    # ดึงเวลาปัจจุบัน
    now = datetime.now()

    # แปลงเวลาเป็นรูปแบบ "00:00"
    formatted_time = now.strftime("%H")
    # แปลงเวลาเป็น integer ก่อนที่จะบวก
    num = int(formatted_time) + 1

    # อ่านข้อมูลจากไฟล์ OP_Game.json
    with open(api_folder + '/OP_Game.json', 'r', encoding='utf-8') as json_file:
        OP_Game = json.load(json_file)

    # สร้างเซ็ตเพื่อเก็บเปอร์เซ็นต์ที่สร้างขึ้นแล้ว
    used_percentages = set()
    used_data = set()
    used_percen_splins = set()
    used_percen_game = set()

    # สร้างข้อความ message_percen และตรวจสอบเปอร์เซ็นต์ในเซ็ต
    def generate_unique_percentage():
        while True:
            percentage = random.uniform(70, 95)
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
            percentage_game = random.randint(1, 23)
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
        "url": "https://i.postimg.cc/k4R6bM2z/Octoplay.png",
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
        game = random.choice(OP_Game)
        
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
                game = random.choice(OP_Game)

        message_percen = generate_unique_percentage()
        message_percen_splin = generate_unique_percen_splin()
        message_percen_game = generate_unique_percentage_game()

        bubble =    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": bg_image,
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
                "url": "https://i.postimg.cc/mkb4G8Wj/1360b.png",
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
    with open(api_folder + '/flex_message/BONUSTIME_OP.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)
    if debug:
        print(api_folder + '/flex_message/BONUSTIME_OP.json')

def BONUSTIME_GO(api_folder):
    # ดึงเวลาปัจจุบัน
    now = datetime.now()

    # แปลงเวลาเป็นรูปแบบ "00:00"
    formatted_time = now.strftime("%H")
    # แปลงเวลาเป็น integer ก่อนที่จะบวก
    num = int(formatted_time) + 1

    # อ่านข้อมูลจากไฟล์ GO_Game.json
    with open(api_folder + '/GO_Game.json', 'r', encoding='utf-8') as json_file:
        GO_Game = json.load(json_file)

    # สร้างเซ็ตเพื่อเก็บเปอร์เซ็นต์ที่สร้างขึ้นแล้ว
    used_percentages = set()
    used_data = set()
    used_percen_splins = set()
    used_percen_game = set()

    # สร้างข้อความ message_percen และตรวจสอบเปอร์เซ็นต์ในเซ็ต
    def generate_unique_percentage():
        while True:
            percentage = random.uniform(70, 95)
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
            percentage_game = random.randint(1, 23)
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
        "url": "https://i.postimg.cc/Zq7sqHNj/Play-n-Go.png",
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
        game = random.choice(GO_Game)
        
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
                game = random.choice(GO_Game)

        message_percen = generate_unique_percentage()
        message_percen_splin = generate_unique_percen_splin()
        message_percen_game = generate_unique_percentage_game()

        bubble =    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": bg_image,
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
                "url": "https://i.postimg.cc/vBCPrm3V/9217783f1982b255-org.png",
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
    with open(api_folder + '/flex_message/BONUSTIME_GO.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)
    if debug:
      print(api_folder + '/flex_message/BONUSTIME_GO.json')

def BONUSTIME_R88(api_folder):
    # ดึงเวลาปัจจุบัน
    now = datetime.now()

    # แปลงเวลาเป็นรูปแบบ "00:00"
    formatted_time = now.strftime("%H")
    # แปลงเวลาเป็น integer ก่อนที่จะบวก
    num = int(formatted_time) + 1

    # อ่านข้อมูลจากไฟล์ R88_Game.json
    with open(api_folder + '/R88_Game.json', 'r', encoding='utf-8') as json_file:
        R88_Game = json.load(json_file)

    # สร้างเซ็ตเพื่อเก็บเปอร์เซ็นต์ที่สร้างขึ้นแล้ว
    used_percentages = set()
    used_data = set()
    used_percen_splins = set()
    used_percen_game = set()

    # สร้างข้อความ message_percen และตรวจสอบเปอร์เซ็นต์ในเซ็ต
    def generate_unique_percentage():
        while True:
            percentage = random.uniform(70, 95)
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
            percentage_game = random.randint(1, 23)
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
        "url": "https://i.postimg.cc/xCkQjcXJ/Rich88.png",
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
        game = random.choice(R88_Game)
        
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
                game = random.choice(R88_Game)

        message_percen = generate_unique_percentage()
        message_percen_splin = generate_unique_percen_splin()
        message_percen_game = generate_unique_percentage_game()

        bubble =    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": bg_image,
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
                "url": "https://i.postimg.cc/vTfd9kLG/logo-hacksaw-gaming.png",
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
    with open(api_folder + '/flex_message/BONUSTIME_R88.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)
    if debug:
      print(api_folder + '/flex_message/BONUSTIME_R88.json')
    
def BONUSTIME_NL(api_folder):
    # ดึงเวลาปัจจุบัน
    now = datetime.now()

    # แปลงเวลาเป็นรูปแบบ "00:00"
    formatted_time = now.strftime("%H")
    # แปลงเวลาเป็น integer ก่อนที่จะบวก
    num = int(formatted_time) + 1

    # อ่านข้อมูลจากไฟล์ `jl_Game.json
    with open(api_folder + '/NL_game.json', 'r', encoding='utf-8') as json_file:
        NL_game = json.load(json_file)

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
        "url": "https://img5.pic.in.th/file/secure-sv1/NL.png",
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
        game = random.choice(NL_game)
        
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
                game = random.choice(NL_game)

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
                "url": "https://img2.pic.in.th/pic/cropped-nolimit-city.png",
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
    with open(api_folder + '/flex_message/BONUSTIME_NL.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)
    if debug:    
        print(api_folder + '/flex_message/BONUSTIME_NL.json')

def BONUSTIME_NE(api_folder):
    # ดึงเวลาปัจจุบัน
    now = datetime.now()

    # แปลงเวลาเป็นรูปแบบ "00:00"
    formatted_time = now.strftime("%H")
    # แปลงเวลาเป็น integer ก่อนที่จะบวก
    num = int(formatted_time) + 1

    # อ่านข้อมูลจากไฟล์ `jl_Game.json
    with open(api_folder + '/NE_game.json', 'r', encoding='utf-8') as json_file:
        NE_game = json.load(json_file)

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
        "url": "https://img5.pic.in.th/file/secure-sv1/NE.png",
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
        game = random.choice(NE_game)
        
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
                game = random.choice(NE_game)

        message_percen = generate_unique_percentage()
        message_percen_splin = generate_unique_percen_splin()
        message_percen_game = generate_unique_percentage_game()

        bubble =    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": bg_image,
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
                "url": "https://img2.pic.in.th/pic/netent_logo_online_white_and_green.png",
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
    with open(api_folder + '/flex_message/BONUSTIME_NE.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)
    if debug:
        print(api_folder + '/flex_message/BONUSTIME_NE.json')

def BONUSTIME_MG(api_folder):
    # ดึงเวลาปัจจุบัน
    now = datetime.now()

    # แปลงเวลาเป็นรูปแบบ "00:00"
    formatted_time = now.strftime("%H")
    # แปลงเวลาเป็น integer ก่อนที่จะบวก
    num = int(formatted_time) + 1

    # อ่านข้อมูลจากไฟล์ `jl_Game.json
    with open(api_folder + '/MC_game.json', 'r', encoding='utf-8') as json_file:
        MC_game = json.load(json_file)

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
        "url": "https://img5.pic.in.th/file/secure-sv1/MC11f6ba13f6d8f5e7.png",
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
        game = random.choice(MC_game)
        
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
                game = random.choice(MC_game)

        message_percen = generate_unique_percentage()
        message_percen_splin = generate_unique_percen_splin()
        message_percen_game = generate_unique_percentage_game()

        bubble =    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": bg_image,
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
                "url": "https://img2.pic.in.th/pic/pngegg-21f9aa84d8368d623.png",
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
    with open(api_folder + '/flex_message/BONUSTIME_MG.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)
    if debug:
        print(api_folder + '/flex_message/BONUSTIME_MG.json')

def BONUSTIME_JL(api_folder):
    # ดึงเวลาปัจจุบัน
    now = datetime.now()

    # แปลงเวลาเป็นรูปแบบ "00:00"
    formatted_time = now.strftime("%H")
    # แปลงเวลาเป็น integer ก่อนที่จะบวก
    num = int(formatted_time) + 1

    # อ่านข้อมูลจากไฟล์ JL_Game.json
    with open(api_folder + '/JL_Game.json', 'r', encoding='utf-8') as json_file:
        JL_Game = json.load(json_file)

    # สร้างเซ็ตเพื่อเก็บเปอร์เซ็นต์ที่สร้างขึ้นแล้ว
    used_percentages = set()
    used_data = set()
    used_percen_splins = set()
    used_percen_game = set()

    # สร้างข้อความ message_percen และตรวจสอบเปอร์เซ็นต์ในเซ็ต
    def generate_unique_percentage():
        while True:
            percentage = random.uniform(70, 95)
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
            percentage_game = random.randint(1, 23)
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
        "url": "https://img2.pic.in.th/pic/JL.png",
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
        game = random.choice(JL_Game)
        
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
                game = random.choice(JL_Game)

        message_percen = generate_unique_percentage()
        message_percen_splin = generate_unique_percen_splin()
        message_percen_game = generate_unique_percentage_game()

        bubble =    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": bg_image,
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
                "url": "https://img2.pic.in.th/pic/Logo-Jili.webp",
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
    with open(api_folder + '/flex_message/BONUSTIME_JL.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)
    if debug:
        print(api_folder + '/flex_message/BONUSTIME_JL.json')

def BONUSTIME_JK(api_folder):
    # ดึงเวลาปัจจุบัน
    now = datetime.now()

    # แปลงเวลาเป็นรูปแบบ "00:00"
    formatted_time = now.strftime("%H")
    # แปลงเวลาเป็น integer ก่อนที่จะบวก
    num = int(formatted_time) + 1

    # อ่านข้อมูลจากไฟล์ `JK_Game.json
    with open(api_folder + '/JK_game.json', 'r', encoding='utf-8') as json_file:
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
    with open(api_folder + '/flex_message/BONUSTIME_JK.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)
    if debug:
        print(api_folder + '/flex_message/BONUSTIME_JK.json')

def BONUSTIME_AMB(api_folder):
    # ดึงเวลาปัจจุบัน
    now = datetime.now()

    # แปลงเวลาเป็นรูปแบบ "00:00"
    formatted_time = now.strftime("%H")
    # แปลงเวลาเป็น integer ก่อนที่จะบวก
    num = int(formatted_time) + 1

    # อ่านข้อมูลจากไฟล์ `jl_Game.json
    with open(api_folder + '/AMB_game.json', 'r', encoding='utf-8') as json_file:
        AMB_game = json.load(json_file)

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
        "url": "https://img2.pic.in.th/pic/AMB.png",
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
        game = random.choice(AMB_game)
        
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
                game = random.choice(AMB_game)

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
                "url": "https://img2.pic.in.th/pic/askmebetthai.png.webp",
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
    with open(api_folder + '/flex_message/BONUSTIME_AMB.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)
    if debug:
        print(api_folder + '/flex_message/BONUSTIME_AMBS.json')

def BONUSTIME_AMBS(api_folder):
    # ดึงเวลาปัจจุบัน
    now = datetime.now()

    # แปลงเวลาเป็นรูปแบบ "00:00"
    formatted_time = now.strftime("%H")
    # แปลงเวลาเป็น integer ก่อนที่จะบวก
    num = int(formatted_time) + 1

    # อ่านข้อมูลจากไฟล์ AMBS_game.json
    with open(api_folder + '/AMBS_game.json', 'r', encoding='utf-8') as json_file:
        AMBS_game = json.load(json_file)

    # สร้างเซ็ตเพื่อเก็บเปอร์เซ็นต์ที่สร้างขึ้นแล้ว
    used_percentages = set()
    used_data = set()
    used_percen_splins = set()
    used_percen_game = set()

    # สร้างข้อความ message_percen และตรวจสอบเปอร์เซ็นต์ในเซ็ต
    def generate_unique_percentage():
        while True:
            percentage = random.uniform(70, 95)
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
            percentage_game = random.randint(1, 23)
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
        "url": "https://img5.pic.in.th/file/secure-sv1/1AMBS.png",
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
  ],"sender": {
      "iconUrl": "https://video-public.canva.com/VAEQmJMm6R8/v/a372d097e3.gif",
      "name": "เลขาธีม 😁"
    }, "quickReply": {
    "items": [  
          {
        "type": "action",
        "imageUrl": "https://video-public.canva.com/VADhwZBf_RY/v/0d1c3ca5c8.gif",
          "action": {
         "type": "uri",
         "label": "ธีมทางการใหม่",
         "uri": "https://line.me/R/shop/theme/showcase?id=new"
   }
      },      {
        "type": "action",
        "imageUrl": "https://media-public.canva.com/M7NGs/MAEwAnM7NGs/1/tl.png",
          "action": {
         "type": "uri",
         "label": "สั่งซื้อ iton5",
         "uri": "line://nv/profilePopup/mid=ufb9d34cac39cc328b9febede9f106341"
   }
      }
    ]
  }
}

    # สร้าง bubbles และเพิ่มลงใน data
    for _ in range(Game_List):
        game = random.choice(AMBS_game)
        
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
                game = random.choice(AMBS_game)

        message_percen = generate_unique_percentage()
        message_percen_splin = generate_unique_percen_splin()
        message_percen_game = generate_unique_percentage_game()

        bubble =    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": bg_image,
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
                "url": "https://pic.in.th/image/askmeslot-logo.1K7SW9",
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
    with open(api_folder + '/flex_message/BONUSTIME_AMBS.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)
    if debug:
        print(api_folder + '/flex_message/BONUSTIME_AMBS.json')

def BONUSTIME_CQ9(api_folder):
    # ดึงเวลาปัจจุบัน
    now = datetime.now()

    # แปลงเวลาเป็นรูปแบบ "00:00"
    formatted_time = now.strftime("%H")
    # แปลงเวลาเป็น integer ก่อนที่จะบวก
    num = int(formatted_time) + 1

    # อ่านข้อมูลจากไฟล์ CQ9_Game.json
    with open(api_folder + '/CQ9_Game.json', 'r', encoding='utf-8') as json_file:
        CQ9_Game = json.load(json_file)

    # สร้างเซ็ตเพื่อเก็บเปอร์เซ็นต์ที่สร้างขึ้นแล้ว
    used_percentages = set()
    used_data = set()
    used_percen_splins = set()
    used_percen_game = set()

    # สร้างข้อความ message_percen และตรวจสอบเปอร์เซ็นต์ในเซ็ต
    def generate_unique_percentage():
        while True:
            percentage = random.uniform(70, 95)
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
            percentage_game = random.randint(1, 23)
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
        "url": "https://img2.pic.in.th/pic/1CQ9.png",
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
  ],"sender": {
      "iconUrl": "https://video-public.canva.com/VAEQmJMm6R8/v/a372d097e3.gif",
      "name": "เลขาธีม 😁"
    }, "quickReply": {
    "items": [  
          {
        "type": "action",
        "imageUrl": "https://video-public.canva.com/VADhwZBf_RY/v/0d1c3ca5c8.gif",
          "action": {
         "type": "uri",
         "label": "ธีมทางการใหม่",
         "uri": "https://line.me/R/shop/theme/showcase?id=new"
   }
      },      {
        "type": "action",
        "imageUrl": "https://media-public.canva.com/M7NGs/MAEwAnM7NGs/1/tl.png",
          "action": {
         "type": "uri",
         "label": "สั่งซื้อ iton5",
         "uri": "line://nv/profilePopup/mid=ufb9d34cac39cc328b9febede9f106341"
   }
      }
    ]
  }
}

    # สร้าง bubbles และเพิ่มลงใน data
    for _ in range(Game_List):
        game = random.choice(CQ9_Game)
        
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
                game = random.choice(CQ9_Game)

        message_percen = generate_unique_percentage()
        message_percen_splin = generate_unique_percen_splin()
        message_percen_game = generate_unique_percentage_game()

        bubble =    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": bg_image,
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
                "url": "https://pic.in.th/image/logo.1K7XzN",
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
    with open(api_folder + '/flex_message/BONUSTIME_CQ9.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)
    if debug:
        print(api_folder + '/flex_message/BONUSTIME_CQ9.json')

def BONUSTIME_EVO(api_folder):
    # ดึงเวลาปัจจุบัน
    now = datetime.now()

    # แปลงเวลาเป็นรูปแบบ "00:00"
    formatted_time = now.strftime("%H")
    # แปลงเวลาเป็น integer ก่อนที่จะบวก
    num = int(formatted_time) + 1

    # อ่านข้อมูลจากไฟล์ EVO_Game.json
    with open(api_folder + '/EVO_Game.json', 'r', encoding='utf-8') as json_file:
        EVO_Game = json.load(json_file)

    # สร้างเซ็ตเพื่อเก็บเปอร์เซ็นต์ที่สร้างขึ้นแล้ว
    used_percentages = set()
    used_data = set()
    used_percen_splins = set()
    used_percen_game = set()

    # สร้างข้อความ message_percen และตรวจสอบเปอร์เซ็นต์ในเซ็ต
    def generate_unique_percentage():
        while True:
            percentage = random.uniform(70, 95)
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
            percentage_game = random.randint(1, 23)
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
        "url": "https://img2.pic.in.th/pic/1EVO.png",
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
  ],"sender": {
      "iconUrl": "https://video-public.canva.com/VAEQmJMm6R8/v/a372d097e3.gif",
      "name": "เลขาธีม 😁"
    }, "quickReply": {
    "items": [  
          {
        "type": "action",
        "imageUrl": "https://video-public.canva.com/VADhwZBf_RY/v/0d1c3ca5c8.gif",
          "action": {
         "type": "uri",
         "label": "ธีมทางการใหม่",
         "uri": "https://line.me/R/shop/theme/showcase?id=new"
   }
      },      {
        "type": "action",
        "imageUrl": "https://media-public.canva.com/M7NGs/MAEwAnM7NGs/1/tl.png",
          "action": {
         "type": "uri",
         "label": "สั่งซื้อ iton5",
         "uri": "line://nv/profilePopup/mid=ufb9d34cac39cc328b9febede9f106341"
   }
      }
    ]
  }
}

    # สร้าง bubbles และเพิ่มลงใน data
    for _ in range(Game_List):
        game = random.choice(EVO_Game)
        
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
                game = random.choice(EVO_Game)

        message_percen = generate_unique_percentage()
        message_percen_splin = generate_unique_percen_splin()
        message_percen_game = generate_unique_percentage_game()

        bubble =    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": bg_image,
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
                "url": "https://pic.in.th/image/evoplay-white-portfolio-narrow.1K7cs3",
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
    with open(api_folder + '/flex_message/BONUSTIME_EVO.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)
    if debug:
        print(api_folder + '/flex_message/BONUSTIME_EVO.json')
        
def BONUSTIME_FKG(api_folder):
    # ดึงเวลาปัจจุบัน
    now = datetime.now()

    # แปลงเวลาเป็นรูปแบบ "00:00"
    formatted_time = now.strftime("%H")
    # แปลงเวลาเป็น integer ก่อนที่จะบวก
    num = int(formatted_time) + 1

    # อ่านข้อมูลจากไฟล์ FKG_Game.json
    with open(api_folder + '/FKG_game.json', 'r', encoding='utf-8') as json_file:
        FKG_Game = json.load(json_file)

    # สร้างเซ็ตเพื่อเก็บเปอร์เซ็นต์ที่สร้างขึ้นแล้ว
    used_percentages = set()
    used_data = set()
    used_percen_splins = set()
    used_percen_game = set()

    # สร้างข้อความ message_percen และตรวจสอบเปอร์เซ็นต์ในเซ็ต
    def generate_unique_percentage():
        while True:
            percentage = random.uniform(70, 95)
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
            percentage_game = random.randint(1, 23)
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
        "url": "https://img2.pic.in.th/pic/1FKG.png",
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
  ],"sender": {
      "iconUrl": "https://video-public.canva.com/VAEQmJMm6R8/v/a372d097e3.gif",
      "name": "เลขาธีม 😁"
    }, "quickReply": {
    "items": [  
          {
        "type": "action",
        "imageUrl": "https://video-public.canva.com/VADhwZBf_RY/v/0d1c3ca5c8.gif",
          "action": {
         "type": "uri",
         "label": "ธีมทางการใหม่",
         "uri": "https://line.me/R/shop/theme/showcase?id=new"
   }
      },      {
        "type": "action",
        "imageUrl": "https://media-public.canva.com/M7NGs/MAEwAnM7NGs/1/tl.png",
          "action": {
         "type": "uri",
         "label": "สั่งซื้อ iton5",
         "uri": "line://nv/profilePopup/mid=ufb9d34cac39cc328b9febede9f106341"
   }
      }
    ]
  }
}

    # สร้าง bubbles และเพิ่มลงใน data
    for _ in range(Game_List):
        game = random.choice(FKG_Game)
        
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
                game = random.choice(FKG_Game)

        message_percen = generate_unique_percentage()
        message_percen_splin = generate_unique_percen_splin()
        message_percen_game = generate_unique_percentage_game()

        bubble =    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": bg_image,
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
                "url": "https://img5.pic.in.th/file/secure-sv1/funkygames_2x_6d6a769cff.png",
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
    with open(api_folder + '/flex_message/BONUSTIME_FKG.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)
    if debug:
        print(api_folder + '/flex_message/BONUSTIME_FKG.json')

def BONUSTIME_HBE(api_folder):
    # ดึงเวลาปัจจุบัน
    now = datetime.now()

    # แปลงเวลาเป็นรูปแบบ "00:00"
    formatted_time = now.strftime("%H")
    # แปลงเวลาเป็น integer ก่อนที่จะบวก
    num = int(formatted_time) + 1

    # อ่านข้อมูลจากไฟล์ HBE_Game.json
    with open(api_folder + '/HBE_Game.json', 'r', encoding='utf-8') as json_file:
        HBE_Game = json.load(json_file)

    # สร้างเซ็ตเพื่อเก็บเปอร์เซ็นต์ที่สร้างขึ้นแล้ว
    used_percentages = set()
    used_data = set()
    used_percen_splins = set()
    used_percen_game = set()

    # สร้างข้อความ message_percen และตรวจสอบเปอร์เซ็นต์ในเซ็ต
    def generate_unique_percentage():
        while True:
            percentage = random.uniform(70, 95)
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
            percentage_game = random.randint(1, 23)
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
        "url": "https://img5.pic.in.th/file/secure-sv1/1HBE.png",
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
  ],"sender": {
      "iconUrl": "https://video-public.canva.com/VAEQmJMm6R8/v/a372d097e3.gif",
      "name": "เลขาธีม 😁"
    }, "quickReply": {
    "items": [  
          {
        "type": "action",
        "imageUrl": "https://video-public.canva.com/VADhwZBf_RY/v/0d1c3ca5c8.gif",
          "action": {
         "type": "uri",
         "label": "ธีมทางการใหม่",
         "uri": "https://line.me/R/shop/theme/showcase?id=new"
   }
      },      {
        "type": "action",
        "imageUrl": "https://media-public.canva.com/M7NGs/MAEwAnM7NGs/1/tl.png",
          "action": {
         "type": "uri",
         "label": "สั่งซื้อ iton5",
         "uri": "line://nv/profilePopup/mid=ufb9d34cac39cc328b9febede9f106341"
   }
      }
    ]
  }
}

    # สร้าง bubbles และเพิ่มลงใน data
    for _ in range(Game_List):
        game = random.choice(HBE_Game)
        
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
                game = random.choice(HBE_Game)

        message_percen = generate_unique_percentage()
        message_percen_splin = generate_unique_percen_splin()
        message_percen_game = generate_unique_percentage_game()

        bubble =    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": bg_image,
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
                "url": "https://img5.pic.in.th/file/secure-sv1/habanero-systems-logo-squared-1600x1600.png",
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
    with open(api_folder + '/flex_message/BONUSTIME_HBE.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)
    if debug:
      print(api_folder + '/flex_message/BONUSTIME_HBE.json')

def BONUSTIME_RTG(api_folder):
    # ดึงเวลาปัจจุบัน
    now = datetime.now()

    # แปลงเวลาเป็นรูปแบบ "00:00"
    formatted_time = now.strftime("%H")
    # แปลงเวลาเป็น integer ก่อนที่จะบวก
    num = int(formatted_time) + 1

    # อ่านข้อมูลจากไฟล์ RTG_Game.json
    with open(api_folder + '/RTG_Game.json', 'r', encoding='utf-8') as json_file:
        RTG_Game = json.load(json_file)

    # สร้างเซ็ตเพื่อเก็บเปอร์เซ็นต์ที่สร้างขึ้นแล้ว
    used_percentages = set()
    used_data = set()
    used_percen_splins = set()
    used_percen_game = set()

    # สร้างข้อความ message_percen และตรวจสอบเปอร์เซ็นต์ในเซ็ต
    def generate_unique_percentage():
        while True:
            percentage = random.uniform(70, 95)
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
            percentage_game = random.randint(1, 23)
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
        "url": "https://img5.pic.in.th/file/secure-sv1/1RTG.png",
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
  ],"sender": {
      "iconUrl": "https://video-public.canva.com/VAEQmJMm6R8/v/a372d097e3.gif",
      "name": "เลขาธีม 😁"
    }, "quickReply": {
    "items": [  
          {
        "type": "action",
        "imageUrl": "https://video-public.canva.com/VADhwZBf_RY/v/0d1c3ca5c8.gif",
          "action": {
         "type": "uri",
         "label": "ธีมทางการใหม่",
         "uri": "https://line.me/R/shop/theme/showcase?id=new"
   }
      },      {
        "type": "action",
        "imageUrl": "https://media-public.canva.com/M7NGs/MAEwAnM7NGs/1/tl.png",
          "action": {
         "type": "uri",
         "label": "สั่งซื้อ iton5",
         "uri": "line://nv/profilePopup/mid=ufb9d34cac39cc328b9febede9f106341"
   }
      }
    ]
  }
}

    # สร้าง bubbles และเพิ่มลงใน data
    for _ in range(Game_List):
        game = random.choice(RTG_Game)
        
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
                game = random.choice(RTG_Game)

        message_percen = generate_unique_percentage()
        message_percen_splin = generate_unique_percen_splin()
        message_percen_game = generate_unique_percentage_game()

        bubble =    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": bg_image,
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
                "url": "https://img2.pic.in.th/pic/redtiger.png",
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
    with open(api_folder + '/flex_message/BONUSTIME_RTG.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)
    if debug:
      print(api_folder + '/flex_message/BONUSTIME_RTG.json')

def BONUSTIME_SMP(api_folder):
    # ดึงเวลาปัจจุบัน
    now = datetime.now()

    # แปลงเวลาเป็นรูปแบบ "00:00"
    formatted_time = now.strftime("%H")
    # แปลงเวลาเป็น integer ก่อนที่จะบวก
    num = int(formatted_time) + 1

    # อ่านข้อมูลจากไฟล์ SMP_game.json
    with open(api_folder + '/SMP_game.json', 'r', encoding='utf-8') as json_file:
        SMP_game = json.load(json_file)

    # สร้างเซ็ตเพื่อเก็บเปอร์เซ็นต์ที่สร้างขึ้นแล้ว
    used_percentages = set()
    used_data = set()
    used_percen_splins = set()
    used_percen_game = set()

    # สร้างข้อความ message_percen และตรวจสอบเปอร์เซ็นต์ในเซ็ต
    def generate_unique_percentage():
        while True:
            percentage = random.uniform(70, 95)
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
            percentage_game = random.randint(1, 23)
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
        "url": "https://img5.pic.in.th/file/secure-sv1/1SMP.png",
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
  ],"sender": {
      "iconUrl": "https://video-public.canva.com/VAEQmJMm6R8/v/a372d097e3.gif",
      "name": "เลขาธีม 😁"
    }, "quickReply": {
    "items": [  
          {
        "type": "action",
        "imageUrl": "https://video-public.canva.com/VADhwZBf_RY/v/0d1c3ca5c8.gif",
          "action": {
         "type": "uri",
         "label": "ธีมทางการใหม่",
         "uri": "https://line.me/R/shop/theme/showcase?id=new"
   }
      },      {
        "type": "action",
        "imageUrl": "https://media-public.canva.com/M7NGs/MAEwAnM7NGs/1/tl.png",
          "action": {
         "type": "uri",
         "label": "สั่งซื้อ iton5",
         "uri": "line://nv/profilePopup/mid=ufb9d34cac39cc328b9febede9f106341"
   }
      }
    ]
  }
}

    # สร้าง bubbles และเพิ่มลงใน data
    for _ in range(Game_List):
        game = random.choice(SMP_game)
        
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
                game = random.choice(SMP_game)

        message_percen = generate_unique_percentage()
        message_percen_splin = generate_unique_percen_splin()
        message_percen_game = generate_unique_percentage_game()

        bubble =    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": bg_image,
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
                "url": "https://img5.pic.in.th/file/secure-sv1/simpleplayefd4802bb163adfb.webp",
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
    with open(api_folder + '/flex_message/BONUSTIME_SMP.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)
    if debug:
      print(api_folder + '/flex_message/BONUSTIME_SMP.json')
    
def BONUSTIME_SXO(api_folder):
    # ดึงเวลาปัจจุบัน
    now = datetime.now()

    # แปลงเวลาเป็นรูปแบบ "00:00"
    formatted_time = now.strftime("%H")
    # แปลงเวลาเป็น integer ก่อนที่จะบวก
    num = int(formatted_time) + 1

    # อ่านข้อมูลจากไฟล์ SXO_game.json
    with open(api_folder + '/SXO_game.json', 'r', encoding='utf-8') as json_file:
        SXO_game = json.load(json_file)

    # สร้างเซ็ตเพื่อเก็บเปอร์เซ็นต์ที่สร้างขึ้นแล้ว
    used_percentages = set()
    used_data = set()
    used_percen_splins = set()
    used_percen_game = set()

    # สร้างข้อความ message_percen และตรวจสอบเปอร์เซ็นต์ในเซ็ต
    def generate_unique_percentage():
        while True:
            percentage = random.uniform(70, 95)
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
            percentage_game = random.randint(1, 23)
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
        "url": "https://img2.pic.in.th/pic/1SXO.png",
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
  ],"sender": {
      "iconUrl": "https://video-public.canva.com/VAEQmJMm6R8/v/a372d097e3.gif",
      "name": "เลขาธีม 😁"
    }, "quickReply": {
    "items": [  
          {
        "type": "action",
        "imageUrl": "https://video-public.canva.com/VADhwZBf_RY/v/0d1c3ca5c8.gif",
          "action": {
         "type": "uri",
         "label": "ธีมทางการใหม่",
         "uri": "https://line.me/R/shop/theme/showcase?id=new"
   }
      },      {
        "type": "action",
        "imageUrl": "https://media-public.canva.com/M7NGs/MAEwAnM7NGs/1/tl.png",
          "action": {
         "type": "uri",
         "label": "สั่งซื้อ iton5",
         "uri": "line://nv/profilePopup/mid=ufb9d34cac39cc328b9febede9f106341"
   }
      }
    ]
  }
}

    # สร้าง bubbles และเพิ่มลงใน data
    for _ in range(Game_List):
        game = random.choice(SXO_game)
        
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
                game = random.choice(SXO_game)

        message_percen = generate_unique_percentage()
        message_percen_splin = generate_unique_percen_splin()
        message_percen_game = generate_unique_percentage_game()

        bubble =    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": bg_image,
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
                "url": "https://img2.pic.in.th/pic/logo-slotxo-site.webp",
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
    with open(api_folder +'/flex_message/BONUSTIME_SXO.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)
    if debug:
      print(api_folder +'/flex_message/BONUSTIME_SXO.json')
  
def BONUSTIME_YGG(api_folder):
    # ดึงเวลาปัจจุบัน
    now = datetime.now()

    # แปลงเวลาเป็นรูปแบบ "00:00"
    formatted_time = now.strftime("%H")
    # แปลงเวลาเป็น integer ก่อนที่จะบวก
    num = int(formatted_time) + 1

    # อ่านข้อมูลจากไฟล์ YGG_Game.json
    with open(api_folder + '/YGG_Game.json', 'r', encoding='utf-8') as json_file:
        YGG_Game = json.load(json_file)

    # สร้างเซ็ตเพื่อเก็บเปอร์เซ็นต์ที่สร้างขึ้นแล้ว
    used_percentages = set()
    used_data = set()
    used_percen_splins = set()
    used_percen_game = set()

    # สร้างข้อความ message_percen และตรวจสอบเปอร์เซ็นต์ในเซ็ต
    def generate_unique_percentage():
        while True:
            percentage = random.uniform(70, 95)
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
            percentage_game = random.randint(1, 23)
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
        "url": "https://img5.pic.in.th/file/secure-sv1/1YGG.png",
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
  ],"sender": {
      "iconUrl": "https://video-public.canva.com/VAEQmJMm6R8/v/a372d097e3.gif",
      "name": "เลขาธีม 😁"
    }, "quickReply": {
    "items": [  
          {
        "type": "action",
        "imageUrl": "https://video-public.canva.com/VADhwZBf_RY/v/0d1c3ca5c8.gif",
          "action": {
         "type": "uri",
         "label": "ธีมทางการใหม่",
         "uri": "https://line.me/R/shop/theme/showcase?id=new"
   }
      },      {
        "type": "action",
        "imageUrl": "https://media-public.canva.com/M7NGs/MAEwAnM7NGs/1/tl.png",
          "action": {
         "type": "uri",
         "label": "สั่งซื้อ iton5",
         "uri": "line://nv/profilePopup/mid=ufb9d34cac39cc328b9febede9f106341"
   }
      }
    ]
  }
}

    # สร้าง bubbles และเพิ่มลงใน data
    for _ in range(Game_List):
        game = random.choice(YGG_Game)
        
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
                game = random.choice(YGG_Game)

        message_percen = generate_unique_percentage()
        message_percen_splin = generate_unique_percen_splin()
        message_percen_game = generate_unique_percentage_game()

        bubble =    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": bg_image,
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
                "url": "https://img5.pic.in.th/file/secure-sv1/yggdrasil.webp",
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
    with open(api_folder + '/flex_message/BONUSTIME_YGG.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)
    if debug:
      print(api_folder + '/flex_message/BONUSTIME_YGG.json')

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

def BONUSTIME_SN(api_folder):
    # ดึงเวลาปัจจุบัน
    now = datetime.now()

    # แปลงเวลาเป็นรูปแบบ "00:00"
    formatted_time = now.strftime("%H")
    # แปลงเวลาเป็น integer ก่อนที่จะบวก
    num = int(formatted_time) + 1

    # อ่านข้อมูลจากไฟล์ `jl_Game.json
    with open(api_folder + '/SN_game.json', 'r', encoding='utf-8') as json_file:
        SN_game = json.load(json_file)

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
        "url": "https://img5.pic.in.th/file/secure-sv1/SPbf387d83ceeacfa3.png",
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
        game = random.choice(SN_game)
        
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
                game = random.choice(SN_game)

        message_percen = generate_unique_percentage()
        message_percen_splin = generate_unique_percen_splin()
        message_percen_game = generate_unique_percentage_game()

        bubble =    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": bg_image,
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
                "url": "https://img5.pic.in.th/file/secure-sv1/spinix_logo.webp",
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
    with open(api_folder + '/flex_message/BONUSTIME_SN.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)
    if debug:
      print(api_folder + '/flex_message/BONUSTIME_SN.json')

def BONUSTIME_ACE333(api_folder):
    # ดึงเวลาปัจจุบัน
    now = datetime.now()

    # แปลงเวลาเป็นรูปแบบ "00:00"
    formatted_time = now.strftime("%H")
    # แปลงเวลาเป็น integer ก่อนที่จะบวก
    num = int(formatted_time) + 1

    # อ่านข้อมูลจากไฟล์ `jl_Game.json
    with open(api_folder + '/ACE333_game.json', 'r', encoding='utf-8') as json_file:
        ACE333_game = json.load(json_file)

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
        "url": "https://i.postimg.cc/28vsnX6m/Bg-ACE333.png",
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
        game = random.choice(ACE333_game)
        
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
                game = random.choice(ACE333_game)

        message_percen = generate_unique_percentage()
        message_percen_splin = generate_unique_percen_splin()
        message_percen_game = generate_unique_percentage_game()

        bubble =    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": bg_image,
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
                "url": "https://i.postimg.cc/fWvXkM7h/the-online-casino-product-from-Advant-Play-gamingsoft.png",
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
    with open(api_folder + '/flex_message/BONUSTIME_ACE333.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)
    if debug:
      print(api_folder + '/flex_message/BONUSTIME_ACE333.json')

def BONUSTIME_G5(api_folder):
    # ดึงเวลาปัจจุบัน
    now = datetime.now()

    # แปลงเวลาเป็นรูปแบบ "00:00"
    formatted_time = now.strftime("%H")
    # แปลงเวลาเป็น integer ก่อนที่จะบวก
    num = int(formatted_time) + 1

    # อ่านข้อมูลจากไฟล์ `jl_Game.json
    with open(api_folder + '/G5_game.json', 'r', encoding='utf-8') as json_file:
        G5_game = json.load(json_file)

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
        "url": "https://i.postimg.cc/wjkTQBv6/Bg-5G.png",
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
        game = random.choice(G5_game)
        
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
                game = random.choice(G5_game)

        message_percen = generate_unique_percentage()
        message_percen_splin = generate_unique_percen_splin()
        message_percen_game = generate_unique_percentage_game()

        bubble =    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": bg_image,
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
                "url": "https://i.postimg.cc/ydD1KXTd/the-online-casino-product-from-Advant-Play-gamingsoft.png",
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
    with open(api_folder + '/flex_message/BONUSTIME_G5.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)
    if debug:
      print(api_folder + '/flex_message/BONUSTIME_G5.json')

def BONUSTIME_ADP(api_folder):
    # ดึงเวลาปัจจุบัน
    now = datetime.now()

    # แปลงเวลาเป็นรูปแบบ "00:00"
    formatted_time = now.strftime("%H")
    # แปลงเวลาเป็น integer ก่อนที่จะบวก
    num = int(formatted_time) + 1

    # อ่านข้อมูลจากไฟล์ `jl_Game.json
    with open(api_folder + '/ADP_game.json', 'r', encoding='utf-8') as json_file:
        ADP_game = json.load(json_file)

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
        "url": "https://i.postimg.cc/Dwwc78RD/Bg-ADP.png",
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
        game = random.choice(ADP_game)
        
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
                game = random.choice(ADP_game)

        message_percen = generate_unique_percentage()
        message_percen_splin = generate_unique_percen_splin()
        message_percen_game = generate_unique_percentage_game()

        bubble =    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": bg_image,
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
                "url": "https://i.postimg.cc/C54jgg7S/the-online-casino-product-from-Advant-Play-gamingsoft.png",
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
    with open(api_folder + '/flex_message/BONUSTIME_ADP.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)
    if debug:
      print(api_folder + '/flex_message/BONUSTIME_ADP.json')

def BONUSTIME_BTG(api_folder):
    # ดึงเวลาปัจจุบัน
    now = datetime.now()

    # แปลงเวลาเป็นรูปแบบ "00:00"
    formatted_time = now.strftime("%H")
    # แปลงเวลาเป็น integer ก่อนที่จะบวก
    num = int(formatted_time) + 1

    # อ่านข้อมูลจากไฟล์ `jl_Game.json
    with open(api_folder + '/BTG_game.json', 'r', encoding='utf-8') as json_file:
        BTG_game = json.load(json_file)

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
        "url": "https://i.postimg.cc/mDyccSHS/Bg-BTG.png",
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
        game = random.choice(BTG_game)
        
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
                game = random.choice(BTG_game)

        message_percen = generate_unique_percentage()
        message_percen_splin = generate_unique_percen_splin()
        message_percen_game = generate_unique_percentage_game()

        bubble =    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": bg_image,
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
                "url": "https://i.postimg.cc/VsHfKTmC/the-online-casino-product-from-Advant-Play-gamingsoft.png",
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
    with open(api_folder + '/flex_message/BONUSTIME_BTG.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)
    if debug:
      print(api_folder + '/flex_message/BONUSTIME_BTG.json')

def BONUSTIME_GDY(api_folder):
    # ดึงเวลาปัจจุบัน
    now = datetime.now()

    # แปลงเวลาเป็นรูปแบบ "00:00"
    formatted_time = now.strftime("%H")
    # แปลงเวลาเป็น integer ก่อนที่จะบวก
    num = int(formatted_time) + 1

    # อ่านข้อมูลจากไฟล์ `jl_Game.json
    with open(api_folder + '/GDY_game.json', 'r', encoding='utf-8') as json_file:
        GDY_game = json.load(json_file)

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
        "url": "https://i.postimg.cc/sgPRC0dK/Bg-GDY.png",
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
        game = random.choice(GDY_game)
        
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
                game = random.choice(GDY_game)

        message_percen = generate_unique_percentage()
        message_percen_splin = generate_unique_percen_splin()
        message_percen_game = generate_unique_percentage_game()

        bubble =    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": bg_image,
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
                "url": "https://i.postimg.cc/m2CrhjW1/the-online-casino-product-from-Advant-Play-gamingsoft.png",
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
    with open(api_folder + '/flex_message/BONUSTIME_GDY.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)
    if debug:
      print(api_folder + '/flex_message/BONUSTIME_GDY.json')

def BONUSTIME_MNP(api_folder):
    # ดึงเวลาปัจจุบัน
    now = datetime.now()

    # แปลงเวลาเป็นรูปแบบ "00:00"
    formatted_time = now.strftime("%H")
    # แปลงเวลาเป็น integer ก่อนที่จะบวก
    num = int(formatted_time) + 1

    # อ่านข้อมูลจากไฟล์ `jl_Game.json
    with open(api_folder + '/MNP_game.json', 'r', encoding='utf-8') as json_file:
        MNP_game = json.load(json_file)

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
        "url": "https://i.postimg.cc/K8tgSF8V/Bg-MNP.png",
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
        game = random.choice(MNP_game)
        
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
                game = random.choice(MNP_game)

        message_percen = generate_unique_percentage()
        message_percen_splin = generate_unique_percen_splin()
        message_percen_game = generate_unique_percentage_game()

        bubble =    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": bg_image,
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
                "url": "https://i.postimg.cc/rmZDCwfd/the-online-casino-product-from-Advant-Play-gamingsoft.png",
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
    with open(api_folder + '/flex_message/BONUSTIME_MNP.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)
    if debug:
      print(api_folder + '/flex_message/BONUSTIME_MNP.json')

def BONUSTIME_ODG(api_folder):
    # ดึงเวลาปัจจุบัน
    now = datetime.now()

    # แปลงเวลาเป็นรูปแบบ "00:00"
    formatted_time = now.strftime("%H")
    # แปลงเวลาเป็น integer ก่อนที่จะบวก
    num = int(formatted_time) + 1

    # อ่านข้อมูลจากไฟล์ `jl_Game.json
    with open(api_folder + '/ODG_game.json', 'r', encoding='utf-8') as json_file:
        ODG_game = json.load(json_file)

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
        "url": "https://i.postimg.cc/3rDGCgHY/Bg-ODG.png",
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
        game = random.choice(ODG_game)
        
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
                game = random.choice(ODG_game)

        message_percen = generate_unique_percentage()
        message_percen_splin = generate_unique_percen_splin()
        message_percen_game = generate_unique_percentage_game()

        bubble =    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": bg_image,
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
                "url": "https://i.postimg.cc/FRYL6Sdb/the-online-casino-product-from-Advant-Play-gamingsoft.png",
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
    with open(api_folder + '/flex_message/BONUSTIME_ODG.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)
    if debug:
      print(api_folder + '/flex_message/BONUSTIME_ODG.json')

def BONUSTIME_SW(api_folder):
    # ดึงเวลาปัจจุบัน
    now = datetime.now()

    # แปลงเวลาเป็นรูปแบบ "00:00"
    formatted_time = now.strftime("%H")
    # แปลงเวลาเป็น integer ก่อนที่จะบวก
    num = int(formatted_time) + 1

    # อ่านข้อมูลจากไฟล์ `jl_Game.json
    with open(api_folder + '/SW_game.json', 'r', encoding='utf-8') as json_file:
        SW_game = json.load(json_file)

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
        "url": "https://i.postimg.cc/25Kqn5c1/Bg-SW.png",
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
        game = random.choice(SW_game)
        
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
                game = random.choice(SW_game)

        message_percen = generate_unique_percentage()
        message_percen_splin = generate_unique_percen_splin()
        message_percen_game = generate_unique_percentage_game()

        bubble =    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": bg_image,
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
                "url": "https://i.postimg.cc/6Q327Z0s/the-online-casino-product-from-Advant-Play-gamingsoft.png",
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
    with open(api_folder + '/flex_message/BONUSTIME_SW.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)
    if debug:
      print(api_folder + '/flex_message/BONUSTIME_SW.json')

def BONUSTIME_WMS(api_folder):
    # ดึงเวลาปัจจุบัน
    now = datetime.now()

    # แปลงเวลาเป็นรูปแบบ "00:00"
    formatted_time = now.strftime("%H")
    # แปลงเวลาเป็น integer ก่อนที่จะบวก
    num = int(formatted_time) + 1

    # อ่านข้อมูลจากไฟล์ `jl_Game.json
    with open(api_folder + '/WMS_game.json', 'r', encoding='utf-8') as json_file:
        WMS_game = json.load(json_file)

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
    data =  {
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
        "url": "https://i.postimg.cc/CxMdt89Z/Bg-WMS.png",
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
        game = random.choice(WMS_game)
        
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
                game = random.choice(WMS_game)

        message_percen = generate_unique_percentage()
        message_percen_splin = generate_unique_percen_splin()
        message_percen_game = generate_unique_percentage_game()

        bubble =    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": bg_image,
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
                "url": "https://i.postimg.cc/YqzhbRDK/the-online-casino-product-from-Advant-Play-gamingsoft.png",
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
    with open(api_folder + '/flex_message/BONUSTIME_WMS.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)
    if debug:
      print(api_folder + '/flex_message/BONUSTIME_WMS.json')

def BONUSTIME_EXPS(api_folder):
    # ดึงเวลาปัจจุบัน
    now = datetime.now()

    # แปลงเวลาเป็นรูปแบบ "00:00"
    formatted_time = now.strftime("%H")
    # แปลงเวลาเป็น integer ก่อนที่จะบวก
    num = int(formatted_time) + 1

    # อ่านข้อมูลจากไฟล์ `jl_Game.json
    with open(api_folder + '/EXPS_game.json', 'r', encoding='utf-8') as json_file:
        EXPS_game = json.load(json_file)

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
    data =  {
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
        "url": "https://i.postimg.cc/pd94X03g/Bg-EXPS.png",
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
        game = random.choice(EXPS_game)
        
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
                game = random.choice(EXPS_game)

        message_percen = generate_unique_percentage()
        message_percen_splin = generate_unique_percen_splin()
        message_percen_game = generate_unique_percentage_game()

        bubble =    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": bg_image,
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
                "url": "https://i.postimg.cc/qqr5wpgT/the-online-casino-product-from-Advant-Play-gamingsoft.png",
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
    with open(api_folder + '/flex_message/BONUSTIME_EXPS.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)
    if debug:
      print(api_folder + '/flex_message/BONUSTIME_EXPS.json')

def BONUSTIME_BPS(api_folder):
    # ดึงเวลาปัจจุบัน
    now = datetime.now()

    # แปลงเวลาเป็นรูปแบบ "00:00"
    formatted_time = now.strftime("%H")
    # แปลงเวลาเป็น integer ก่อนที่จะบวก
    num = int(formatted_time) + 1

    # อ่านข้อมูลจากไฟล์ `jl_Game.json
    with open(api_folder + '/BPS_game.json', 'r', encoding='utf-8') as json_file:
        BPS_game = json.load(json_file)

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
    data =  {
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
        "url": "https://i.postimg.cc/g0QJnTjR/Bg-BPS.png",
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
        game = random.choice(BPS_game)
        
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
                game = random.choice(BPS_game)

        message_percen = generate_unique_percentage()
        message_percen_splin = generate_unique_percen_splin()
        message_percen_game = generate_unique_percentage_game()

        bubble =    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": bg_image,
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
                "url": "https://i.postimg.cc/fbJyWNzD/the-online-casino-product-from-Advant-Play-gamingsoft.png",
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
    with open(api_folder + '/flex_message/BONUSTIME_BPS.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)
    if debug:
      print(api_folder + '/flex_message/BONUSTIME_BPS.json')

def BONUSTIME_EDPN(api_folder):
    # ดึงเวลาปัจจุบัน
    now = datetime.now()

    # แปลงเวลาเป็นรูปแบบ "00:00"
    formatted_time = now.strftime("%H")
    # แปลงเวลาเป็น integer ก่อนที่จะบวก
    num = int(formatted_time) + 1

    # อ่านข้อมูลจากไฟล์ `jl_Game.json
    with open(api_folder + '/EDPN_game.json', 'r', encoding='utf-8') as json_file:
        EDPN_game = json.load(json_file)

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
        "url": "https://i.postimg.cc/sxy3WdrB/Bg-EDPN.png",
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
        game = random.choice(EDPN_game)
        
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
                game = random.choice(EDPN_game)

        message_percen = generate_unique_percentage()
        message_percen_splin = generate_unique_percen_splin()
        message_percen_game = generate_unique_percentage_game()

        bubble =    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": bg_image,
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
                "url": "https://i.postimg.cc/7YKq5WQ6/the-online-casino-product-from-Advant-Play-gamingsoft.png",
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
    with open(api_folder + '/flex_message/BONUSTIME_EDPN.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)
    if debug:
      print(api_folder + '/flex_message/BONUSTIME_EDPN.json')

def BONUSTIME_I8(api_folder):
    # ดึงเวลาปัจจุบัน
    now = datetime.now()

    # แปลงเวลาเป็นรูปแบบ "00:00"
    formatted_time = now.strftime("%H")
    # แปลงเวลาเป็น integer ก่อนที่จะบวก
    num = int(formatted_time) + 1

    # อ่านข้อมูลจากไฟล์ `jl_Game.json
    with open(api_folder + '/I8_game.json', 'r', encoding='utf-8') as json_file:
        I8_game = json.load(json_file)

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
        "url": "https://i.postimg.cc/tCTLMC2q/Bg-I8.png",
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
        game = random.choice(I8_game)
        
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
                game = random.choice(I8_game)

        message_percen = generate_unique_percentage()
        message_percen_splin = generate_unique_percen_splin()
        message_percen_game = generate_unique_percentage_game()

        bubble =    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": bg_image,
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
                "url": "https://i.postimg.cc/Y9zJJv59/the-online-casino-product-from-Advant-Play-gamingsoft.png",
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
    with open(api_folder + '/flex_message/BONUSTIME_I8.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)
    if debug:
      print(api_folder + '/flex_message/BONUSTIME_I8.json')

def BONUSTIME_SBOS(api_folder):
    # ดึงเวลาปัจจุบัน
    now = datetime.now()

    # แปลงเวลาเป็นรูปแบบ "00:00"
    formatted_time = now.strftime("%H")
    # แปลงเวลาเป็น integer ก่อนที่จะบวก
    num = int(formatted_time) + 1

    # อ่านข้อมูลจากไฟล์ `jl_Game.json
    with open(api_folder + '/SBOS_game.json', 'r', encoding='utf-8') as json_file:
        SBOS_game = json.load(json_file)

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
        "url": "https://i.postimg.cc/cH0zMsvN/Bg-SBOS.png",
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
        game = random.choice(SBOS_game)
        
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
                game = random.choice(SBOS_game)

        message_percen = generate_unique_percentage()
        message_percen_splin = generate_unique_percen_splin()
        message_percen_game = generate_unique_percentage_game()

        bubble =    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": bg_image,
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
                "url": "https://i.postimg.cc/Vs7hnP13/the-online-casino-product-from-Advant-Play-gamingsoft.png",
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
    with open(api_folder + '/flex_message/BONUSTIME_SBOS.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)
    if debug:
      print(api_folder + '/flex_message/BONUSTIME_SBOS.json')

def BONUSTIME_YGR(api_folder):
    # ดึงเวลาปัจจุบัน
    now = datetime.now()

    # แปลงเวลาเป็นรูปแบบ "00:00"
    formatted_time = now.strftime("%H")
    # แปลงเวลาเป็น integer ก่อนที่จะบวก
    num = int(formatted_time) + 1

    # อ่านข้อมูลจากไฟล์ `jl_Game.json
    with open(api_folder + '/YGR_game.json', 'r', encoding='utf-8') as json_file:
        YGR_game = json.load(json_file)

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
    data =  {
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
        "url": "https://i.postimg.cc/dtb4jqfS/Bg-YGR.png",
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
        game = random.choice(YGR_game)
        
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
                game = random.choice(YGR_game)

        message_percen = generate_unique_percentage()
        message_percen_splin = generate_unique_percen_splin()
        message_percen_game = generate_unique_percentage_game()

        bubble =    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": bg_image,
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
                "url": "https://i.postimg.cc/ZR5c5090/the-online-casino-product-from-Advant-Play-gamingsoft.png",
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
    with open(api_folder + '/flex_message/BONUSTIME_YGR.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)
    if debug:
      print(api_folder + '/flex_message/BONUSTIME_YGR.json')


configDefault = configparser.ConfigParser()
configDefault.read(['config.ini'])
patch = os.getenv("PATCH_DIR", configDefault.get("Config", "patch"))
folder_list = json.loads(configDefault.get("Config", "folder_list"))

for folder in folder_list:
    config = configparser.ConfigParser()
    config.read(patch + folder + '/config.ini')

    Name_Web = config['Config']['Name_Web']
    Game_List = int(config['Config']['Game_List'])
    Logo_Web = config['Config']['Logo_Web']
    Logo_menu = config['Config']['Logo_menu']
    Link_Web = config['Config']['Link_Web']
    port = config['Config']['port']
    
    print(folder + " | " + Name_Web + " | " + port)
    try:
      LotteryGuide(patch + folder)
      LOTTO(patch + folder)
      BONUSTIME(patch + folder)
      BONUSTIME_PP(patch + folder)
      BONUSTIME_AMBG(patch + folder)
      BONUSTIME_AMP(patch + folder)
      BONUSTIME_KAGM(patch + folder)
      BONUSTIME_K9(patch + folder)
      BONUSTIME_NS(patch + folder)
      BONUSTIME_SPG(patch + folder)
      BONUSTIME_RY(patch + folder)
      BONUSTIME_DGG(patch + folder)
      BONUSTIME_HK(patch + folder)
      BONUSTIME_OP(patch + folder)
      BONUSTIME_GO(patch + folder)
      BONUSTIME_R88(patch + folder)
      BONUSTIME_PG(patch + folder)
      BONUSTIME_NL(patch + folder)
      BONUSTIME_NE(patch + folder)
      BONUSTIME_MG(patch + folder)
      BONUSTIME_JL(patch + folder)
      BONUSTIME_JK(patch + folder)
      BONUSTIME_AMB(patch + folder)
      BONUSTIME_AMBS(patch + folder)
      BONUSTIME_CQ9(patch + folder)
      BONUSTIME_EVO(patch + folder)
      BONUSTIME_FKG(patch + folder)
      BONUSTIME_HBE(patch + folder)
      BONUSTIME_RTG(patch + folder)
      BONUSTIME_SMP(patch + folder)
      BONUSTIME_SXO(patch + folder)
      BONUSTIME_YGG(patch + folder)
      BONUSTIME_SN(patch + folder)
      BONUSTIME_G5(patch + folder)
      BONUSTIME_ACE333(patch + folder)
      BONUSTIME_ADP(patch + folder)
      BONUSTIME_BTG(patch + folder)
      BONUSTIME_GDY(patch + folder)
      BONUSTIME_MNP(patch + folder)
      BONUSTIME_ODG(patch + folder)
      BONUSTIME_SW(patch + folder)
      BONUSTIME_WMS(patch + folder)
      BONUSTIME_EXPS(patch + folder)
      BONUSTIME_BPS(patch + folder)
      BONUSTIME_EDPN(patch + folder)      
      BONUSTIME_I8(patch + folder)
      BONUSTIME_SBOS(patch + folder)
      BONUSTIME_YGR(patch + folder)            
      #BONUSTIME_AG(patch + folder)
      #BONUSTIME_SA(patch + folder)
      #BONUSTIME_CDG(patch + folder)
      #BONUSTIME_AE(patch + folder)
      #BONUSTIME_WM(patch + folder)
      #BONUSTIME_BG(patch + folder)
      #BONUSTIME_AB(patch + folder)
      #BONUSTIME_XPG(patch + folder)
      #BONUSTIME_WR(patch + folder)
      #BONUSTIME_MT(patch + folder)
    except Exception as e:
      print(e)
      print(patch + folder)
      sys.exit(0)
      
    if debug:
        print("\n")
    sleep(0.4)