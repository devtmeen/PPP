import pickle
import os
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

access_token = config['Config']['access_token']
channel_secret = config['Config']['channel_secret']
Link_Web = config['Config']['Link_Web']

from linebot.v3.messaging import (
    MessagingApi,
    ReplyMessageRequest,
    TextMessage,
    FlexMessage,
    FlexContainer,
    QuickReply,
    QuickReplyItem,
    MessageAction,
    URIAction,
)
from linebot.v3.webhooks import (
    MessageEvent,
)


def reply_message_text(event: MessageEvent, messageing_api: MessagingApi, text: str):
    return messageing_api.reply_message_with_http_info(
        ReplyMessageRequest(
            replyToken=event.reply_token,
            messages=[TextMessage(text=text)],
        )
    )


def reply_flex_message(event: MessageEvent, messageing_api: MessagingApi, flex_file: str,text ="TEST"):
    quick_reply = QuickReply(
        items=[
            QuickReplyItem(
                action=URIAction(label="สมัครสมาชิก", uri= Link_Web ),
                imageUrl="https://img2.pic.in.th/pic/17d09b22e8a1bbac9.png"
            ),
            QuickReplyItem(
                action=MessageAction(label="เติมเงิน", text= "/BANKING" ),
                imageUrl="https://img2.pic.in.th/pic/80750a9cc1f1f3ce7b862010b78992a4.png"
            ),
             QuickReplyItem(
                action=MessageAction(label="โปรโมชั่น", text= "/โปรโมชั่น" ),
                imageUrl="https://i.postimg.cc/59kJp7qr/pngegg.png"
            ),
             QuickReplyItem(
                action=MessageAction(label="BONUSTIME", text= "/BONUSTIME" ),
                imageUrl="https://img2.pic.in.th/pic/4e9c36755ea0d1244.png"
            ),
             QuickReplyItem(
                action=URIAction(label="ติดต่อแอดมิน", uri= Link_Web ),
                imageUrl="https://img5.pic.in.th/file/secure-sv1/38a2144a0729bebc5.png"
            ),
        ]
    )
    return messageing_api.reply_message_with_http_info(
        ReplyMessageRequest(
            replyToken=event.reply_token,
            messages=[ 
                FlexMessage(altText="BONUSTIME", contents=FlexContainer.from_json(
                loading_flex_content(flex_file))
                ), 
                TextMessage(text=text,
                quick_reply=quick_reply,
                 )
                ],
        )
    )


def detect_command(command: str) -> bool: return len(command.split('/')) == 2 if '/' in command else False
    
def register_flex_command(): pickle.dump([{"filename": f, "command": f.split(".")[0]} for f in os.listdir('./flex_message') if os.path.isfile(os.path.join('./flex_message', f)) and "_c" not in f], open('./flex_command.pkl', 'wb'))

def loading_flex_command(): return [f'/{r["command"]}' for r in pickle.load(open('./flex_command.pkl', 'rb'))]

def loading_flex_content(flex_file):
    with open(f'./flex_message/{flex_file}', 'r', encoding='utf-8') as file:
        return file.read()

