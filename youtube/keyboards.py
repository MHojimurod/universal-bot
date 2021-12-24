from pytube import YouTube
from constants import *

DASHES = '-' * 20


def make_yt_text(lang: int, yt: YouTube):
    text = f"<b>id:</b> {yt['id']}\n<b>title:</b>{yt['title']}\n<b>description:</b>\n{DASHES}\n{yt['description'][0:20]}\n{DASHES}"
    keyboards = InlineKeyboardMarkup([
        [InlineKeyboardButton(DOWNLOAD_VIDEO_TEXT[lang], callback_data=f"download_video:{yt['id']}"),
         InlineKeyboardButton(DOWNLOAD_AUDIO_TEXT[lang], callback_data=f"download_audio:{yt['id']}")],
        [InlineKeyboardButton(SAVE_VIDEO[lang], callback_data=f"save_video:{yt['id']}")]
    ])
    return {
        "caption": text,
        "photo": yt['thumbnail'].split("?")[0],
        "parse_mode": "HTML",
        "reply_markup": keyboards
    }
