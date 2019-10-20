# myColourModule.py
# Decription: Module containing colour related functions
# Author: AL
# Date: July 2019

def isPixelGreen(R,G,B) :
  """Returns True if the pixel is green,
     False otherwise."""
  # if R < 180 and R >= 0 and G > 230 and G <= 255 and B < 120 and B >= 0 :
  #   answer = True
  # else :
  #   answer = False
  # return answer
  return R < 180 and R >= 0 and G > 230 and G <= 255 and B < 120 and B >= 0


def isPixelBlue(R,G,B) :
  """Returns True if the pixel is green,
     False otherwise."""
  # if R < 180 and R >= 0 and G > 230 and G <= 255 and B < 120 and B >= 0 :
  #   answer = True
  # else :
  #   answer = False
  # return answer
  return R < 180 and R >= 0 and B > 130 and B <= 255 and G < 120 and G >= 0