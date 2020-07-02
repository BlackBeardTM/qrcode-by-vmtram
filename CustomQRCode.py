import qrcode
from custom_image import CustomImage
from PIL import Image
import uuid,base64,json
from io import BytesIO

QRCodes = []
version = 4
border = 1
box_size = 30
qr = qrcode.QRCode(
    version=version,
    error_correction=qrcode.constants.ERROR_CORRECT_Q,
    box_size=box_size,
    border=border,
    image_factory=CustomImage,
)

qr.add_data("random value")
qr.make(fit=True)
# Generate fancy qr code
img = qr.make_image(fill_color="black", back_color="transparent", body='point',version=version,eye_ball="ball0", eye="eye0")
img.save("qrcode.png")
# Add logo
im = Image.open('qrcode.png')
im = im.convert("RGBA")
logo = Image.open('logo.png')
logo_scale = version /1.5 if version > 4 else version / 1.25
pixel_size = (17 + version * 4 + 2*border) * box_size
box = (int(pixel_size/2-(100*logo_scale)), int(pixel_size/2-(25*logo_scale)),
       int(pixel_size/2+(100*logo_scale)), int(pixel_size/2+(25*logo_scale)))
im.crop(box)
region = logo
region = region.resize((box[2]-box[0], box[3]-box[1]))
im.paste(region,box)
buffered = BytesIO()
im.paste(region,box)
im.save("finalQR.png")
im.show("qrcodex.png")