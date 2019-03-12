png = ".png"
stripes = []
quadrangles = []
quadrangles1 = []

"""
HorizontalDrawing() - горизонтальное черчение по строкам, верхняя граница - синяя линия, нижняя - красная.
                      Обрабатывает изображение целиком. Пробегает изображение сверху вниз, наткнувшись на черный пиксель,
                      чертит линию на пиксель выше и идет дальше, если встречается черный пиксель опускается на строчку,
                      если черный пиксель не встречается до конца строки то чертит красную линию и идет дальше.
                      На выходе заполняется глобальынй список stripes, в котором хранятся координаты каждой полосы.
VerticalDrawing() - вертикальное черчение, алгоритм аналогичен горизонтальному, но с изменениями, работает для одной полосы,
                    поэтому в связке с @all_stripes, чтоб покрыть всё изображение
                    На выходе заполняем глобальынй список quadrangles1, где хранятся координаты четырехугольников, а именно
                    левого верхнего угла и правого нижнего угла. (quadrangles пока вспомагательный список)
                    
"""


def HorizontalDrawing(image, draw):
    flag = 0
    buf = 0
    i, j = 0, 0
    width = image.size[0]
    height = image.size[1]
    while i < height:
        while j < width:  # ширина
            a = image.getpixel((j, i))[0]
            b = image.getpixel((j, i))[1]
            c = image.getpixel((j, i))[2]
            if (a <= 24 and b <= 24 and c <= 24) and flag == 0:
                flag = 1
                print("start", j, i, image.getpixel((j, i)))
                draw.line((0, i - 1, width, i - 1), (10, 25, 255), 1)
                buf = i - 1
                stripes.append([buf, height])
                break
            elif flag == 1 and (a <= 24 and b <= 24 and c <= 24):
                break
            elif flag == 1 and j == width - 1:
                draw.line((0, i, width, i), (255, 35, 28))
                # stripes.pop(len(stripes) - 1)
                del stripes[len(stripes) - 1]
                stripes.append([buf, i])
                print("end", j, i)
                flag = 0
            j = j + 1
        i = i + 1
        j = 0


def all_stripes(VerticalDrawing):
    def func(image, draw):
        i = 0
        while i < len(stripes):
            VerticalDrawing(i, image, draw)
            i = i + 1
        i = 0
        while i != len(quadrangles):
            quadrangles1.append([quadrangles[i], quadrangles[i + 1]])
            i = i + 2

    return func


@all_stripes
def VerticalDrawing(x, image, draw):
    j = stripes[x][0]
    height = stripes[x][1]
    width = image.size[0]
    i = 0
    flag = 0
    flag1 = 0
    while i < width:
        while height > j:  # высота
            a = image.getpixel((i, j))[0]
            b = image.getpixel((i, j))[1]
            c = image.getpixel((i, j))[2]
            if (a <= 24 and b <= 24 and c <= 24) and flag == 0:
                flag = 1
                draw.line((i - 1, stripes[x][0], i - 1, height), (10, 25, 255))
                quadrangles.append((i - 1, stripes[x][0]))
                quadrangles.append((width, stripes[x][1]))
                print("start", j, i - 1)
                break
            elif flag == 1 and (a <= 24 and b <= 24 and c <= 24):
                break
            elif flag == 1 and j == height - 1:
                if flag1 == i - 1:
                    draw.line((i - 1, stripes[x][0], i - 1, height), (255, 35, 28))
                    # quadrangles.pop(len(quadrangles) - 1)
                    del quadrangles[len(quadrangles) - 1]
                    quadrangles.append((i - 1, height))
                    print("end", i, j)
                    flag = 0
                    flag1 = 0
                else:
                    flag1 = i
            j = j + 1
        i = i + 1
        j = stripes[x][0]
