#Program:  paintMIDI image converter
#Name:     Carlos Espinoza
#Date:     
#
#Description:


#from jarray import array      # import array function

myImg  = pickAFile()          #get a file from user
myImg  = makePicture(myImg)   #take file path and turn into picture

width  = getWidth(myImg)
height = getHeight(myImg)



##########################################################
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
    
#end OBJECT
#########################################################


#make list of colors for comparison
wt = makeColor(255, 255, 255)
bk = makeColor(0,   0,   0)
rd = makeColor(255, 0,   0)
og = makeColor(255, 165, 0)
yl = makeColor(255, 255, 0)
gr = makeColor(0,   255, 0)
bl = makeColor(0,   0,   255)
vi = makeColor(143, 0,   255)


# take and sort list by value, look at jeremys email to get values.
color_list = [rd, og, yl, gr, bl, vi, wt, bk]


wtL = RGB(255, 255, 255)
bkL = RGB(0,   0,   0)
rdL = RGB(255, 0,   0)
ogL = RGB(255, 165, 0)
ylL = RGB(255, 255, 0)
grL = RGB(0,   255, 0)
blL = RGB(0,   0,   255)
viL = RGB(143, 0,   255)

cList = [rdL, ogL, ylL, grL, blL, viL, wtL, bkL]




maxDiff = 0

###############################################################
# compare()
#
# check pixle that is passed in
# find the closest color in our color list
# return the color in our list
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
  
# END compare()
###############################################################



###############################################################
# compareRGB()
# compare the R G B separately to select the closest color
# similar to top, but made my own algorithm

def compareRGB(pixColor, cList):

  newSum = 9000 # similar value 200 to start with.
  oldSum = newSum
  color = white
  global maxDiff
  
  # Get RGB values of pixle
  pcR = getRed  (pixColor)
  pcG = getGreen(pixColor)
  pcB = getBlue (pixColor)
  
  size = len(cList)
  
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
    
    
    if newSum > oldSum:
      maxDiff = newSum
    
    
    if oldSum > newSum:
      oldSum = newSum
      color  = makeColor(clR, clG, clB)
  
  
  return color





# END compareRGB()
###############################################################


for i in range (0, width):          # iterate from top to bottom of image
  for j in range (0, height):       # iterate from left to right of image
    pix   = getPixel (myImg,i,j)    
    myCol = getColor (pix)
    
    #makeItThisColor = compare(myCol, color_list)  # call compare to get color
    makeItThisColor = compareRGB(pix, cList)  # call new compare 
    setColor(pix, makeItThisColor)                # set new color

printNow(maxDiff)

show(myImg)    #show picture



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
