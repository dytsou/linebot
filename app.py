from flask import Flask, request, abort
from linebotAPI import *
from sql import check_user_info
from extensions import migrate, db
from events_basic import about_event, location_event, other_event
from events_service import *
from urllib.parse import parse_qsl

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://dytsou:dyt50u@127.0.0.1:5432/linebot0824'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.app = app
db.init_app(app)
migrate.init_app(app, db)


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
    check_user_info(event)
    
    if message_text == '@about': # 關鍵字
        about_event(event)
    elif message_text == '@location':
        location_event(event)
    elif message_text == '@service':
        service_category_event(event)
    # elif message_text == '@appointment':
    #     service_appointment_event(event)
    else:
        other_event(event)

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

@handler.add(PostbackEvent)
def handle_postback(event):
    data = dict(parse_qsl(event.postback.data))
    print(data['action'])
    print(data['itemid'])    

@handler.add(PostbackEvent)
def handle_postback(event):
    data = dict(parse_qsl(event.postback.data))
    if data.get('action') == 'service_category':
        service_event(event)
    # elif data.get('action') == 'select_date':
    #     service_select_event(event)
    # elif data.get('action') == 'select_time':
    #     service_select_time_event(event)

    # print('date:', data.get('date'))
    # print('time:', data.get('time'))
    print('action:', data.get('action'))
    print('itemid:', data.get('itemid'))
    


if __name__ == "__main__":
    app.run()