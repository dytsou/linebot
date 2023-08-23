from flask import Flask, request, abort
from linebotAPI import *
from extensions import migrate, db
from models.user import User
from events_basic import about_event, location_event, other_event


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://dytsou:dyt50u@127.0.0.1:5432/linebot0820'
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
    user = User.query.filter(User.line_id == event.source.user_id).first() # 查詢使用者是否存在
    # print(event.source.user_id) 
    if not user:
        profile = line_bot_api.get_profile(event.source.user_id) # 取得使用者資料
        # print(profile.display_name)
        # print(profile.user_id)
        # print(profile.picture_url)
        # print(profile.status_message)
        new_user = User(profile.user_id, profile.display_name, profile.picture_url) # 建立新使用者
        db.session.add(new_user) # 新增使用者到資料庫
        db.session.commit() # 儲存
    
    if message_text == '@about': # 關鍵字
        about_event(event)
    elif message_text == '@location':
        location_event(event)
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

if __name__ == "__main__":
    app.run()