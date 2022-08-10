第一步安装依赖：启动终端依次敲入命令

sudo apt-get install g++ # or clang++ (presumably)
sudo apt-get install autoconf automake libtool
sudo apt-get install autoconf-archive
sudo apt-get install pkg-config
sudo apt-get install libpng12-dev
sudo apt-get install libjpeg8-dev
sudo apt-get install libtiff5-dev
sudo apt-get install zlib1g-dev

第二步安装Leptonica
sudo apt-get install libleptonica-dev

第三步安装tesseract

sudo apt-get install tesseract-ocr

第四步安装pytesseract

pip install pytesseract

第五步启动python，新建文件夹输入以下代码

#!/usr/bin/env python

from PIL import Image
import pytesseract
text=Image.open('/home/pi/.local/lib/python2.7/site-packages/pytesseract/test.png')
#print(text)
print(pytesseract.image_to_string(text))

第六步保存并运行