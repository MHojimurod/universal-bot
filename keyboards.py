from telegram import *
from telegram.ext import *
def menu_keyboards(language:int) -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup([
        ["📹 YouTube"]
    ])