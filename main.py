from telegram import *
from telegram.ext import *
from constants import (TOKEN, db, language_keyboards, LANGUAGE, MENU, uz_lang, ru_lang, en_lang)
from youtube import YouTube
from texts import SUCCESSFULLY_REGISTERED, MAIN_MENU_TEXT
from keyboards import menu_keyboards


class Bot(Updater):
    def __init__(self):
        super(Bot, self).__init__(TOKEN)
        self.YouTube = YouTube()
        self.dispatcher.add_handler(ConversationHandler(
            entry_points=[
                CommandHandler('start', self.start)
            ],
            states={
                MENU: [MessageHandler(Filters.regex("^📹 YouTube"), self.YouTube.initialize)],
                LANGUAGE: [MessageHandler(Filters.text, self.language)]

            },
            fallbacks=[

            ]
        ))

    def start(self, update: Update, context: CallbackContext):
        user = update.message.from_user
        db_user = db.get_user(user.id)
        print(db_user)
        if db_user is None:
            update.message.reply_text("Iltimos tilni tanlang!", reply_markup=language_keyboards)
            return LANGUAGE
        else:
            update.message.reply_text(MAIN_MENU_TEXT[user['language']], reply_markup=menu_keyboards(db_user['language']))
            return MENU

    def language(self, update: Update, context: CallbackContext):
        user = update.message.from_user
        context.user_data['language'] = language = {uz_lang: 0, ru_lang: 1, en_lang: 2}[update.message.text]
        db.create_user(user.id, language)
        update.message.reply_text(SUCCESSFULLY_REGISTERED[language], reply_markup=menu_keyboards(language))
        return MENU

    def run(self):
        self.start_polling()
        print("Starting polling...")
        self.idle()


bot = Bot()
bot.run()