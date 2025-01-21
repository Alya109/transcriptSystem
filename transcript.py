# This work done by group ##:
# Araja, Prince Jeoff, 2024-04758-MN-0, {contribution}
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
    while stdDetails.loc[stdDetails['stdID'] == int(stdID)].empty:
        print("Invalid ID. Please try again.")
        stdID = input("Enter student ID: ")
    return stdID
    
# Start feature asking for student level and degree
def startFeature():

    levels = []
    degrees = []
    print("Select Student Level:")
    print("U - Undergraduate")
    print("G - Graduate")
    print("B - Both")
    # Loop for input in-case the level inputted isn't in the choices
    while True:
        level = input("Enter your choice (U/G/B): ").upper()
        if level in ["U", "G", "B"]:
            if level == "U":
                levels.append("U")
            if level == "G":
                levels.append("G")
            if level == "B":
                levels.append("U")
                levels.append("G")
            break
        print("Invalid choice. Please try again.")
    
    # Degree input loop
    if level in ["G", "B"]:
        print("M - Master")
        print("D - Doctorate")
        print("B0 - Both")
        while True:
            degree = input("Degree level (M/D/B0): ").upper()
            if degree in ["M", "D", "B0"]:
                if degree == "M":
                    degrees.append("M")
                if degree == "D":
                    degrees.append("D")
                if degree == "B0":
                    degrees.append("M")
                    degrees.append("D")
                break
            print("Invalid choice. Please try again.")
        
    sleep(1)
    return level, degree
    
def menuFeature(stdID, levels, degrees):
    # Print the menu details
    print("\n\033[1mStudent Transcript Generation System\033[0m")
    print("======================================")
    print("1. Student Details\n2. Statistics\n3. Transcript based on major courses")
    print("4. Transcript based on minor courses\n5. Full Transcript\n6. Previous transcript request")
    print("7. Select another student\n8. Terminate the system")
    print("======================================")
    featureChoice = int(input("\033[1mEnter your feature (1-8): \033[0m"))

    requestCount += 1
    if featureChoice == 1:
        detailsFeature(stdID, stdDetails, levels, degrees)
        recordRequest(stdID, "Student Details")
    elif featureChoice == 2:
        statisticsFeature(stdID, stdDetails, levels, degrees)
        recordRequest(stdID, "Statistics")
    elif featureChoice == 3:
        majorTranscriptFeature(stdID, stdDetails, levels, degrees)
        recordRequest(stdID, "Major Transcript")
    elif featureChoice == 4:
        minorTranscriptFeature(stdID, stdDetails, levels, degrees)
        recordRequest(stdID, "Minor Transcript")
    elif featureChoice == 5:
        fullTranscriptFeature(stdID, stdDetails, levels, degrees)
        recordRequest(stdID, "Full Transcript")
    elif featureChoice == 6:
        previousRequestsFeature(stdID)
        recordRequest(stdID, "Previous Requests")
    elif featureChoice == 7:
        newStudentFeature()
    elif featureChoice == 8:
        terminateFeature(requestCount)
    else:
        print("Invalid choice. Please try again.")
    return requestCount

# Details Feature showing students personal information
def detailsFeature(stdID, stdDetails, levels, degrees):

    valueCheck = False
    sd = loadDetailsFile(stdDetails)
    dataFilter = sd[(sd["stdID"] == int(stdID)) & (
        sd["Level"].isin(level)) & (sd["Degree"].isin(degree))]
    if dataFilter.empty:
        print("No data was found with the data you entered.\n")
        return
    levels = dataFilter["Levels"].unique()
    detailDisplay = ""
    detailDisplay += f"Name: {dataFilter["Name"].iloc[0]}\n" \
              f"stdID: {dataFilter["stdID"].iloc[0]}\n" \
              f"Level(s): {", ".join(levels)}\n" \
              f"Number of terms: {dataFilter["Terms"].sum(0)}\n" \
              f"College(s): {", ".join(dataFilter["College"].unique().tolist())}\n" \
              f"Department(s): {", ".join(dataFilter["Department"].unique().tolist())}"
    
    valueCheck = True
    
    exportInfo = f"std{stdID}details.txt"
    with open(exportInfo, 'w') as info:
        info.write(detailDisplay)
    print(detailDisplay)
    sleep(2)
    # Haven't tested it yet
    
