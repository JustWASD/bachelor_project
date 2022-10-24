# importing Image class from PIL package
import time

from PIL import Image

# creating a object
im = Image.open("Nasi.jpg")
im2 = Image.open("tattooidee.jpg")

im.show()
time.sleep(3)
im.close()
im2.show()
time.sleep(3)
im2.close()
im.show()

