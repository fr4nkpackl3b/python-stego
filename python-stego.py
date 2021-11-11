#!/usr/bin/env python3

from PIL import Image
import re

R = 0; G = 1; B = 2

img_name = 'outfile.png'

try:
    img = Image.open(img_name)   # return an image object
except:
    print ('Put outfile.png file on this directory')
    exit(1)

pixels = list(img.getdata())    # gets the image's data
nozero = []

print("Extracting non zero pixels...")
for rgb in pixels:  # skipping zero rgb
        if rgb != (0, 0, 0):
                nozero.append(rgb)
message = ""

print("getting the message")
# Getting the last digit from the RBG tuples
for i in nozero:
        if i[0] % 10 != 0 or i[1] % 10 != 0 or i[2] % 10 != 0:  # some numbers don't end with 0, so we will want it

            r = '{:08b}'.format(i[R] % 10)[6:8] # Get the last 2 bits of the octal obtained by doing module 10, and convert them to binary
            g = '{:08b}'.format(i[G] % 10)[5:8] # Get the last 3 bits ----
            b = '{:08b}'.format(i[B] % 10)[5:8] # Get the last 3 bits ----
            str = r + g + b # All the bits represents a binary number
            i = chr(int(str[:8], 2))  # ASCII char from each 8 bits number converted to decimal
            message = message + i   # joins each char to a message

print("Looking for the flag...")
regex = re.compile("(hidden message is:[.*])") # creating the pattern to find the flag inside the message
found = regex.search(message)   # searching regex in the message

if found:
    print(found.group(1))   # shows the match
    exit(0)
else:
    print ("nothing found")
    exit(1)