# Statistics Feature shows student's records
def statisticsFeature(stdID, stdDetails, levels, degrees):
    valueCheck = False
    sd = loadDetailsFile(stdDetails)
    statsDisplay = ""
    
    for level in levels:
        if level == "U":
            levelName = "Undergraduate"
        else:
            levelName = "Graduate"
        for degree in degrees:
            dataFilter = sd[(sd['Level'] == level) and (sd['Degree'] == degree)]
            if dataFilter.empty:
                continue
            overallAverage = dataFilter['Grade'].mean()
            aveTerm = dataFilter.groupby('Term')['Grade'].mean()
            maxTerm = dataFilter['Grade'].max()
            maxGrades = dataFilter[dataFilter['Grade'] == termMax]
            minTerm = dataFilter['Grade'].min()
            minGrades = dataFilter[dataFilter['Grade'] == termMin]
            
            statsTitle = f"     {levelName} ({degree}) Level     "
            statsDisplay += "=" * 50 + "\n"
            statsDisplay += f"{statTitle.center(50, *'*')}\n"
            statsDisplay += "=" * 50 + "\n"
            statsDisplay += f"Overall average (major and minor) for all terms: {overallAverage:.2f}\n"
            statsDisplay += "Average (major and minor) of each term:\n"
            for term, avg in aveTerm.items():
                statsDisplay += f"\tTerm {term}: {avg:.2f}\n"
            statsDisplay += "Maximum grade(s) and in which term(s):\n"
            for _, row in maxGrades.iterrows():
                statsDisplay += f"\tTerm {row['Term']}: {row['Grade']}\n"
            statsDisplay += "Minimum grade(s) and in which term(s):\n"
            for _, row in minGrades.iterrows():
                statsDisplay += f"\tTerm {row['Term']}: {row['Grade']}\n"
            valueCheck = True
        if valueCheck:
            exportInfo = f"std{stdID}statistics.txt"
            with open(exportInfo, 'w') as info:
                info.write(statsDisplay)
            print(statsDisplay)
        else:
        # Prints if no data was found
        print('No data was found with the data you entered\n')
    sleep(2)
    
# Major Transcript shows students transscript of record based on their major courses
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
def previousRequestsFeature(stdID):
    with open("{stdID}previousRequest.txt", "r") as request:
        request.read()
    print("=============================================")
    print("  Request          Date           Time       ")
    print("=============================================")
    print("  Major          22/09/2020      13:30:09    ")
    print("  Full           12/02/2021      14:40:03    ")

# New Student Feature allows another student after clearing all previous data
def newStudentFeature():
    print("Clearing cache...")
    cls()
    sleep(1)
    main()


# Terminate Feature shows the number of request during the session
def terminateFeature():
    print("Terminating the system. Goodbye!")
    exit()

def recordRequest(stdID, requestDetails):
    
    # Ewan di ko pa naaayos
    with open("{stdID}previousRequest.txt", "a+") as prevReq:
        prevReq.write(f"")

def main():
    
    stdDetails = loadDetailsFile("studentDetails.csv")
    sleep(1)
    
    # Get user input for student level and degree
    level, degree = startFeature()
    
    # Gets studentID and checks if it matches the stdID in the database
    stdID = input("Enter your student ID: ")
    stdID = studentIDCheck(stdID, stdDetails)
    
    requestCount = 0
    while True:
        requestCount = menuFeature(stdID, stdDetails, requestCount)


