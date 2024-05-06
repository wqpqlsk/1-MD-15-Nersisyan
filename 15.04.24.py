def a1():
    from PIL import Image
    image = Image.open('pes.jpg')
    image.show()
    print(f"Формат: {image.format}")
    print(f"Ширина: {image.width}")
    print(f"Размер: {image.size}")
    print(f"Цветовая модель: {image.mode}")
a1()

def pes2(in_path, out_path):
    from PIL import Image
    a = Image.open(in_path)
    wid = int(a.width)//3
    hei = int(a.height)//3
    aa_img = a.resize(wid, hei)
    aa_img.save(out_path)
    aa_img.show()
    b = aa_img.transpose(Image.FLIP_RIGHT_LEFT)
    b.show()
    b.save('D:\\nersisyan\\pythonProject6\\pes3.jpg')
    c = aa_img.transpose(Image.FLIP_RIGHT_LEFT)
    c.show()
    c.save('D:\\nersisyan\\pythonProject6\\pes4.jpg')
pes2('D:\\nersisyan\\pythonProject6\\pes.jpg', 'D:\\nersisyan\\pythonProject6\\pes2.jpg')

def img_mirrow(pes):
    for i in pes:
        temp = Image.open(i)
        temp.show()
        v = temp.filter(ImageFilter.SHARPEN)
        v.save('D:\1-MD-15-Nersisyan\\15.04.24\\{i+"pes0.jpg"}')
img_mirrow(['D:\1-MD-15-Nersisyan\\15.04.24\\pess0.jpg',
            'D:\1-MD-15-Nersisyan\\15.04.24\\pes1.jpg',
            'D:\1-MD-15-Nersisyan\\15.04.24\\pes3.jpg',
            'D:\1-MD-15-Nersisyan\\15.04.24\\pes4.jpg',
            'D:\1-MD-15-Nersisyan\\15.04.24\\pes5.jpg'])