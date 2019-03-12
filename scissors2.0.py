from PIL import Image, ImageDraw

from MechanicalDrawing import quadrangles1, HorizontalDrawing, stripes, VerticalDrawing, quadrangles, png

image = Image.open("ans1" + png)  # Открываем изображение.
# draw = ImageDraw.Draw(image)
# print(quadrangles1[210][0])

stripes_original = tuple(stripes)
quadrangles1_original = tuple(quadrangles1)
Cut = "Cut/"
a = f"Cut/pic"
buf = []
k=0
def reverse(arr, img):
    # j = 0
    i = 0
    # a = "Cut/pic"
    # print(len(arr))
    global a
    global k
    while i < len(arr):
        #print(i, " step")
        # try:
        # image = Image.open("ans1.png")
        #print("размер =",img.size[0],"*",img.size[1])
        b = a + f'.{i}'
        img.crop((arr[i][0][0] + 1, arr[i][0][1] + 1, arr[i][1][0], arr[i][1][1])).save(b + png, "PNG")

        # print(stripes)

        stripes.clear()
        image = Image.open(b + png)
        #print("размер image=", image.size[0], "*", image.size[1])
        if image.size[0] >= 4 and image.size[1] >= 7:
            # print(image.size[0], "*", image.size[1])
            # print("i = ", i)
            draw = ImageDraw.Draw(image)
            HorizontalDrawing(image, draw)
            # print(stripes)
            image.save(b + png, "PNG")
            image = Image.open(b + png)
            draw = ImageDraw.Draw(image)
            quadrangles.clear()
            quadrangles1.clear()
            #print("stripes =", stripes)
            j = 0
            while j < len(stripes):
                VerticalDrawing(j, image, draw)
                j = j + 1
            image.save(b + png, "PNG")
            # print(quadrangles)
            j = 0
            while j != len(quadrangles):
                quadrangles1.append([quadrangles[j], quadrangles[j + 1]])
                j = j + 2
            #print(quadrangles1)
            # j = j + 1
            if quadrangles1[0][0][0] == -1 and quadrangles1[0][0][1] == -1 and quadrangles1[0][1][0] == image.size[0] and quadrangles1[0][1][1] == image.size[1]:
                buf.append(([], image,b))
                i = i + 1
                continue
            else:
                buf.append((tuple(quadrangles1),image,b))

            #a = b

        # image.crop((0,stripes[0][0] + 1,image.size[0],stripes[0][1])).save(f"Cut/pic{i}.png", "PNG")
        # del draw
        #  print("DONE!!!!")
        #  i = i + 1
        # else
        #a = b
        i = i + 1



reverse(quadrangles1_original, image)
#print("+++++++++++",len(buf))
#a = f"Cut/pic{0}"
#reverse(buf[0][0], buf[0][1])
#a = f"Cut/pic{0}"
#buf.pop(0)
#print("+++++++++++",len(buf))
#a = f"Cut/pic{1}"
#reverse(buf[0][0], buf[0][1])
#buf.pop(0)
#print("+++++++++++",len(buf))
i=0
while len(buf)!=0:
    a = buf[0][2]
    reverse(buf[0][0], buf[0][1])
    # a = f"Cut/pic{0}"
    buf.pop(0)
    #print("+++++++++++", len(buf))
    i=i+1
