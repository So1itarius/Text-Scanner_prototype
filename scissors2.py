from PIL import Image, ImageDraw

from MechanicalDrawing import quadrangles1, HorizontalDrawing, stripes, VerticalDrawing, quadrangles, png

"""
cutter() - функция, которая принимает массив координат многоуголников, и режет их на отдельные картинки.
           заполняет буфферынй массив buf
in_depth() - применяет cutter() к массиву картинок buf, новые данные отправляются в конец списка,а первый рабочий элемент 
             удаляется и так до тех пор пока список не обнулится. Пытался сделать рекурсивную функцию, но запутался с именами,
             поэтому это вторая версия, первая пока не работает

"""

Cut = "Cut/"
a = f"Cut/pic"
buf = []


def cutter(arr, img):
    i = 0
    global a
    while i < len(arr):
        b = a + f'.{i}'
        img.crop((arr[i][0][0] + 1, arr[i][0][1] + 1, arr[i][1][0], arr[i][1][1])).save(b + png, "PNG")
        stripes.clear()
        image = Image.open(b + png)
        if image.size[0] >= 4 and image.size[1] >= 7:

            draw = ImageDraw.Draw(image)
            HorizontalDrawing(image, draw)
            image.save(b + png, "PNG")
            image = Image.open(b + png)
            draw = ImageDraw.Draw(image)
            quadrangles.clear()
            quadrangles1.clear()
            VerticalDrawing(image, draw)
            image.save(b + png, "PNG")
            if quadrangles1[0][0][0] == -1 and quadrangles1[0][0][1] == -1 and quadrangles1[0][1][0] == image.size[0] \
                    and quadrangles1[0][1][1] == image.size[1]:
                buf.append(([], image, b))
                i = i + 1
                continue
            else:
                buf.append((tuple(quadrangles1), image, b))
        i = i + 1


def in_depth():
    i = 0
    global a
    while len(buf) != 0:
        a = buf[0][2]
        cutter(buf[0][0], buf[0][1])
        buf.pop(0)
        i = i + 1
