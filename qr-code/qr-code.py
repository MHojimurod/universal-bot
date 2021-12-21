
import qrcode

def create_qrcode(text, color):
    qr_code_img = qrcode.QRCode()
    qr_code_img.add_data(text)
    canvas = qr_code_img.make_image(fill_color=color)
    fname = f"qr_code" + ".png"
    canvas.save(fname, "PNG")
    return fname


import cv2
from pyzbar.pyzbar import decode


filename = "qr-code/qr_code.png"
image = cv2.imread(filename)
print(decode(image))





