
import qrcode
from requests.api import get
import cv2
from pyzbar.pyzbar import decode
class Qr:
    def create_qrcode(text, color):
        qr_code_img = qrcode.QRCode()
        qr_code_img.add_data(text)
        canvas = qr_code_img.make_image(fill_color=color)
        fname = f"qr_code" + ".png"
        canvas.save(fname, "PNG")
        return fname

    def get_qrcode(image):
        img = cv2.imread(image)
        data = decode(img)[0].data.__str__()
        return data

