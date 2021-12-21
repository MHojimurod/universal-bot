from telegram import *
from telegram.ext import *
from constants import *
from .texts import *
from pytube import YouTube as Yt
from pytube.exceptions import RegexMatchError
class YouTube:

    def initialize(self, update:Update, context:CallbackContext):
        user = update.message.from_user
        db_user = db.get_user(user.id)
        print(db_user)
        update.message.reply_text(SEND_YOU_TUBE_URL_MESSAGE_TEXT[db_user['language']])
        return YOU_TUBE_GET_URL_OR_ID

    def get_url_or_id(self,update:Update, context:CallbackContext):
        user = update.message.from_user
        db_user = db.get_user(user.id)
        url = update.message.text
        try:
            yt = Yt(url)
        except RegexMatchError:
            update.message.reply_text(URL_NOT_MATCH[db_user['language']])
            return
        else:
            print(yt)