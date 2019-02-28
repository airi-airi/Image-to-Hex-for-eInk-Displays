#GPL-3.0-only

from PIL import Image

im = Image.open("eye.bmp")  #replace with your bitmap
pix = im.load();
imwidth,imheight = im.size

if(imwidth%8 != 0): #image width must be a multiple of 8
    quit()

hexwidth = imwidth/8

hexarr = []
for jj in range(0,imheight):
    for ii in range(0,hexwidth):
        strv = ''
        for ij in range(0,8):
            pixval = pix[(ii*8)+ij,jj]
            if(pixval == 255):
                pixval = 1
            else:
                pixval = 0
            strv += str(pixval)
        #hexv = hex(int(strv, 2))
        num = (int(strv, 2))
        numa =  '0x%02X' % num
        hexarr.append(numa)


print "const unsigned char IMAGE_EYE[] PROGMEM = {"

cnter = 0
for a in hexarr:
    print a + ",",
    cnter += 1
    if cnter > 15:
        cnter = 0
        print
print
print "};"






