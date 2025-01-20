# This work done by group ##:
# Araja, Prince Jeoff, {studentID}, {contribution}
# Lumabi, Earl Vanesse, 2024-04985-MN-0, {contribution}
# Modesto, Isaiah, {studentID}, {contribution}
# Rivera, Robert Aron, 2024-04019-MN-0, {contribution}

import time
import numpy as np
import os

# Clears the console output
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# Sleep function to let the program rest for a few seconds
def sleep(mode):
    # Mode 1 for 2 second rest
    if mode == 1:
        time.sleep(2)
    # Mode 2 for 4 second rest
    elif mode == 2:
        time.sleep(4)

def loadDetailsFile():

# Start feature asking for student level and degree
def startFeature():
    print("Select Student Level:")
    print("U - Undergraduate")
    print("G - Graduate")
    print("B - Both")
    # Loop for input
    while True:
        level = input("Enter your choice (U/G/B): ").upper()
        if level in ["U", "G", "B"]:
            break
        print("Invalid choice. Please try again.")

    if level in ["G", "B"]:
        print("M - Master")
        print("D - Doctorate")
        print("B0 - Both")
        while True:
            degree = input("Degree level (M/D/B0): ").upper()
            if degree in ["M", "D", "B0"]:
                break
            print("Invalid choice. Please try again.")
    while True:
        stdID = input("Enter student ID: ")
        


    sleep(1)
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
    # Di pa ayos to
    if featureChoice == 1:
        detailsFeature()
    elif featureChoice == 2:
        statisticsFeature()
    elif featureChoice == 3:
        majorTranscriptFeature()
    elif featureChoice == 4:
        minorTranscriptFeature()
    elif featureChoice == 5:
        fullTranscriptFeature()
    elif featureChoice == 6:
        previousRequestsFeature()
    elif featureChoice == 7:
        newStudentFeature()
    elif featureChoice == 8:
        terminateFeature()
    else:
        return "Invalid choice. Please try again."


def detailsFeature():
    studentDetails = f"Name: {studentData[0]}\nstdID: {studentData[1]}\nLevel(s): {studentData[2]}\nNumber of terms: {studentData[3]}\n"
def statisticsFeature():

def majorTranscriptFeature():

def minorTranscriptFeature():

def fullTranscriptFeature():

def previousRequestsFeature():

def newStudentFeature():

def terminateFeature():

def main():

    

