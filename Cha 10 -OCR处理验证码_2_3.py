from PIL import Image
im = Image.open(r'C:\Users\15527\OneDrive\Documents\爬虫\captcha.jpg')
gray = im.convert('L')
gray.show()
gray.save(r"C:\Users\15527\OneDrive\Documents\爬虫\captcha_gray.jpg")

threshold = 150
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
out = gray.point(table, '1')
out.show()
out.save("captcha_thresholded.jpg")

import pytesseract
th = Image.open('captcha_thresholded.jpg')
print(pytesseract.image_to_string(th))