from PIL import Image

im = Image.open("image_1.jpg")


im.show()


im.format


im.size


im.mode


box = (100, 100, 400, 400)
region = im.crop(box)

region.show()

im1 = im.copy()
region = region.transpose(Image.ROTATE_180)
im1.paste(region, box)


im1.show()

r, g, b = im.split()

r.show()

g.show()

b.show()


im2 = Image.merge("RGB", (b, g, r))
im2.show()

im3 = im.resize((128, 128))
im3.show()

im4 = im.rotate(45) # degrees counter-clockwise
im4.show()

im5 = im.transpose(Image.FLIP_LEFT_RIGHT)
im5.show()

im6 = im.convert(mode = 'L')
im6.show()

im6.mode

from PIL import ImageFilter


im7 = im.filter(ImageFilter.BLUR)
im7.show()


im8 = im.filter(ImageFilter.UnsharpMask())
im8.show()



from PIL import ImageEnhance

enh = ImageEnhance.Contrast(im)
im9 = enh.enhance(2)
im9.show()

im9.save('Enh.png')

