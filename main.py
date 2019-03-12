from PIL import Image, ImageDraw

from MechanicalDrawing import HorizontalDrawing, VerticalDrawing, png, quadrangles1
from scissors2 import cutter, in_depth
"""
Данные действия облегчают работу tesseract-у, решая вопрос с сегментацией вручную
"""

image = Image.open("ans"+png)  # Открываем изображение.
draw = ImageDraw.Draw(image)  # Создаем инструмент для рисования.
HorizontalDrawing(image, draw) # Расчерчиваем документ горизонтальными линиями
VerticalDrawing(image, draw) # Расчерчиваем документ вертикальными линиями
image.save("ans1"+png, "PNG")


image = Image.open("ans1" + png) # Открываем расчерченое изображение
draw = ImageDraw.Draw(image)
quadrangles1_original = tuple(quadrangles1)
cutter(quadrangles1_original, image) # режем на прямоугольники
in_depth() # полученые прямоугольники расчерчиваем и режем пока изображение не будет представлять из себя целое слово или букву

del draw