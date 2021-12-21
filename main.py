from telegram import *
from telegram.ext import *
from constants import (TOKEN)


class Bot(Updater):
    def __init__(self):
        super(Bot, self).__init__(TOKEN)

    def start(self, update:Update, context:CallbackContext):
        user = update.message.from_user
        
    
    def run(self):
        self.start_polling()
        self.idle()