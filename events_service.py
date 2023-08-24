from linebotAPI import *
from url import *

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


