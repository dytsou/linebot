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
    UnfollowEvent,
    TemplateSendMessage, 
    ImageCarouselTemplate, 
    ImageCarouselColumn, 
    PostbackAction,
    PostbackEvent,
    FlexSendMessage,
    QuickReply,
    QuickReplyButton,
    MessageAction,
)

line_bot_api = LineBotApi('fPzcWsxdrtZiGB9HJ2JtTAcDbxgeGZWp+dxmrh7VgFTzUItPE6MjDjaP8K7uRM0KZRIJN+kAZyXFrBoFwc2gHP6MogNU3c5PMJjmjcH5NMbHw92ZLvPu5BfU2oWHx9b2pJDfV4/ZuyPxH/0Q61UcbgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('d4c3581384cbbe2b90f6298ec3cac353')