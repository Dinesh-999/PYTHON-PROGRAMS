# creating qrcode
#

import pyqrcode

# String which represent the QR code
s = "https://www.youtube.com/channel/UCeO9hPCfRzqb2yTuAn713Mg"

# Generate QR code
url = pyqrcode.create(s)

# Create and save the png file naming "myqr.png"
url.svg("C:\\Users\\Dinesh\\PycharmProjects\\starterkit\\Begineer\\myyoutube.svg", scale=8)

