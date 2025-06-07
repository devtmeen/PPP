import configparser
from datetime import datetime, date

# อ่านค่าจากไฟล์ config.ini
config = configparser.ConfigParser()
config.read('config.ini')

# ดึงค่า Name_Web และ Game_List จาก config
access_token = config['Config']['access_token']
channel_secret = config['Config']['channel_secret']
expired = config['Config']['expired']

import json
from flask import Flask, request, abort

from linebot.v3 import (
    WebhookHandler
)
from linebot.v3.exceptions import (
    InvalidSignatureError
)
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
)
from linebot.v3.webhooks import (
    MessageEvent,
    TextMessageContent
)
from linebot.v3.messaging.models import ShowLoadingAnimationRequest

from util import register_flex_command, loading_flex_command, detect_command, reply_message_text, reply_flex_message

app = Flask(__name__)

configuration = Configuration(
    access_token=access_token)
handler = WebhookHandler(channel_secret)


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    # app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        app.logger.info(
            "Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'
    
@handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event: MessageEvent):
    is_command = detect_command(event.message.text)
    if not is_command:
        return

    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        loading_request = ShowLoadingAnimationRequest(
            chat_id=event.source.user_id,
            loading_seconds=20
        )
        line_bot_api.show_loading_animation(loading_request)
        cmd = event.message.text
        command = loading_flex_command()
        for c in command:
            match cmd:
                case "/test":
                    reply_message_text(event, line_bot_api,"@@@Test text command.")
                    return
                case c:
                    now = datetime.now()
                    CurrentDate = now.strftime("%d-%m-%Y %H:%M:%S")
                    ExpiredDate = expired.format(datetime.now())
                    if CurrentDate >= ExpiredDate:
                        return
                    if cmd not in command:
                        reply_message_text(event, line_bot_api, "Not found this command.")
                        return
                    if cmd =="/BONUSTIME_AMP":
                        reply_flex_message(event, line_bot_api, f"{c.replace('/', '')}.json","4 เกมค่าย Askmeplay ที่มียอดถอนสูงที่สุดในชั่วโมงนี้")
                        return 0
                    if cmd =="/BANKING":
                        reply_flex_message(event, line_bot_api, f"{c.replace('/', '')}.json","กดปุ่มเพื่อคัดลอกเลขบัญชี กรุณาตรวจสอบบัญชีก่อนทำธุรกรรม")
                        return 0
                    if cmd =="/BONUSTIME_AMBG":
                        reply_flex_message(event, line_bot_api, f"{c.replace('/', '')}.json","4 เกมค่าย Ambgaming ที่มียอดถอนสูงที่สุดในชั่วโมงนี้")
                        return 0
                    if cmd =="/BONUSTIME_NS":
                        reply_flex_message(event, line_bot_api, f"{c.replace('/', '')}.json","4 เกมค่าย Nextspin ที่มียอดถอนสูงที่สุดในชั่วโมงนี้")
                        return 0
                    if cmd =="/BONUSTIME_KAGM":
                        reply_flex_message(event, line_bot_api, f"{c.replace('/', '')}.json","4 เกมค่าย KA Gaming ที่มียอดถอนสูงที่สุดในชั่วโมงนี้")
                        return 0
                    if cmd =="/BONUSTIME_K9":
                        reply_flex_message(event, line_bot_api, f"{c.replace('/', '')}.json","4 เกมค่าย 918kiss ที่มียอดถอนสูงที่สุดในชั่วโมงนี้")
                        return 0
                    if cmd =="/BONUSTIME_SPG":
                        reply_flex_message(event, line_bot_api, f"{c.replace('/', '')}.json","4 เกมค่าย Spadegaming ที่มียอดถอนสูงที่สุดในชั่วโมงนี้")
                        return 0
                    if cmd =="/FOOTBALL":
                        reply_flex_message(event, line_bot_api, f"{c.replace('/', '')}.json","5 คู่ที่น่าสนใจในวันนี้")
                        return 0      
                    if cmd =="/BONUSTIME_PG":
                        reply_flex_message(event, line_bot_api, f"{c.replace('/', '')}.json","4 เกมค่าย PG Soft ที่มียอดถอนสูงที่สุดในชั่วโมงนี้")
                        return 0
                    if cmd =="/BONUSTIME_GO":
                        reply_flex_message(event, line_bot_api, f"{c.replace('/', '')}.json","4 เกมค่าย Play n Go ที่มียอดถอนสูงที่สุดในชั่วโมงนี้")
                        return 0
                    if cmd =="/BONUSTIME_OP":
                        reply_flex_message(event, line_bot_api, f"{c.replace('/', '')}.json","4 เกมค่าย Octoplay ที่มียอดถอนสูงที่สุดในชั่วโมงนี้")
                        return 0
                    if cmd =="/BONUSTIME_R88":
                        reply_flex_message(event, line_bot_api, f"{c.replace('/', '')}.json","4 เกมค่าย R88 ที่มียอดถอนสูงที่สุดในชั่วโมงนี้")
                        return 0
                    if cmd =="/BONUSTIME_RY":
                        reply_flex_message(event, line_bot_api, f"{c.replace('/', '')}.json","4 เกมค่าย Royal Slot ที่มียอดถอนสูงที่สุดในชั่วโมงนี้")
                        return 0
                    if cmd =="/BONUSTIME_HK":
                        reply_flex_message(event, line_bot_api, f"{c.replace('/', '')}.json","4 เกมค่าย Hacksaw ที่มียอดถอนสูงที่สุดในชั่วโมงนี้")
                        return 0
                    if cmd =="/BONUSTIME_DGG":
                        reply_flex_message(event, line_bot_api, f"{c.replace('/', '')}.json","4 เกมค่าย Dragongaming ที่มียอดถอนสูงที่สุดในชั่วโมงนี้")
                        return 0
                    elif cmd =="/BONUSTIME":
                        reply_flex_message(event, line_bot_api, f"{c.replace('/', '')}.json","เลือกค่ายเกมที่ต้องการเช็คอัตราการชนะ")
                        return 0
                    elif cmd =="/BONUSTIME_PP":
                        reply_flex_message(event, line_bot_api, f"{c.replace('/', '')}.json","4 เกมค่าย Pragmatic ที่มียอดถอนสูงที่สุดในชั่วโมงนี้")
                        return 0      
                    elif cmd =="/BONUSTIME_JK":
                        reply_flex_message(event, line_bot_api, f"{c.replace('/', '')}.json","4 เกมค่าย Joker ที่มียอดถอนสูงที่สุดในชั่วโมงนี้")
                        return 0
                    elif cmd =="/BONUSTIME_MG":
                        reply_flex_message(event, line_bot_api, f"{c.replace('/', '')}.json","4 เกมค่าย Microgaming ที่มียอดถอนสูงที่สุดในชั่วโมงนี้")
                        return 0 
                    elif cmd =="/BONUSTIME_JL":
                        reply_flex_message(event, line_bot_api, f"{c.replace('/', '')}.json","4 เกมค่าย Jili ที่มียอดถอนสูงที่สุดในชั่วโมงนี้")
                        return 0 
                    elif cmd =="/BONUSTIME_SN":
                        reply_flex_message(event, line_bot_api, f"{c.replace('/', '')}.json","4 เกมค่าย Spinix ที่มียอดถอนสูงที่สุดในชั่วโมงนี้")
                        return 0 
                    elif cmd =="/BONUSTIME_NE":
                        reply_flex_message(event, line_bot_api, f"{c.replace('/', '')}.json","4 เกมค่าย Netent ที่มียอดถอนสูงที่สุดในชั่วโมงนี้")
                        return 0 
                    elif cmd =="/BONUSTIME_NL":
                        reply_flex_message(event, line_bot_api, f"{c.replace('/', '')}.json","4 เกมค่าย Nolimit ที่มียอดถอนสูงที่สุดในชั่วโมงนี้")
                        return 0 
                    elif cmd =="/BONUSTIME_AMB":
                        reply_flex_message(event, line_bot_api, f"{c.replace('/', '')}.json","4 เกมค่าย Askmebet ที่มียอดถอนสูงที่สุดในชั่วโมงนี้")
                        return 0 
                    elif cmd =="/BONUSTIME_AMBS":
                        reply_flex_message(event, line_bot_api, f"{c.replace('/', '')}.json","4 เกมค่าย Askmeslot ที่มียอดถอนสูงที่สุดในชั่วโมงนี้")
                        return 0 
                    elif cmd =="/BONUSTIME_CQ9":
                        reply_flex_message(event, line_bot_api, f"{c.replace('/', '')}.json","4 เกมค่าย CQ9 ที่มียอดถอนสูงที่สุดในชั่วโมงนี้")
                        return 0 
                    elif cmd =="/BONUSTIME_EVO":
                        reply_flex_message(event, line_bot_api, f"{c.replace('/', '')}.json","4 เกมค่าย Evoplay ที่มียอดถอนสูงที่สุดในชั่วโมงนี้")
                        return 0 
                    elif cmd =="/BONUSTIME_RTG":
                        reply_flex_message(event, line_bot_api, f"{c.replace('/', '')}.json","4 เกมค่าย RED TIGER ที่มียอดถอนสูงที่สุดในชั่วโมงนี้")
                        return 0 
                    elif cmd =="/BONUSTIME_HBE":
                        reply_flex_message(event, line_bot_api, f"{c.replace('/', '')}.json","4 เกมค่าย Habanerd ที่มียอดถอนสูงที่สุดในชั่วโมงนี้")
                        return 0 
                    elif cmd =="/BONUSTIME_FKG":
                        reply_flex_message(event, line_bot_api, f"{c.replace('/', '')}.json","4 เกมค่าย FUNKY ที่มียอดถอนสูงที่สุดในชั่วโมงนี้")
                        return 0 
                    elif cmd =="/BONUSTIME_YGG":
                        reply_flex_message(event, line_bot_api, f"{c.replace('/', '')}.json","4 เกมค่าย YGGDRASIL ที่มียอดถอนสูงที่สุดในชั่วโมงนี้")
                        return 0 
                    elif cmd =="/BONUSTIME_SXO":
                        reply_flex_message(event, line_bot_api, f"{c.replace('/', '')}.json","4 เกมค่าย SlotXO ที่มียอดถอนสูงที่สุดในชั่วโมงนี้")
                        return 0 
                    elif cmd =="/BONUSTIME_SMP":
                        reply_flex_message(event, line_bot_api, f"{c.replace('/', '')}.json","4 เกมค่าย SIMPLE PLAY ที่มียอดถอนสูงที่สุดในชั่วโมงนี้")
                        return 0 
                    elif cmd =="/BONUSTIME_AG":
                        reply_flex_message(event, line_bot_api, f"{c.replace('/', '')}.json","5 ห้องค่าย AG ที่มียอดถอนสูงที่สุดในชั่วโมงนี้")
                        return 0 
                    elif cmd =="/BONUSTIME_CDG":
                        reply_flex_message(event, line_bot_api, f"{c.replace('/', '')}.json","5 ห้องค่าย Dream Gaming ที่มียอดถอนสูงที่สุดในชั่วโมงนี้")
                        return 0 
                    elif cmd =="/BONUSTIME_SA":
                        reply_flex_message(event, line_bot_api, f"{c.replace('/', '')}.json","5 ห้องค่าย SA Gaming ที่มียอดถอนสูงที่สุดในชั่วโมงนี้")
                        return 0 
                    elif cmd =="/BONUSTIME_AE":
                        reply_flex_message(event, line_bot_api, f"{c.replace('/', '')}.json","5 ห้องค่าย AE Sexy ที่มียอดถอนสูงที่สุดในชั่วโมงนี้")
                        return 0 
                    elif cmd =="/BONUSTIME_WM":
                        reply_flex_message(event, line_bot_api, f"{c.replace('/', '')}.json","5 ห้องค่าย WM ที่มียอดถอนสูงที่สุดในชั่วโมงนี้")
                        return 0 
                    elif cmd =="/BONUSTIME_BG":
                        reply_flex_message(event, line_bot_api, f"{c.replace('/', '')}.json","5 ห้องค่าย Big Gaming ที่มียอดถอนสูงที่สุดในชั่วโมงนี้")
                        return 0 
                    elif cmd =="/BONUSTIME_AB":
                        reply_flex_message(event, line_bot_api, f"{c.replace('/', '')}.json","5 ห้องค่าย Allbet ที่มียอดถอนสูงที่สุดในชั่วโมงนี้")
                        return 0 
                    elif cmd =="/BONUSTIME_XPG":
                        reply_flex_message(event, line_bot_api, f"{c.replace('/', '')}.json","5 ห้องค่าย XPG ที่มียอดถอนสูงที่สุดในชั่วโมงนี้")
                        return 0 
                    elif cmd =="/BONUSTIME_WR":
                        reply_flex_message(event, line_bot_api, f"{c.replace('/', '')}.json","5 ห้องค่าย WR ที่มียอดถอนสูงที่สุดในชั่วโมงนี้")
                        return 0 
                    elif cmd =="/BONUSTIME_MT":
                        reply_flex_message(event, line_bot_api, f"{c.replace('/', '')}.json","5 ห้องค่าย MT ที่มียอดถอนสูงที่สุดในชั่วโมงนี้")
                        return 0
                    
                    
                    elif cmd =="/BONUSTIME_G5":
                        reply_flex_message(event, line_bot_api, f"{c.replace('/', '')}.json","4 เกมค่าย 5G Games ที่มียอดถอนสูงที่สุดในชั่วโมงนี้")
                        return 0
                    elif cmd =="/BONUSTIME_ACE333":
                        reply_flex_message(event, line_bot_api, f"{c.replace('/', '')}.json","4 เกมค่าย ACE333 ที่มียอดถอนสูงที่สุดในชั่วโมงนี้")
                        return 0                    
                    elif cmd =="/BONUSTIME_ADP":
                        reply_flex_message(event, line_bot_api, f"{c.replace('/', '')}.json","4 เกมค่าย Advantplay ที่มียอดถอนสูงที่สุดในชั่วโมงนี้")
                        return 0                    
                    elif cmd =="/BONUSTIME_BTG":
                        reply_flex_message(event, line_bot_api, f"{c.replace('/', '')}.json","4 เกมค่าย BT Gaming ที่มียอดถอนสูงที่สุดในชั่วโมงนี้")
                        return 0                    
                    elif cmd =="/BONUSTIME_EXPS":
                        reply_flex_message(event, line_bot_api, f"{c.replace('/', '')}.json","4 เกมค่าย The Expanse ที่มียอดถอนสูงที่สุดในชั่วโมงนี้")
                        return 0
                    elif cmd =="/BONUSTIME_GDY":
                        reply_flex_message(event, line_bot_api, f"{c.replace('/', '')}.json","4 เกมค่าย Goldy ที่มียอดถอนสูงที่สุดในชั่วโมงนี้")
                        return 0
                    elif cmd =="/BONUSTIME_MNP":
                        reply_flex_message(event, line_bot_api, f"{c.replace('/', '')}.json","4 เกมค่าย MannaPlay ที่มียอดถอนสูงที่สุดในชั่วโมงนี้")
                        return 0                    
                    elif cmd =="/BONUSTIME_ODG":
                        reply_flex_message(event, line_bot_api, f"{c.replace('/', '')}.json","4 เกมค่าย Odin Gaming ที่มียอดถอนสูงที่สุดในชั่วโมงนี้")
                        return 0                    
                    elif cmd =="/BONUSTIME_SW":
                        reply_flex_message(event, line_bot_api, f"{c.replace('/', '')}.json","4 เกมค่าย Skywind ที่มียอดถอนสูงที่สุดในชั่วโมงนี้")
                        return 0                    
                    elif cmd =="/BONUSTIME_WMS":
                        reply_flex_message(event, line_bot_api, f"{c.replace('/', '')}.json","4 เกมค่าย WMSlot ที่มียอดถอนสูงที่สุดในชั่วโมงนี้")
                        return 0
                    elif cmd =="/BONUSTIME_BPS":
                        reply_flex_message(event, line_bot_api, f"{c.replace('/', '')}.json","4 เกมค่าย BigPot ที่มียอดถอนสูงที่สุดในชั่วโมงนี้")
                        return 0
                    elif cmd =="/BONUSTIME_EDPN":
                        reply_flex_message(event, line_bot_api, f"{c.replace('/', '')}.json","4 เกมค่าย ES ที่มียอดถอนสูงที่สุดในชั่วโมงนี้")
                        return 0                    
                    elif cmd =="/BONUSTIME_I8":
                        reply_flex_message(event, line_bot_api, f"{c.replace('/', '')}.json","4 เกมค่าย I8 ที่มียอดถอนสูงที่สุดในชั่วโมงนี้")
                        return 0                    
                    elif cmd =="/BONUSTIME_SBOS":
                        reply_flex_message(event, line_bot_api, f"{c.replace('/', '')}.json","4 เกมค่าย SBO Slot ที่มียอดถอนสูงที่สุดในชั่วโมงนี้")
                        return 0                    
                    elif cmd =="/BONUSTIME_YGR":
                        reply_flex_message(event, line_bot_api, f"{c.replace('/', '')}.json","4 เกมค่าย YGR ที่มียอดถอนสูงที่สุดในชั่วโมงนี้")
                        return 0                                                                                                                                                           
                    elif cmd =="/หวยรัฐบาล":
                        reply_flex_message(event, line_bot_api, f"{c.replace('/', '')}.json","ตรวจหวยรัฐบาล ผลหวยรัฐบาลวันนี้")
                        return 0 
                    elif cmd =="/หวยลาว":
                        reply_flex_message(event, line_bot_api, f"{c.replace('/', '')}.json","ตรวจหวยลาว ผลหวยลาววันนี้")
                        return 0 
                    elif cmd =="/หวยหุ้น":
                        reply_flex_message(event, line_bot_api, f"{c.replace('/', '')}.json","ตรวจหวยหุ้น ผลหวยหุ้นวันนี้")
                        return 0 
                    elif cmd =="/หวยธกส":
                        reply_flex_message(event, line_bot_api, f"{c.replace('/', '')}.json","ตรวจหวยธกส ผลหวยธกสวันนี้")
                        return 0 
                    elif cmd =="/หวยออมสิน":
                        reply_flex_message(event, line_bot_api, f"{c.replace('/', '')}.json","ตรวจหวยออมสิน ผลหวยออมสินวันนี้")
                        return 0 
                    elif cmd =="/หวยฮานอย":
                        reply_flex_message(event, line_bot_api, f"{c.replace('/', '')}.json","ตรวจหวยฮานอย ผลหวยฮานอยวันนี้")
                        return 0
                    elif cmd =="/LOTTO":
                        reply_flex_message(event, line_bot_api, f"{c.replace('/', '')}.json","เลือกหวยที่ต้องการจะเช็ค")
                        return 0
                    elif cmd =="/แนวทางหวย":
                        reply_flex_message(event, line_bot_api, f"{c.replace('/', '')}.json","เลือกหวยที่ต้องการดูเลขเด็ด")
                        return 0    
                    elif cmd =="/THAILOTTOS":
                        reply_flex_message(event, line_bot_api, f"{c.replace('/', '')}.json","ขอให้ลูกค้าทุกท่านรวยๆ เฮงๆนะคะ")
                        return 0             
                    elif cmd =="/GSBLOTTOS":
                        reply_flex_message(event, line_bot_api, f"{c.replace('/', '')}.json","ขอให้ลูกค้าทุกท่านรวยๆ เฮงๆนะคะ")
                        return 0 
                    elif cmd =="/LAOLOTTOS":
                        reply_flex_message(event, line_bot_api, f"{c.replace('/', '')}.json","ขอให้ลูกค้าทุกท่านรวยๆ เฮงๆนะคะ")
                        return 0 
                    elif cmd =="/YEEKEELOTTOS":
                        reply_flex_message(event, line_bot_api, f"{c.replace('/', '')}.json","ขอให้ลูกค้าทุกท่านรวยๆ เฮงๆนะคะ")
                        return 0 
                    elif cmd =="/HANOILOTTOS":
                        reply_flex_message(event, line_bot_api, f"{c.replace('/', '')}.json","ขอให้ลูกค้าทุกท่านรวยๆ เฮงๆนะคะ")
                        return 0             
                    elif cmd =="/HANOINORMALLOTTOS":
                        reply_flex_message(event, line_bot_api, f"{c.replace('/', '')}.json","ขอให้ลูกค้าทุกท่านรวยๆ เฮงๆนะคะ")
                        return 0 
                    elif cmd =="/HANOISPECIALLOTTOS":
                        reply_flex_message(event, line_bot_api, f"{c.replace('/', '')}.json","ขอให้ลูกค้าทุกท่านรวยๆ เฮงๆนะคะ")
                        return 0 
                    elif cmd =="/วิเคราะห์บอลสด":
                        reply_flex_message(event, line_bot_api, f"{c.replace('/', '')}.json","วิเคราะห์บอลสดประจำวันนี้")
                        return 0 
                    elif cmd =="/โปรโมชั่น":
                        reply_flex_message(event, line_bot_api, f"{c.replace('/', '')}.json","เลือกโปรโมชั่นที่คุณสนใจ")
                        return 0 
                    elif cmd =="/HANOIVIPLOTTOS":
                        reply_flex_message(event, line_bot_api, f"{c.replace('/', '')}.json","ขอให้ลูกค้าทุกท่านรวยๆ เฮงๆนะคะ")
                        return 0                                   
                    reply_flex_message(event, line_bot_api, f"{c.replace('/', '')}.json",cmd)
                    return

if __name__ == "__main__":
    register_flex_command()
    app.run("0.0.0.0", config['Config']['port'], debug=True)

