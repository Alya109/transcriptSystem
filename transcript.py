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
    return stdDetails

def studentIDCheck(stdID, stdDetails):
    while str(stdID).strip() not in stdDetails["stdID"].astype(str).str.strip().values:
        print("Invalid ID. Please try again.")
        stdID = input("Enter student ID: ")
    return stdID
    

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
        
    sleep(1)
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
    
    if featureChoice == 1:
        detailsFeature(stdID, stdDetails)
    elif featureChoice == 2:
        statisticsFeature(stdID, stsDetails)
    elif featureChoice == 3:
        majorTranscriptFeature(stdID, stdDetails)
    elif featureChoice == 4:
        minorTranscriptFeature(stdID, stdDetails)
    elif featureChoice == 5:
        fullTranscriptFeature(stdID, stdDetails)
    elif featureChoice == 6:
        previousRequestsFeature(stdID, stdDetails)
    elif featureChoice == 7:
        newStudentFeature(stdID, stdDetails)
    elif featureChoice == 8:
        terminateFeature(stdID, stdDetails)
    else:
        return "Invalid choice. Please try again."

# Details Feature showing students personal information
def detailsFeature(stdID, stdDetails):
    details = stdDetails.loc[stdDetails["ID"] == stdID]
    
    detailsStd = f"{stdID}details.txt"
    
    with open(details, "w") as file:
        for column in details.columns:
            stdRecord = f"{column}: {details.iloc[0][column]}"
            print(stdRecord)
            file.write(stdRecord + "\n")
    sleep(2)
    # Haven't tested it yet
    
# Statistics Feature shows student's records
def statisticsFeature(stdID, stdDetails):
    courseData = stdDetails.loc[stdDetails["ID"] == stdID]
    # For visual purposes
    # Undergraduate level
    print("===============================")
    print("****** {levels} Level ******")
    print("===============================")
    print("Overall average (major and minor) for all terms: ")
    print("Average (major and minor) for each term: ")
    print("      Term 1: ")
    print("      Term 2: ")
    print("      Term 3: ")
    print("Maximum grade(s) and in which term(s): ")
    print("Minimum grade(s) and in which term(s): ")
    print("Do you have any repeated course(s)? ")
    # Graduate Level
    print("===============================")
    print("****** Graduate(M) Level ******")
    print("===============================")
    print("Overall average (major and minor) for all terms: ")
    print("Average (major and minor) for each term: ")
    print("      Term 1: ")
    print("      Term 2: ")
    print("      Term 3: ")
    print("Maximum grade(s) and in which term(s): ")
    print("Minimum grade(s) and in which term(s): ")
    print("Do you have any repeated course(s)? ")

# Major Transscript shows students transscript of record based on their major courses
def majorTranscriptFeature():
    details = stdDetails.loc[stdDetails["ID"] == stdID]
    # Visualization purposes for major courses
    print("Name:                 stdID:                 ")
    print("College:              Department:            ")
    print("Major:                Minor:                 ")
    print("Level:                Number of terms:       ")
    print("=============================================")
    print("**************      Term 1     **************")
    print("=============================================")
    print("course ID  course name  credit hours  grade  ")
    print("c1         course 1     3             80     ")
    print("c2         course 2     4             90     ")
    print("Major average =         Overall average =    ")
    print("=============================================")
    print("        End of Transcript for Level(U)       ")
    print("=============================================")

# Minor Transscript shows students transcript of record based on their minor courses
def minorTranscriptFeature():
    details = stdDetails.loc[stdDetails["ID"] == stdID]
    # Visualization purposes for minor courses
    print("Name:                 stdID:                 ")
    print("College:              Department:            ")
    print("Major:                Minor:                 ")
    print("Level:                Number of terms:       ")
    print("=============================================")
    print("**************      Term 1     **************")
    print("=============================================")
    print("course ID  course name  credit hours  grade  ")
    print("c1         course 1     3             80     ")
    print("c2         course 2     4             90     ")
    print("Major average =         Overall average =    ")
    print("=============================================")
    print("        End of Transcript for Level(U)       ")
    print("=============================================")


# Full Transscript shows students transcript of record on both major and minor courses
def fullTranscriptFeature():
    details = stdDetails.loc[stdDetails["ID"] == stdID]
    # Visualization for full transcript showing both minor and major courses
    print("Name:                 stdID:                 ")
    print("College:              Department:            ")
    print("Major:                Minor:                 ")
    print("Level:                Number of terms:       ")
    print("=============================================")
    print("**************      Term 1     **************")
    print("=============================================")
    print("course ID  course name  credit hours  grade  ")
    print("c1         course 1     3             80     ")
    print("c2         course 2     4             90     ")
    print("Major average =         Overall average =    ")
    print("=============================================")
    print("        End of Transcript for Level(U)       ")
    print("=============================================")


# Previous Request shows students recent request
def previousRequestsFeature():
    
    print("=============================================")
    print("  Request          Date           Time       ")
    print("=============================================")
    print("  Major          22/09/2020      13:30:09    ")
    print("  Full           12/02/2021      14:40:03    ")

# New Student Feature allows another student after clearing all previous data
def newStudentFeature():

# Terminate Feature shows the number of request during the session
def terminateFeature():
    print("Terminating the system. Goodbye!")
    exit()

def main():

