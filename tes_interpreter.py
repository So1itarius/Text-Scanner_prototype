try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

"""
Блок работы с tesseract-ом, пока тестовый

"""
# pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files(x86)\Tesseract-OCR\tesseract.exe'
print(pytesseract.image_to_string(Image.open('mail.png') # читает имя только в таком виде, лол, из папки examples не читает
                                  , lang='eng'
                                  ))
