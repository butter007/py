from PIL import Image,ImageDraw,ImageFont

def add_num(img) :
    draw = ImageDraw.Draw(img)
    myfont = ImageFont.truetype('c:/windows/fonts/Arial.ttf',size = 40)
    fillcolor = '#ff0000'
    width ,height = img.size
    print width
    print height
    draw.text((0,50),'99',font = myfont,fill = fillcolor)
    img.save('reuslt.jpg','jpeg')
    return 0

print dir(__name__)