# This work done by group ##:
# Araja, Prince Jeoff, {studentID}, {contribution}
# Lumabi, Earl Vanesse, {studentID}, {contribution}
# Modesto, Isaiah, {studentID}, {contribution}
# Rivera, Robert Aron, {studentID}, {contribution}

import time
import numpy
import os

# Clears the console output
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def sleep():
  time.sleep(2)

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
  
  sleep()
  menuFeature()
  return level, degree
    
def menuFeature():
  print("\n\033[1mStudent Transcript Generation System\033[0m")
  print("======================================")
  print("1. Student Details\n2. Statistics\n3. Transcript based on major courses")
  print("4. Transcript based on minor courses\n5. Full Transcript\n6. Previous transcript request")
  print("7. Select another student\n8. Terminate the system")
  print("======================================")
  featureChoice = int(input("\033[1mEnter your feature (1-8): \033[0m"))
  return featureChoice

def detailsFeature():

def statisticsFeature():

def majorTranscriptFeature():

def minorTranscriptFeature():

def fullTranscriptFeature():

def previousRequestsFeature():

def newStudentFeature():

def terminateFeature():

def main():






