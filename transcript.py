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
    degree = input("Degree level (M/D/B0): ").upper()
  
  time.sleep(2)
  menuFeature()
  return level, degree
    
def menuFeature():
  print("\033[1mStudent Transcript Generation System\033[0m")
  print("======================================")
  print("1. Student Details\n2. Statistics\n3. Transcript based on major courses")
  print("4. Transcript based on minor courses\n5. Full Transcript\n6. Previous transcript request")
  print("7. Select another student\n8. Terminate the system")
  print("======================================")
  print("\033[1mEnter your feature: \033[0m")

def whateverFeatureThisIs():

def featureOne():

def featureTwo():




