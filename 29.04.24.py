from PIL import Image
def num1():
  pic = Image. open ("открыткабрату. jpg")
  pic. show()
    result = pic.crop((232, 171, 903, 843))
    result. save ("пеоткрытка.jpg")
    result. show()
num1()

from PIL import Image
def num2():
  a = {"hapb": "hapb-jpg", "8mar": "8mar. jpg", "23feb": "28feb. jpg" }
  b = input("Какой праздник?")
  if b in a:
    result = a[b]
    if result is not None:
      ot = Image. open(result)
      ot.show()
    else:
      print ("ошибка")
    else:
      print ("Открытки нет")


from PIL import Image, ImageDraw, ImageFont
def num3():
  name = input ("Кого поздравить? ")
  pic = Image. open ("открыткабрату. jpg")
  font = ImageFont. load_default()
  result = pic.crop (200, 90, 850, 900))
  draw_text = ImageDraw.Draw(result)
  draw_text.text((215, 100), f"{name} Поздравляю!", stroke_width=(1), font_size=30, fill=(255,0,0))
  result.show()
num3)
