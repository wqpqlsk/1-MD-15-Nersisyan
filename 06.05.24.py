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

