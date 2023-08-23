from flask import Flask, request, abort

from linebotAPI import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://dytsou:dyt50u@127.0.0.1:5432/linebot0820'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

def about_event(event):
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

def location_event(event):
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

def other_event(event):
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