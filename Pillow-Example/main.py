# Combining two images
# Description: Take two images (2 files): one is the foreground object, the other is the background. Once combined, the resulting image has the foreground object with the background. 
# Author: Oscar Zhang
# Date: Oct,2019

# Import necessary image processing package, library or module.
from PIL import Image
import myColourModule

# Main part of program

# Open the files
imageKidGreen = Image.open("kid-green.jpg").load()
image_beach = Image.open("beach.jpg").load()

# Create output canvas
imageOutput = Image.open("kid-green.jpg")

# Get width and height of image
width = imageOutput.width
height = imageOutput.height
print(width,height)

# Create a nested for loop using range
for i in range(height):
  for j in range(width):
    r = imageKidGreen[i,j][0]
    g = imageKidGreen[i,j][1]
    b = imageKidGreen[i,j][2]

    # If the pixel at coordinate i,j is green, we want to replace that pixel's green color with the color from the beach image (could be beige, blue, etc.)
    # if g == 255 :
    if myColourModule.isPixelBlue(r,g,b):
      xy = (i,j) 
      
      # Create a tuple that holds the coordinates i,j for use in Line 39
      colour = (255,255,10)
      
      # Get the colour of the pixel in the beach image
      imageOutput.putpixel(xy, colour) 
    if myColourModule.isPixelGreen(r,g,b) :
      # The function returns True or False 
      xy = (i,j) 
      
      # Create a tuple that holds the coordinates i,j for use in Line 39
      colour = image_beach[i,j]
      
      # Get the colour of the pixel in the beach image
      imageOutput.putpixel(xy, colour) 
      
      # Change the colour in the output image (which originally was the same as the green screen image - see Line 21) to the beach image
      # Note: The putpixel function takes two parameters. The first one is the coordinates in the image to modify, and the second parameter is the colour to modify it to.

imageOutput.save("output.png","png")
