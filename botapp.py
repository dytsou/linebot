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
    ReplyMessageRequest,
    TextMessage
)
from linebot.v3.webhooks import (
    MessageEvent,
    TextMessageContent
)

app = Flask(__name__)

configuration = Configuration(access_token='fPzcWsxdrtZiGB9HJ2JtTAcDbxgeGZWp+dxmrh7VgFTzUItPE6MjDjaP8K7uRM0KZRIJN+kAZyXFrBoFwc2gHP6MogNU3c5PMJjmjcH5NMbHw92ZLvPu5BfU2oWHx9b2pJDfV4/ZuyPxH/0Q61UcbgdB04t89/1O/w1cDnyilFU=')
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


@handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event):
    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        message_text = str(event.message.text).lower()
        if message_text == '@about':
            emoji = [
                {
                    "index": 0,
                    "productId": "5ac1bfd5040ab15980c9b435",
                    "emojiId": "001"
                },
                {
                    "index": 13,
                    "productId": "5ac1bfd5040ab15980c9b435",
                    "emojiId": "002"
                },
            ]
        text_message = TextMessage(text="$歡迎使用linebot $",emojis=emoji)
        line_bot_api.reply_message_with_http_info(
            ReplyMessageRequest(
                reply_token=event.reply_token,
                messages=[text_message]
            )
        )

if __name__ == "__main__":
    app.run()