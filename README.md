# qrcode-by-vmtram
generates a qrcode that can be formated and use a logo.

Please take note that this is not my own original code, this was created by https://github.com/vmtram however the code was never added to a repository.

## Python Libraries required
```cmd
pip install qrcode[pil]
```

## parameters:

### fill_color
This is the foreground color and uses any text base color ie:
* black, green, magenta, lime, etc.

### back_color
This is the background color and uses any text base color along with transparent ie:
* transparent, white, green, yellow, etc.
### body
This is the texture/shape to be used for the middle of the QR code:
* square : will generate squares as the centre.
* point : will generate dots as the centre.
### version
* This is the density and complexity of the qr code the higher this is set the more details will be added to the qr code.
### eye_ball
This is the texture/shape to be used inside of the cornert pieces.
* ball0 = squares
* ball1 = circles
### eye
This is the texture/shape to be used corner frame pieces.
* eye0 = squares
* eye1 = circles

## An important variable to play with when genrating and testing the qr code:

The 'error_correction' parameter for the qr code references to the below:

There are the following four levels. The values in parentheses indicate error correction ability (error correction rate for all codewords).

* 'qrcode.constants.ERROR_CORRECT_L' (Approx 7%)
* 'qrcode.constants.ERROR_CORRECT_M' (Approx 15%, default)
* 'qrcode.constants.ERROR_CORRECT_Q' (Approx 25%)
* 'qrcode.constants.ERROR_CORRECT_H' (Approx 30%)

For more information about the QR code error correction feature, refer to the official page of Denso Wave below.

https://www.qrcode.com/en/about/error_correction.html
