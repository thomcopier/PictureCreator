from PIL import Image
from random import randint
from math import ceil,trunc
from pathlib import Path

# Save Image
def save_image(image, path):
    image.save(path, 'bmp')
  
# Create a new image with the given size
def create_image(i, j):
    image = Image.new("RGB", (i, j), "white")
    return image

def distributeDots(totalX, totalY, image):
    width, height = image.size
    betweenX = (width-totalX)/(totalX+1)
    betweenY = (height-totalY)/(totalY+1)
    currentY = int(betweenY+1)
    pixelsToChange = []
    for j in range(totalY):
        currentX = betweenX+1
        for i in range(totalX):
            pixelsToChange.append([int(currentX), int(currentY)])
            currentX += betweenX + 1
        currentY += betweenY + 1
    return(pixelsToChange)
    
def randomChange(pixels, maxOffsetX, maxOffsetY):
    for pixel in range(len(pixels)):            
        pixels[pixel][0] += randint(-maxOffsetX,maxOffsetX)
        pixels[pixel][1] += randint(-maxOffsetY,maxOffsetY)
    return pixels

def sizeDots(pixels, sizeX, sizeY):
    newPixels = []
    for pixel in pixels:
        addLeft = int(-((ceil(sizeX/2))-1))
        addRight = int(trunc(sizeX/2))
        addTop = int(-((ceil(sizeY/2))-1))
        addBottom = int(trunc(sizeY/2))
        for i in range(addLeft,addRight):
            for j in range(addTop, addBottom):
                newPixels.append((pixel[0]+i,pixel[1]+j))
    return newPixels

def colorPixels(image, pixels, color):
    for pixel in pixels:
        image.putpixel(pixel,color)
    return image

def gatherVariables():
    print("How do you want the file to be called? (.bmp will be added automatically)")
    filename = input()
    print("How many pixels are there in every square horizontally?")
    pixelsPerSquareX = int(input())
    print("How many pixels are there in every square vertically?")
    pixelsPerSquareY = int(input())
    print("How many squares are there horizontally?")
    totalSquaresX = int(input())
    print("How many squares are there vertically?")
    totalSquaresY = int(input())
    print("What is the width of the spot?")
    spotWidth = int(input())
    print("What is the height of the spot?")
    spotHeight = int(input())
    print("What is the maximum random offset horizontally?")
    maxRandOffsetX = int(input())
    print("What is the maximum random offset vertically?")
    maxRandOffsetY = int(input())
    return filename,pixelsPerSquareX,pixelsPerSquareY,totalSquaresX,totalSquaresY,spotWidth,spotHeight,maxRandOffsetX,maxRandOffsetY

name,PPSX,PPSY,TSX,TSY,SW,SH,MROX,MROY = gatherVariables()
newImage = create_image(PPSX*TSX, PPSY*TSY)
dotMatrix = distributeDots(TSX,TSY,newImage)
dotMatrix = randomChange(dotMatrix, MROX, MROY)
sizedDotMatrix = sizeDots(dotMatrix, SW, SH)
newImage = colorPixels(newImage, sizedDotMatrix, (0,0,0))
print(r''+str(Path().absolute()) + "\Pictures\ " + name + '.bmp')
save_image(newImage, r''+str(Path().absolute()) + "\Pictures\ " + name + '.bmp')