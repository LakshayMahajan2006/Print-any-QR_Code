# Print-any-QR_Code
#import qrcode module
import qrcode# pip install qrcode

qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5

    )

data = "Hello I am a QR Code. "
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="black", back_color="white")
img.save("qr.png")
