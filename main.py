'''import qrcode

img = qrcode.make('https://www.youtube.com/watch?v=y9VXWsU3FSE')
img.save('qrcode.png')

'''
import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('Some data')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
cc=img.save('code.png')
print(cc)