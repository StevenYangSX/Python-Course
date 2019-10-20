from PIL import Image
import colorModule


# Open the files
imageKidGreen = Image.open("kid-green.jpg").load()
image_beach = Image.open("beach.jpg").load()

# Create output canvas
imageOutput = Image.open("kid-green.jpg")

# Get width and height of image
width = imageOutput.width
height = imageOutput.height
print(width,height)

#TODO:write functions to put the kid on the beach. if some pixel is green
#     then substitude this pixel with original beach pixel.



def combineImages(imgKid, imgBeach):
    for i in range(width):
        for j in range(height):

            # r = imgKid[i,j][0]
            # g = imgKid[i,j][1]
            # b = imgKid[i,j][2]
            #print("OK!")
            if(colorModule.isPixelGreen(i,j,imgKid)):
                #coverPixel(i,j, imgBeach)
                #print("ok!")
                #imgKid[i,j] = imgBeach[i,j]
                xy = (i,j)
                imageOutput.putpixel(xy, imgBeach[i,j])

#New grayscale image = ( (0.3 * R) + (0.59 * G) + (0.11 * B) ).
def convertToGrayScale(img, img2):
    for i in range(width):
        for j in range(height):
            xy = (i,j)
            img2.putpixel(xy,(int(img[i,j][2] * 0.2988),int(img[i,j][1] * 0.5870),int(img[i,j][0]*0.1140)))
           


#TODO: function to calculate percentage of each color in mm.jpg

def imgToRgbList(img):
    innerList = []
    outterList = []
    for i in range(width_mm):
        for j in range(height_mm):
            innerList = list(img[i,j])
            outterList.append(innerList)
    return outterList

def shadowRemover(list):
    for rgb in list:
        if(rgb[0] < 38 and rgb[1] < 38 and rgb[2] < 38):
            list.remove(rgb)
    return rgb
def logoRemover(list):
    for rgb in list:
        if(rgb[0] > 220 and rgb[1] < 220 and rgb[2] < 220):
            list.remove(rgb)
    return rgb

def greenPicker(list):
    counter = 0
    for rgb in list:
        if(rgb[0] < 30 and rgb[1] > 70 and rgb[2] < 30):
            list.remove(rgb)
            counter += 1
    return counter, list

def redPicker(list):
    counter = 0
    for rgb in list:
        if(rgb[0] >190  and rgb[1] < 50 and rgb[2] < 50):
            list.remove(rgb)
            counter += 1
    return counter

def bluePicker(list):
    counter = 0
    for rgb in list:
        if(rgb[0]  < 70  and rgb[1] < 70 and rgb[2] > 160):
            list.remove(rgb)
            counter += 1
    return counter

def yellowPicker(list):
    counter = 0
    for rgb in list:
        if(rgb[0]  > 210  and rgb[1] > 210 and rgb[2] < 90):
            list.remove(rgb)
            counter += 1
    return counter


def removeBlue(list):
    rg = []
    for rgb in list:
        rg.append(rgb[0:2])
    return rg


def brownPicker(list):
    rg = removeBlue(list)
    counter = 0
    for i in rg:
        if(i[0] < 100 and i[1] < 60):
            counter += 1
    return counter

def greenRemover(list , targetList):
    for item in targetList:
        list.remove(item)
    return list


def calculatePercentage(img):

    rgb_list = imgToRgbList(img)
    numOfData = 0
    numGreen = 0
    numRed = 0
    numBlue = 0
    numYellow = 0
    numOrange = 0
    numBrown = 0
    #print (len(rgb_list))
    #return print(rgb_list)
    #get rid of shaddles and white logo
    #shadowRemover(rgb_list)
    for rgb in rgb_list:
        if(rgb[0] < 38 and rgb[1] < 38 and rgb[2] < 38):
            rgb_list.remove(rgb)
        if(rgb[0] > 220 and rgb[1] < 220 and rgb[2] < 220):
            rgb_list.remove(rgb)
    #print (len(rgb_list))
    #logoRemover(rgb_list)

    numOfData = len(rgb_list)
    print ("rgb list before remove:",len(rgb_list))
    numGreen , greenList = greenPicker(rgb_list)
    greenRemover(rgb_list, greenList)
    print ("number of Green pixel:",numGreen)
    print ("number after remove green: ",len(rgb_list))
    # numRed = redPicker(rgb_list)
    # numBlue = bluePicker(rgb_list)
    # numYellow = yellowPicker(rgb_list)
    # numBrown = brownPicker(rgb_list)
    # numOrange = len(rgb_list)
    # colorDetector(rgb_list)
    # resultPrinter(rgb_list)
    #print(numOfData,numGreen,numRed,numBlue,numYellow,numBrown,numOrange)


#function call to get resulting image

# combineImages(imageKidGreen, image_beach)
# imageOutput.save("output.png","png")

# image_combined = Image.open("output.png").load()
# imageOutput2 = Image.open("kid-green.jpg")
# convertToGrayScale(image_combined,imageOutput2)
# imageOutput2.save("gray.png","png")

mmImg = Image.open("mm.jpg").load()
imageOutput3 = Image.open("kid-green.jpg")

width_mm = imageOutput3.width
height_mm = imageOutput3.height
# print(width_mm, height_mm)

calculatePercentage(mmImg)