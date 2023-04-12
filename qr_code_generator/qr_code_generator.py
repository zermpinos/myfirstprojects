"""
qr_code_generator.py
This program creates a qr code, if given a url.

Requirements:
    - Python 3.x
    - qrcode module
Parameters:
    - dara: The valid url mentioned before.

Author:
    Panagiotis Zermpinos
Version:
    1.0 (April 2023)
"""

import qrcode

data = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
img = qrcode.make(data)

# Save the image file
img.save('qrcode_1.png')
