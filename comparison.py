import sys

from PIL import Image, ImageStat, ImageOps

from MechanicalDrawing import png

from PIL import Image, ImageDraw, ImageFont

from PIL import ImageFont, ImageDraw

im = Image.open("pic.208.8.0" + png)
#image2 = Image.open("ans" + png)
txt = Image.new('RGB', im.size, (255, 255, 255, 0))\
    #.save("autoletter"+png)


#draw = ImageDraw.Draw(txt)
#print(image.size)
#image.resize((152,20),
             #Image.BICUBIC
#             ).save("autoletter"+png)

#image.thumbnail((4,4))\
    #.save("autoletter"+png)

im.resize((24,21),).save("autoletter"+png)


# use a bitmap font


#f = ImageFont.load_default()
f = ImageFont.truetype('arial.ttf', size=40,encoding='UTF-8')
#txt=Image.new('L', (500,50))
d = ImageDraw.Draw(txt)
d.text((0, 0), "п",  font=f, fill=0)
#txt.save("autoletter" + png)
#draw.text((7, 7), "в", font=font)

# use a truetype font


#image = Image.open("pic.198.0" + png)
#stat = ImageStat.Stat(image)
#print(stat.extrema)
