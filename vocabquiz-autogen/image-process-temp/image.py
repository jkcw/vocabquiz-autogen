from PIL import Image
import pytesseract
from os import listdir
from os.path import isfile, isdir, join

pytesseract.pytesseract.tesseract_cmd = 'C:/Users/jpc72/AppData/Local/Tesseract-OCR/tesseract.exe'

text_file = open("res.txt", "w")

mypath = "C:/Users/jpc72/Desktop/Vocab Images"
files = listdir(mypath)
size = len(files)

#res = ""
n = 1
for file_name in files:
    path = "C:/Users/jpc72/Desktop/Vocab Images/" + file_name
    img = Image.open(path)
    text = pytesseract.image_to_string(img, lang='eng')
    text_file.write(text)
    print(str(n)+"/"+ str(size))
    n += 1
    #res += text

text_file.close()