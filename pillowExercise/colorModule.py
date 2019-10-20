from PIL import Image



#print(green)
def isPixelGreen(x,y, img):
    
    green = img[5,5]
    if(img[x,y] == green or (img[x,y][0] >0 and img[x,y][0]<19) or (img[x,y][2] >0 and img[x,y][2] < 19) 
        or (img[x,y][1] >200 and img[x,y][1] < 255)):
        return True
    else:
        return False