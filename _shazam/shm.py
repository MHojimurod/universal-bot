from ShazamAPI import Shazam


def find_music(music):


    mp3_file_content_to_recognize = open(music, 'rb').read()

    shazam = Shazam(mp3_file_content_to_recognize)
    recognize_generator = shazam.recognizeSong()
    result = next(recognize_generator)
    if result:

        data = result[1]
        return data