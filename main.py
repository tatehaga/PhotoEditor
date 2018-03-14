#!/usr/bin/python3
import random, argparse
from PIL import Image

parser = argparse.ArgumentParser(description="Image Randomness Adder")
parser.add_argument("filename", help= "name of image file or directory")
parser.add_argument("-o", "--output", help="Name of output", type=str)
parser.add_argument("-v", "--verbose", help= "prints information about the input file", action="store_true")
parser.add_argument("-ns","--nosave", help= "returns file without saving a copy", action = "store_false")
parser.add_argument("-nd", "--nodisplay", help="saves file without displaying the output", action = "store_false")
parser.add_argument("-r", "--randomness", help="enter variation of possible RGB noise values (default of 30)" , default=30, type=int)
args = parser.parse_args()
filename, filetype = str(args.filename).split('.')

rd = args.randomness


im = Image.open(args.filename)
pixelMap = im.load()
if args.verbose:
    print("Filename: " + filename)
    print("File type: " + filetype)
    print("Randomness: " + str(rd))
    print("Image Type: " + str(im.mode))
if args.nodisplay:
    im.show()
img = Image.new( im.mode, im.size)
pixelsNew = img.load()
#
for i in range(img.size[0]):
    for j in range(img.size[1]):
        rand_red = random.randint(-rd,rd)
        rand_blue = random.randint(-rd,rd)
        rand_green = random.randint(-rd,rd)
        redval = pixelMap[i,j][0] + rand_red
        blueval = pixelMap[i,j][1] + rand_blue
        greenval = pixelMap[i,j][2] + rand_green
        if redval >= 255:
            redval = 255
        if redval <= 0:
            redval = 0
        if blueval >= 255:
            blueval = 255
        if blueval <= 0:
            blueval = 0
        if greenval >= 255:
            greenval = 255
        if greenval <= 0:
            greenval = 0
        if str(im.mode) == "RGBA":
            alpha = pixelMap[i,j][3]
            pixelsNew[i,j] = (redval, blueval, greenval, alpha)
        else:
            pixelsNew[i,j] = (redval, blueval, greenval)
im.close()
if args.nodisplay:
    img.show()
if args.nosave:
    if args.output == None:
        img.save(filename + "_RandomNoise_" + str(rd)+ "." + filetype)
    else:
        img.save(str(args.output) + "." + filetype)
img.close()
