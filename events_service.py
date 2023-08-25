from linebotAPI import *
from url import *
from urllib.parse import parse_qsl
from datetime import datetime, timedelta, date, time

def service_category_event(event):
    image_carousel_template_message = TemplateSendMessage(
        alt_text='服務類別',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url=fb_icon(),
                    action=PostbackAction(
                        label='fb網頁設計',
                        display_text='fb網頁設計',
                        data='action=service_category&itemid=1'
                    )
                ),
                ImageCarouselColumn(
                    image_url=ig_icon(),
                    action=PostbackAction(
                        label='ig網頁設計',
                        display_text='ig網頁設計',
                        data='action=service_category&itemid=2'
                    )
                ),
                ImageCarouselColumn(
                    image_url=twitter_icon(),
                    action=PostbackAction(
                        label='twitter網頁設計',
                        display_text='twitter網頁設計',
                        data='action=service_category&itemid=3'
                    )
                ),
            ]
        )
    )
    line_bot_api.reply_message(
        event.reply_token,
        image_carousel_template_message
    )
"""
def service_appointment_event(event):
    image_carousel_template_message = TemplateSendMessage(
        alt_text='預約服務',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url=google_calendar_icon(),
                    action=PostbackAction(
                        label='預約日期',
                        display_text='預約日期',
                        data='action=select_date&itemid=4'
                    )
                ),
                ImageCarouselColumn(
                    image_url=google_clock_icon(),
                    action=PostbackAction(
                        label='預約時間', 
                        display_text='預約時間',
                        data='action=select_time&itemid=5'
                    )
                ),
            ]
        )
    )
    line_bot_api.reply_message(
        event.reply_token,
        image_carousel_template_message
    )
"""   


def service_event(event):
    flex_message = FlexSendMessage(
        alt_text='hello',
        contents={
            "type": "bubble",
            "direction": "ltr",
            "header": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "BEST SUGGESTION",
                        "size": "lg",
                        "align": "center",
                        "weight": "bold"
                    }
                ]
            },
            "hero": {
                "type": "image",
                "url": chatgpt_icon(),
                "size": "full",
                "aspect_ratio": "16:9"
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "ChatGPT can help you.",
                        "align": "center",
                        "wrap": True
                    }
                ]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "contents": [
                    {
                        "type": "button",
                        "action": {
                            "type": "uri",
                            "label": "ChatGPT",
                            "uri": "https://chat.openai.com/"
                        }
                    },
                ]
            }
        }
    )
    line_bot_api.reply_message(
        event.reply_token,
        [flex_message]
    )

"""
def service_select_event(event):
    data = dict(parse_qsl(event.postback.data))
    quick_reply_buttons = []
    today = datetime.datetime.today().date()

    for x in range(1, 8):
        day = today + datetime.today(days=x)

    quick_reply_button = QuickReplyButton(
        action=PostbackAction(
                    label=f'{day}',
                    text=f'I would like to make an appointment for the day of {day}',
                    data=f'action=select_time&service_id={data["service_id"]}&data={data}'
                    )
    )
    quick_reply_button.append(quick_reply_button)

    text_message = TextSendMessage(
                        text='Hello, world',
                        quick_reply=QuickReply(
                                        items=[
                                            QuickReplyButton(
                                                action=MessageAction(label="label", text="text")
                                            )
                                        ]
                                    )
                                )
    line_bot_api.reply_message(
        event.reply_token,
        [text_message]
    )


def service_select_time_event(event):
    data = dict(parse_qsl(event.postback.data))
    quick_reply_buttons = []
    book_time = ['09:00', '11:00', '13:00', '15:00', '17:00']
    for time in book_time:
        quick_reply_button = QuickReplyButton(action=PostbackAction(label=time,
                                                                    text=f'{time} this time',
                                                                    data=f'action=confirm&service_id={data["service_id"]}&date={data["date"]}&time={time}'))
        quick_reply_buttons.append(quick_reply_button)
    text_message = TextSendMessage(text='Hello, world',
                                quick_reply=QuickReply(items=quick_reply_buttons))
    line_bot_api.reply_message(
        event.reply_token,
        [text_message]
    )
"""

