try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

#pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files(x86)\Tesseract-OCR\tesseract.exe'
print(pytesseract.image_to_string(Image.open('mail.png')
                                  ,  lang = 'eng'
                                  ))
