import time
import numpy


# Note: No global variables


# Start feature asking for student level and degree
def startFeature():
  print("Select Student Level:")
  print("U - Undergraduate")
  print("G - Graduate")
  print("B - Both")
  level = input("Enter your choice (U/G/B): ").upper()
  
  if level in ["G", "B"]:
    print("M - Master")
    print("D - Doctorate")
    print("B0 - Both")
    degree = input("Degree level: ").upper()
  
  time.sleep(3)
  menuFeature
  return level, degree
    
  # No degree feature as of now :(
def menuFeature():
  print("Student Transcript Generation System")
  print("======================================")
  print("")
  print("")

def whateverFeatureThisIs():

def featureOne():

def featureTwo():




