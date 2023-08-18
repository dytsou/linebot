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
    StickerSendMessage
)

app = Flask(__name__)

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
        line_bot_api.reply_message( # 回覆訊息
            event.reply_token,
            [text_message, sticker_message]
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

if __name__ == "__main__":
    app.run()