from telegram import *
from telegram.ext import *
from constants import *
from .texts import *

class YouTube:

    def initialize(self, update:Update, context:CallbackContext):
        user = update.message.from_user
        db_user = db.get_user(user.id)
        print(db_user)
        update.message.reply_text(SEND_YOU_TUBE_URL_MESSAGE_TEXT[db_user['language']])