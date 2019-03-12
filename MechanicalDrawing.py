from PIL import Image, ImageDraw

png = ".png"
image = Image.open("ans"+png)  # Открываем изображение.
draw = ImageDraw.Draw(image)  # Создаем инструмент для рисования.
width = image.size[0]  # Определяем ширину.
height = image.size[1]  # Определяем высоту.
pix = image.load()  # Выгружаем значения пикселей.

# flag = 0
print(width, "*", height)
print(image.getpixel((0, 2)))
stripes = []


def HorizontalDrawing(image, draw):
    flag = 0
    buf = 0
    i, j = 0, 0
    width = image.size[0]
    height = image.size[1]
    #print(width, "*", height)
    while i < height:
        while j < width:  # ширина
            #print(i, j)
            a = image.getpixel((j, i))[0]
            b = image.getpixel((j, i))[1]
            c = image.getpixel((j, i))[2]
            # print(i,j)
            if (a <= 24 and b <= 24 and c <= 24) and flag == 0:
                flag = 1
                print("++++", j, i, image.getpixel((j, i)))
                draw.line((0, i - 1, width, i - 1), (10, 25, 255), 1)
                # print("++++", j, i - 1)
                # image.save("ans1.jpg", "JPEG")
                # 200 212 212
                # del draw
                # exit(0)
                buf = i - 1
                stripes.append([buf,height])
                #i = i + 1
                break
            elif flag == 1 and (a <= 24 and b <= 24 and c <= 24):
                #i = i + 1
                #j = 0
                break
                #print("++++")

            elif flag == 1 and j == width - 1:

                draw.line((0, i, width, i), (255, 35, 28))
                stripes.pop(len(stripes) - 1)
                #del stripes[len(stripes) - 1]
                stripes.append([buf, i])
                print("end", j, i)
                flag = 0

            j = j + 1
        i = i + 1
        j = 0

        # draw.point((i, j), (a, b, c))


HorizontalDrawing(image, draw)
quadrangles = []


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
            # print(i,j)
            if (a <= 24 and b <= 24 and c <= 24) and flag == 0:
                flag = 1
                # print("++++", a, b, c, j, i, image.getpixel((i, j)))
                draw.line((i - 1, stripes[x][0], i - 1, height), (10, 25, 255))
                quadrangles.append((i - 1, stripes[x][0]))
                quadrangles.append((width,stripes[x][1]))
                print("++++", j, i - 1)
                # image.save("ans1.jpg", "JPEG")
                # 200 212 212
                # del draw
                # exit(0)
                # buf = i - 1
                #i = i + 1
                break
            elif flag == 1 and (a <= 24 and b <= 24 and c <= 24):
                #i = i + 1
                j = stripes[x][0]
                break
                # print("++++")
            elif flag == 1 and j == height - 1:
                # if flag1 == 0:
                #    flag1 = i
                if flag1 == i - 1:
                    draw.line((i - 1, stripes[x][0], i - 1, height), (255, 35, 28))
                    # stripes.append([buf,i])
                    quadrangles.pop(len(quadrangles) - 1)
                    #del quadrangles[len(quadrangles) - 1]
                    quadrangles.append((i - 1, height))
                    print("end", i, j)
                    flag = 0
                    flag1 = 0
                else:
                    flag1 = i
            j = j + 1
        i = i + 1
        j = stripes[x][0]


i = 0
while i < len(stripes):
    VerticalDrawing(i, image, draw)
    i = i + 1
quadrangles1 = []
i = 0
while i != len(quadrangles):
    quadrangles1.append([quadrangles[i], quadrangles[i + 1]])
    i = i + 2

print(len(quadrangles1))

# VerticalDrawing(30)
image.save("ans1"+png, "PNG")
# 200 212 212
del draw
# print(stripes)
