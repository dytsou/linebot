from models.user import User 
from linebotAPI import *
from extensions import db

def check_user_info(event):
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