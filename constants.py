from db import Db
from telegram import *
from telegram.ext import *
TOKEN = "5074156811:AAHbf9tlMvTI5OF92mboIKriDNCG54W_9FY"

db = Db('users.db')

language_keyboards: ReplyKeyboardMarkup = ReplyKeyboardMarkup([["🇺🇿 o'zbek tili", "🇷🇺 русский"], ["🇺🇸 english"]],
                                                              resize_keyboard=True)

LANGUAGE, MENU = range(2)
uz_lang = "🇺🇿 o'zbek tili"
ru_lang = "🇷🇺 русский"
en_lang = "🇺🇸 english"


