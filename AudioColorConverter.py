#Program:  paintMIDI image converter
#Name:     Carlos Espinoza
#Date:     
#
#Description:





###############################################################
# RGB - will store RGB values for comparisons. 0-255 range
# It will store RED value, GREEN value, BLUE value.
# It will return said information.
#
class RGB:

  def __init__(self, newR, newG, newB):
    self.R = newR
    self.G = newG
    self.B = newB
    val = 0
  
  def myRed(self):
    return self.R
  
  def myGreen(self):
    return self.G
      
  def myBlue(self):
    return self.B
#    
#end RGB CLASS
###############################################################


###############################################################
# Values Global
#



myImg  = pickAFile()          # get a file from user
myImg  = makePicture(myImg)   # take file path and turn into picture

myPath = myImg                # original file path, used to make a modified copy

width  = getWidth(myImg)      # size of width of image selected
height = getHeight(myImg)     # size of height of image selected

mynewpic = makeEmptyPicture(640,480,white) # make blank canvas.


wt = makeColor(255, 255, 255 )    #make list of colors for comparison
bk = makeColor(0,   0,   0)
rd = makeColor(255, 0,   0)
og = makeColor(255, 165, 0)
yl = makeColor(255, 255, 0)
gr = makeColor(0,   255, 0)
bl = makeColor(0,   0,   255)
vi = makeColor(143, 0,   255)

# take and sort list by value, look at jeremys email to get values.
color_list = [rd, og, yl, gr, bl, vi, wt, bk]



# make list of color data objects "RGB", RGB values. 0-255 value range
wtL = RGB(255, 255, 255)
bkL = RGB(0,   0,   0)
rdL = RGB(255, 0,   0)
ogL = RGB(255, 165, 0)
ylL = RGB(255, 255, 0)
grL = RGB(0,   255, 0)
blL = RGB(0,   0,   255)
viL = RGB(143, 0,   255)

# push to a list for iteration.
cList = [rdL, ogL, ylL, grL, blL, viL, wtL, bkL]

#
# END values
###############################################################



###############################################################
# compare()
#
# check pixle that is passed in
# find the closest color in our color list
# return the color in our list
# First algorithem for color selection. Not acurate enough.
# 
def compare(pixColor, color_list):

  closest = 200 #200 works best thus far
  color = white
  global maxDiff
  
  size = len(color_list)
  
  for x in range (0, size-1):
  
    thisFar = distance(color_list[x], pixColor)
    
    if closest > thisFar:
      closet = thisFar
      color  = color_list[x]

  return color

#  
# END compare()
###############################################################




###############################################################
# Image resizeing
# resize()

# NOTES: do a proportional avarage of RGB from a specified area, make it one pixel.
# 
# calculate, make new blank image and start inserting compiled data.

#640 width
#480 height 


def resize():
  
  mynewpic = makeEmptyPicture(640,480,white) # make blank canvas.
  
  global width
  global height
  
  #getcontext().prec = 3
  
  pixlesX = Decimal(width)/Decimal(640)   # number of pixles to analyse across
  pixlesY = Decimal(height)/Decimal(480)  # number of pixles to analyse down
  
  
  
  printNow(width)
  printNow(height)
  printNow(pixlesX)
  printNow(pixlesY)
  

#
# END Image resizing
###############################################################




###############################################################
# compareRGB()
# compare the R G B separately to select the closest color
# similar to top, but made my own algorithm

def compareRGB(pixColor, cList):

  newSum = 9000 # Start large and swap with lowest value, iteravely.
  oldSum = newSum
  color = white
  
  # Get RGB values of pixle
  pcR = getRed  (pixColor)
  pcG = getGreen(pixColor)
  pcB = getBlue (pixColor)
  
  
  for x in cList:
    
    # Get RGB value from currnt color in list
    clR = x.myRed()
    clG = x.myGreen()
    clB = x.myBlue()
    
    # Absolute value for comparison.   
    difR = math.fabs(clR-pcR)
    difG = math.fabs(clG-pcG)
    difB = math.fabs(clB-pcB)
    
    newSum = difR + difG + difB
    
    if oldSum > newSum:
      oldSum = newSum
      color  = makeColor(clR, clG, clB)  
  
  return color

#
# END compareRGB()
###############################################################


###############################################################
# MAIN
#
for i in range (0, width):          # iterate from top to bottom of image
  for j in range (0, height):       # iterate from left to right of image
    pix   = getPixel (myImg,i,j)    
    myCol = getColor (pix)
    
    #makeItThisColor = compare(myCol, color_list)  # call compare to get color
    makeItThisColor = compareRGB(pix, cList)       # call new compare 
    setColor(pix, makeItThisColor)                 # set new color

# resize()
show(myImg)    #show picture


newFileName = requestString("Name new file")
filePath    = pickAFolder()

writePictureTo(myImg,filePath+newFileName+".jpg")

#
# end MAIN
###############################################################



###############################################################
#
# NOTES


# resize idea
# take original, resize, then color swap.


# 0. show before
# 1. get pixle
# 2. get rgb value
# 3. compare to color list (white, black, red, orange, yellow, blue, indigo, violet )
# 4. select closest color and convert to that color.
# 5. show after

# math idea.  closest to zero, absolute value.
# compare to 255 first then move onto other colors.
# if,   any of the colors on list, break and leave a lone. 
# else, otherwise start check.

#convert image height to this
#640 width
#480 height
