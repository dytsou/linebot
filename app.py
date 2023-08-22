from flask import Flask, request, abort

from linebot import (
    LineBotApi,
    WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent,
    TextMessage,
    TextSendMessage,
    StickerSendMessage,
    ImageSendMessage,
    LocationSendMessage,
    FollowEvent,
    UnfollowEvent
)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://dytsou:dyt50u@127.0.0.1:5432/linebot0820'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from extensions import migrate, db
db.app = app
db.init_app(app)
migrate.init_app(app, db)

from models.user import User

line_bot_api = LineBotApi('fPzcWsxdrtZiGB9HJ2JtTAcDbxgeGZWp+dxmrh7VgFTzUItPE6MjDjaP8K7uRM0KZRIJN+kAZyXFrBoFwc2gHP6MogNU3c5PMJjmjcH5NMbHw92ZLvPu5BfU2oWHx9b2pJDfV4/ZuyPxH/0Q61UcbgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('d4c3581384cbbe2b90f6298ec3cac353')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        app.logger.info("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message_text = str(event.message.text).lower()
    if message_text == '@about': # 關鍵字
        emoji = [ # 貼圖
            {
                "index": 0, # 第幾個字元
                "productId": "5ac1bfd5040ab15980c9b435", # 貼圖包ID
                "emojiId": "001" # 貼圖ID
            },
            {
                "index": 12, # 第幾個字元
                "productId": "5ac1bfd5040ab15980c9b435", # 貼圖包ID
                "emojiId": "002" # 貼圖ID
            },
        ]
        text_message = TextMessage(text="$歡迎使用linebot$", emojis=emoji) # 回覆文字
        sticker_message = StickerSendMessage( # 回覆貼圖
            package_id='446', # 貼圖包ID
            sticker_id='1988' # 貼圖ID
        )
        ithome_logo_url = 'https://s4.itho.me/sites/default/files/images/ithome_logo.png'
        image_message = ImageSendMessage(
        original_content_url=ithome_logo_url,
        preview_image_url=ithome_logo_url
        )
        line_bot_api.reply_message( # 回覆訊息
            event.reply_token,
            [text_message, sticker_message, image_message]
        )
    elif message_text == '@location':
        location_message = LocationSendMessage(
            title='NYCU',
            address='30010新竹市東區大學路1001號',
            latitude=24.7868862,
            longitude=120.994922
            )
        line_bot_api.reply_message(
            event.reply_token,
            location_message
        )
    else:
        emoji = [
            {
                "index": 0,
                "productId": "5ac21a18040ab15980c9b43e",
                "emojiId": "014"
            }, 
        ]
        emoji_text = TextMessage(text="$", emojis=emoji)
        text_message = TextMessage(text=event.message.text)
        line_bot_api.reply_message( 
            event.reply_token,
            [emoji_text, text_message]
        )

@handler.add(UnfollowEvent)
def handle_unfollow(event):
    print(event)

@handler.add(FollowEvent)
def handle_follow(event):
    print(event)
    welcome_message = TextSendMessage(text='Hello! User ' + event.source.user_id)
    line_bot_api.push_message(
        event.source.user_id,
        welcome_message
    )

if __name__ == "__main__":
    app.run()