
from constants import *
from .texts import *
from pytube import YouTube as Yt
from pytube.exceptions import RegexMatchError
from .keyboards import make_yt_text
import youtube_dl


class YouTube:

    def initialize(self, update: Update, context: CallbackContext):
        user = update.message.from_user
        db_user = db.get_user(user.id)
        update.message.reply_text(SEND_YOU_TUBE_URL_MESSAGE_TEXT[db_user['language']])
        return YOU_TUBE_GET_URL_OR_ID

    def get_url_or_id(self,update:Update, context:CallbackContext):
        user = update.message.from_user
        db_user = db.get_user(user.id)
        url = update.message.text
        try:
            yt = Yt(url)
            dl = youtube_dl.YoutubeDL({}).download([url])
            print(dl)
        except RegexMatchError:
            update.message.reply_text(URL_NOT_MATCH[db_user['language']])
            return
        else:
            res = make_yt_text(db_user['language'], yt)
            if res is not None:
                update.message.reply_photo(**res)
                context.user_data['yt_video'] = yt
                return VIDEO_ACTIONS
            else:
                update.message.reply_text("Kechirasiz video topilmadi!\nQayta urinib ko'ring!")

    def download_video(self,update: Update, context: CallbackContext):
        video: YouTube = context.user_data['yt_video']
        keyboards:list = []
        for st in video.streams:
            pass


    def download_audio(self,update:Update, context:CallbackContext):
        print('download_audio')

    def save_video(self,update:Update, context:CallbackContext):
        print('save video')
