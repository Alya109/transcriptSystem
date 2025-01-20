# This work done by group ##:
# Araja, Prince Jeoff, {studentID}, {contribution}
# Lumabi, Earl Vanesse, 2024-04985-MN-0, {contribution}
# Modesto, Isaiah, 2024-16637-MN-0, {contribution}
# Rivera, Robert Aron, 2024-04019-MN-0, {contribution}

import time
import pandas as pd
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

def loadDetailsFile(filename):
    stdDetails = pd.read_csv(filename)
    

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
    # Print the menu details
    print("\n\033[1mStudent Transcript Generation System\033[0m")
    print("======================================")
    print("1. Student Details\n2. Statistics\n3. Transcript based on major courses")
    print("4. Transcript based on minor courses\n5. Full Transcript\n6. Previous transcript request")
    print("7. Select another student\n8. Terminate the system")
    print("======================================")
    featureChoice = int(input("\033[1mEnter your feature (1-8): \033[0m"))
    return featureChoice

# Details Feature showing students personal information
def detailsFeature(name, stdID, levels, terms, college, dept):
    print(f"Name: {name}")
    print(f"Student ID: {stdID}")
    print(f"Level(s): {levels}")
    print(f"Number of terms: {terms}")
    print(f"College(s): {college}")
    print(f"Department(s): {dept}")

    sleep(1)

    
# Statistics Feature shows student's records
def statisticsFeature():

# Major Transscript shows students transscript of record based on their major courses
def majorTranscriptFeature():

# Minor Transscript shows students transcript of record based on their minor courses
def minorTranscriptFeature():

# Full Transscript shows students transcript of record on both major and minor courses
def fullTranscriptFeature():

# Previous Request shows students recent request
def previousRequestsFeature():

# New Student Feature allows another student after clearing all previous data
def newStudentFeature():

# Terminate Feature shows the number of request during the session
def terminateFeature():

def main():

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



