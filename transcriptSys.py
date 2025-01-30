# This work done by Group #7:
# Araja, Prince Jeoff, 2024-04758-MN-0, 21%
# Lumabi, Earl Vanesse, 2024-04985-MN-0, 30%
# Modesto, Isaiah, 2024-16637-MN-0, 21%
# Rivera, Robert Aron, 2024-04019-MN-0, 28%

import time
import datetime
import pandas as pd
import os

"""
======================
   System Functions
======================
"""
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
    try:
        return pd.read_csv(filename)
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
        exit()
    
def studentIDCheck(stdID, stdDetails):
    while str(stdID) not in stdDetails['stdID'].astype(str).values:
        print("Invalid ID. Please try again.")
        stdID = input("Enter student ID: ").strip()
    return stdID
"""
===========================
    Transcript Features
===========================
"""
# Start feature asking for student level and degree
def startFeature():

    levels, degrees = [], []
    print("=" * 40)
    print("Select Student Level:")
    print("U - Undergraduate")
    print("G - Graduate")
    print("B - Both")
    print("=" * 40)
    # Loop for input in-case the level inputted isn't in the choices
    while True:
        level = input("Enter your choice (U/G/B): ").upper().strip()
        if level in ["U", "G", "B"]:
            if level == "U":
                levels.append("U")
                degrees.append("BD")
            if level == "G":
                levels.append("G")
            if level == "B":
                levels.append("U")
                degrees.append("BD")
                levels.append("G")
            break
        print("Invalid choice. Please try again.")
    
    # Degree input loop
    if level in ["G", "B"]:
        print("=" * 40)
        print("M - Master")
        print("D - Doctorate")
        print("B0 - Both")
        print("=" * 40)
        while True:
            degree = input("Degree level (M/D/B0): ").upper().strip()
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
    return levels, degrees
    
def menuFeature(stdID, stdDetails, levels, degrees, requestCount, requests):
    cls()
    # Print the menu details
    print(
        "\n\033[1mStudent Transcript Generation System\033[0m\n"
        + "=" * 40 + "\n"
        + "1. Student Details\n"
        + "2. Statistics\n"
        + "3. Transcript based on major courses\n"
        + "4. Transcript based on minor courses\n"
        + "5. Full Transcript\n"
        + "6. Previous transcript request\n"
        + "7. Select another student\n"
        + "8. Terminate the system\n"
        + "=" * 40 + "\n"
    )
    featureChoice = int(input("\033[1mEnter your feature (1-8): \033[0m"))

    if featureChoice == 1:
        detailsFeature(stdID, stdDetails, levels, degrees)
        recordRequest(stdID, "Student Details", requests)
        requestCount += 1
    elif featureChoice == 2:
        statisticsFeature(stdID, levels, degrees)
        recordRequest(stdID, "Statistics", requests)
        requestCount += 1
    elif featureChoice == 3:
        majorTranscriptFeature(stdID, stdDetails, levels, degrees)
        recordRequest(stdID, "Major Transcript", requests)
        requestCount += 1
    elif featureChoice == 4:
        minorTranscriptFeature(stdID, stdDetails, levels, degrees)
        recordRequest(stdID, "Minor Transcript", requests)
        requestCount += 1
    elif featureChoice == 5:
        fullTranscriptFeature(stdID, stdDetails, levels, degrees)
        recordRequest(stdID, "Full Transcript", requests)
        requestCount += 1
    elif featureChoice == 6:
        previousRequestsFeature(stdID)
        recordRequest(stdID, "Previous Requests", requests)
        requestCount += 1
    elif featureChoice == 7:
        newStudentFeature()
        requestCount += 1
    elif featureChoice == 8:
        terminateFeature(requestCount)
    else:
        print("Invalid choice. Please try again.")
    return requestCount
# Details Feature showing students personal information
def detailsFeature(stdID, stdDetails, levels, degrees):
    details = stdDetails
    
    studentInfo = details[(details["stdID"] == int(stdID)) & (
        details["Level"].isin(levels)) & (details["Degree"].isin(degrees))]
    detailInfo = (
        f"Name: {studentInfo['Name'].iloc[0]}\n"
        f"stdID: {stdID}\n"
        f"Level(s): {', '.join(levels)}\n"
        f"Number of Terms: {studentInfo['Terms'].sum(0)}\n"
        f"College(s): {', '.join(studentInfo['College'].unique().tolist())}\n"
        f"Department(s): {', '.join(studentInfo['Department'].unique().tolist())}"
    )
    detailFile = f"std{stdID}details.txt"
    with open(detailFile, "w") as file:
        file.write(detailInfo)
    print(detailInfo)
    sleep(2)
    cls()
    
# Statistics Feature shows student's records
def statisticsFeature(stdID, levels, degrees):
    stdData = pd.read_csv(f"{stdID}.csv")
    
    statDisplay = ""
    if levels == ["U"]:
        for degree in degrees:
            degreeData = stdData[(stdData["Level"].isin(levels)) & (stdData["Degree"].isin(degrees))]
            overallAverage = degreeData["Grade"].mean()
            statDisplay += "=" * 40
            statDisplay += f"\n********** Undergraduate **********\n"
            statDisplay += "=" * 40
            statDisplay += f"\nOverall Average (major and minor) for all terms: {overallAverage:.2f}\n"
            statDisplay += f"Average (major and minor) of each term: \n"
            
            terms = degreeData["Term"].unique()
            for index in terms:
                average = degreeData[(degreeData["Term"] == index)]["Grade"].mean()
                statDisplay += f"Term {index}: {average:.2f}\n"
            maxGrade = degreeData[degreeData["Grade"] == degreeData["Grade"].max()]
            minGrade = degreeData[degreeData["Grade"] == degreeData["Grade"].min()]
            
            statDisplay += f"\nMinimum grade(s) and in which term(s): Term: {minGrade['Term'].iloc[0]}, Grade: {minGrade['Grade'].iloc[0]}"
            statDisplay += f"\nMaximum grade(s) and in which term(s): Term: {maxGrade['Term'].iloc[0]}, Grade: {maxGrade['Grade'].iloc[0]}"
    elif levels == ["G"] or levels == ["U", "G"]:
        for degree in degrees:
            degreeData = stdData[(stdData["Level"].isin(levels)) & (stdData["Degree"].isin(degrees))]
            overallAverage = degreeData["Grade"].mean()
            
            statDisplay += "=" * 40
            statDisplay += f"\n******** Graduate {degree} ********\n"
            statDisplay += "=" * 40
            statDisplay += f"\nOverall Average (major and minor) for all terms: {overallAverage:.2f}\n"
            statDisplay += f"Average (major and minor) of each term: \n"
            
            terms = degreeData["Term"].unique()
            for index in terms:
                average = degreeData[(degreeData["Term"] == index)]["Grade"].mean()
                statDisplay += f"Term {index}: {average:.2f}\n"
            repeatedCourses = degreeData[degreeData.courseName.duplicated()]
            if not repeatedCourses.empty:
                repeated = f"Yes, {repeatedCourses['courseName'].iloc[0]}"
            else:
                repeated = "No"
            maxGrade = degreeData[degreeData["Grade"] == degreeData["Grade"].max()]
            minGrade = degreeData[degreeData["Grade"] == degreeData["Grade"].min()]
            statDisplay += f"Minimum grade(s) and in which term(s): Term: {minGrade['Term'].iloc[0]}, Grade: {minGrade['Grade'].iloc[0]}\n"
            statDisplay += f"\nMaximum grade(s) and in which term(s): Term: {maxGrade['Term'].iloc[0]}, Grade: {maxGrade['Grade'].iloc[0]}\n"
            statDisplay += f"Do you have any repeated course(s)? {repeated}"
    print(statDisplay)
    statsFile = f"std{stdID}statistics.txt"
    with open(statsFile, "w") as stats:
        stats.write(statDisplay)
    sleep(2)
    cls()

# Major Transcript shows students transscript of record based on their major courses
def majorTranscriptFeature(stdID, stdDetails, levels, degrees):
    stdInfo = pd.read_csv(f'{stdID}.csv')
    
    majorDisplay = ""
    for level in levels:
        for degree in degrees:
            majorData = stdDetails[(stdDetails['stdID'] == int(stdID)) & (
                stdDetails['Level'] == level) & (stdDetails['Degree'] == degree)]
            if majorData.empty:
                continue
            border = 60 * "=" + "\n"
            footer = f"     Major Transcript for Level ({level} - {degree})     "
            majorDisplay += border
            majorDisplay += f"{footer.center(60, '*')}\n"
            majorDisplay += f"{border}\n"
            majorDisplay += f"Name: {majorData['Name'].iloc[0]}\t\t\t"
            majorDisplay += f"stdID: {majorData['stdID'].iloc[0]}\n"
            majorDisplay += f"College: {majorData['College'].iloc[0]}\t\t\t\t"
            majorDisplay += f"Department: {majorData['Department'].iloc[0]}\n"
            majorDisplay += f"Major: {majorData['Major'].iloc[0]}\t\t\t"
            majorDisplay += f"Minor: {majorData['Minor'].iloc[0]}\n"
            majorDisplay += f"Level: {majorData['Level'].iloc[0]}\t\t\t\t"
            majorDisplay += f"Number of terms: {majorData['Terms'].sum()}\n\n"
            
            stdDataFilter = stdInfo[(stdInfo['Level'] == level) & (
                stdInfo['Degree'] == degree)]
            
            terms = stdDataFilter['Term'].unique()
            
            for term in terms:
                termDataFilter = stdDataFilter[(stdDataFilter['Term'] == term)]
                majorDataFilter = termDataFilter[termDataFilter['courseType'] == 'Major']
                titleTerm = f"     Term ({term})     "
                border = 60 * "=" + "\n"
                majorDisplay += border
                majorDisplay += f"{titleTerm.center(60, '*')}\n"
                majorDisplay += border
                majorDisplay += "{:<20} {:<20} {:<20} {:<20}\n".format(
                    "courseID", "courseName", "creditHours", "Grade")
                for row in majorDataFilter.itertuples(index=False):
                    majorDisplay += "{:<20} {:<20} {:<20} {:<20}\n".format(
                        row.courseID, row.courseName, row.creditHours, row.Grade)
                
                majorAve = majorDataFilter['Grade'].mean()
                overallAve = termDataFilter['Grade'].mean()
                
                majorDisplay += "\n\n"
                majorDisplay += f"Major Average: {majorAve:.2f}   \t\t\t"
                majorDisplay += f"Overall Average: {overallAve:.2f}\n\n"
            footer = f"     End of Transcript for Level ({level} - {degree})     "
            majorDisplay += border
            majorDisplay += f"{footer.center(60, '*')}\n"
            majorDisplay += border

    print(majorDisplay)
    exportInfo = f"std{stdID}MajorTranscript.txt"
    with open(exportInfo, 'w') as major:
        major.write(majorDisplay)
    sleep(2)
    cls()

# Minor Transcript shows students transcript of record based on their minor courses
def minorTranscriptFeature(stdID, stdDetails, levels, degrees):
    stdInfo = pd.read_csv(f'{stdID}.csv')
    minorDisplay = ""

    for level in levels:
        for degree in degrees:
            minorData = stdDetails[(stdDetails['stdID'] == int(stdID)) & (
                stdDetails['Level'] == level) & (stdDetails['Degree'] == degree)]
            if minorData.empty:
                continue
            border = 60 * "=" + "\n"
            footer = f"     Minor Transcript for Level ({level} - {degree})     "
            minorDisplay += border
            minorDisplay += f"{footer.center(60, '*')}\n"
            minorDisplay += f"{border}\n"
            minorDisplay += f"Name: {minorData['Name'].iloc[0]}\t\t\t"
            minorDisplay += f"stdID: {minorData['stdID'].iloc[0]}\n"
            minorDisplay += f"College: {minorData['College'].iloc[0]}\t\t\t\t"
            minorDisplay += f"Department: {minorData['Department'].iloc[0]}\n"
            minorDisplay += f"Major: {minorData['Major'].iloc[0]}\t\t\t"
            minorDisplay += f"Minor: {minorData['Minor'].iloc[0]}\n"
            minorDisplay += f"Level: {minorData['Level'].iloc[0]}\t\t\t\t"
            minorDisplay += f"Number of terms: {minorData['Terms'].sum()}\n\n"
            
            stdDataFilter = stdInfo[(stdInfo['Level'] == level) & (
                stdInfo['Degree'] == degree)]
            
            terms = stdDataFilter['Term'].unique()
            
            for term in terms:
                termDataFilter = stdDataFilter[(stdDataFilter['Term'] == term)]
                minorDataFilter = termDataFilter[termDataFilter['courseType'] == 'Minor']
                titleTerm = f"     Term ({term})     "
                border = 60 * "=" + "\n"
                minorDisplay += border
                minorDisplay += f"{titleTerm.center(60, '*')}\n"
                minorDisplay += border
                minorDisplay += "{:<20} {:<20} {:<20} {:<20}\n".format(
                    "courseID", "courseName", "creditHours", "Grade")
                for row in minorDataFilter.itertuples(index=False):
                    minorDisplay += "{:<20} {:<20} {:<20} {:<20}\n".format(
                        row.courseID, row.courseName, row.creditHours, row.Grade)
                
                minorAve = minorDataFilter['Grade'].mean()
                overallAve = termDataFilter['Grade'].mean()
                
                minorDisplay += "\n\n"
                minorDisplay += f"Major Average: {minorAve:.2f}   \t\t\t"
                minorDisplay += f"Overall Average: {overallAve:.2f}\n\n"
            footer = f"     End of Transcript for Level ({level} - {degree})     "
            minorDisplay += border
            minorDisplay += f"{footer.center(60, '*')}\n"
            minorDisplay += border

    print(minorDisplay)

    exportInfo = f"std{stdID}MinorTranscript.txt"
    with open(exportInfo, 'w') as minor:
        minor.write(minorDisplay)
    sleep(2)
    cls()
	
# Full Transscript shows students transcript of record on both major and minor courses
def fullTranscriptFeature(stdID, stdDetails, levels, degrees):
    stdInfo = pd.read_csv(f'{stdID}.csv')
    fullDisplay = ""

    for level in levels:
        for degree in degrees:
            fullData = stdDetails[(stdDetails['stdID'] == int(stdID)) & (stdDetails['Level'] == level) & (stdDetails['Degree'] == degree)]
            if fullData.empty:
                continue
            border = 60 * "=" + "\n"
            footer = f"     Full Transcript for Level ({level} - {degree})     "
            fullDisplay += border
            fullDisplay += f"{footer.center(60, '*')}\n"
            fullDisplay += f"{border}\n"
            fullDisplay += f"Name: {fullData['Name'].iloc[0]}\t\t\t"
            fullDisplay += f"stdID: {fullData['stdID'].iloc[0]}\n"
            fullDisplay += f"College: {fullData['College'].iloc[0]}\t\t\t\t"
            fullDisplay += f"Department: {fullData['Department'].iloc[0]}\n"
            fullDisplay += f"Major: {fullData['Major'].iloc[0]}\t\t\t"
            fullDisplay += f"Minor: {fullData['Minor'].iloc[0]}\n"
            fullDisplay += f"Level: {fullData['Level'].iloc[0]}\t\t\t\t"
            fullDisplay += f"Number of terms: {fullData['Terms'].sum()}\n\n"

            stdDataFilter = stdInfo[(stdInfo['Level'] == level) & (stdInfo['Degree'] == degree)]
            terms = stdDataFilter['Term'].unique()
            
            for term in terms:
                termDataFilter = stdDataFilter[(stdDataFilter['Term'] == term)]
                minorDataFilter = termDataFilter[termDataFilter['courseType'] == 'Minor']
                majorDataFilter = termDataFilter[termDataFilter['courseType'] == 'Major']
                
                titleTerm = f"     Term ({term})     "
                border = 60 * "=" + "\n"
                fullDisplay += border
                fullDisplay += f"{titleTerm.center(60, '*')}\n"
                fullDisplay += border
                fullDisplay += "{:<20} {:<20} {:<20} {:<20}\n".format("courseID", "courseName", "creditHours", "Grade")
                
                for row in termDataFilter.itertuples(index=False):
                    fullDisplay += "{:<20} {:<20} {:<20} {:<20}\n".format(row.courseID, row.courseName, row.creditHours, row.Grade)
                
                fullDisplay += "\n\n"
                fullDisplay += f"Major Average: {majorDataFilter['Grade'].mean():.2f}   \t\t\t\t"
                fullDisplay += f"Minor Average: {minorDataFilter['Grade'].mean():.2f}\n"
                fullDisplay += f"Term Average: {termDataFilter['Grade'].mean():.2f}   \t\t\t\t"
                fullDisplay += f"Overall Average: {stdDataFilter['Grade'].mean():.2f}\n\n"
            
            footer = f"     End of Transcript for Level ({level} - {degree})     "
            fullDisplay += border
            fullDisplay += f"{footer.center(60, '*')}\n"
            fullDisplay += border

    fullFile = f"std{stdID}FullTranscript.txt"
    with open(fullFile, 'w') as full:
        full.write(fullDisplay)
            
    print(fullDisplay)
    sleep(2)
    cls()
        
# New Student Feature allows another student after clearing all previous data
def newStudentFeature():
    print("Clearing cache...")
    cls()
    sleep(1)
    main()

# Terminate Feature shows the number of request during the session
def terminateFeature(requestCount):
    cls()
    print(f"Number of requests this session: {requestCount}")
    print("Thank you for using the system!")
    sleep(1)
    exit()

def recordRequest(stdID, request, requests):
    timestamp = datetime.datetime.now()
    new_entry = {
        'request': request,
        'date': timestamp.strftime("%d/%m/%Y"),
        'time': timestamp.strftime("%I:%M %p")
    }
    
    filename = f"std{stdID}PreviousRequests.txt"
    
    # Write header if file doesn't exist
    if not os.path.exists(filename):
        with open(filename, "w") as f:
            f.write(f"{'Request':<20} {'Date':<15} {'Time':<20}\n")
            f.write("-" * 45 + "\n")
    
    # Append the new entry
    with open(filename, "a") as f:
        f.write(f"{request:<20} {new_entry['date']:<15} {new_entry['time']:<20}\n")
    
    return requests

def previousRequestsFeature(stdID):
    # Read from file instead of memory for reliability
    filename = f"std{stdID}PreviousRequests.txt"
    
    try:
        with open(filename, "r") as f:
            content = f.read()
            print(f"\nPrevious requests for {stdID}:")
            print(content or "No previous requests found")
    except FileNotFoundError:
        print("No previous requests found")
    
    sleep(1)

def main():
    requests = {}
    stdDetailsFile = "studentDetails.csv"
    stdDetails = loadDetailsFile(stdDetailsFile)
    
    while True:  # Loop to handle level/degree and student ID validation
        levels, degrees = startFeature()
        
        # Get student ID and validate existence
        stdID = input("Enter your student ID: ").strip()
        stdID = studentIDCheck(stdID, stdDetails)
        
        # Check if the student has data for the selected levels and degrees
        studentData = stdDetails[
            (stdDetails['stdID'] == int(stdID)) &
            (stdDetails['Level'].isin(levels)) &
            (stdDetails['Degree'].isin(degrees))
        ]
        sleep(1)
        if not studentData.empty:
            break  # Valid combination found, exit loop
        else:
            print("\nError: The student does not have records for the selected levels/degrees.\n")
            print("Please reselect levels/degrees or enter a different student ID.\n")
            cls()
    
    requestCount = 0
    while True:
        requestCount = menuFeature(stdID, stdDetails, levels, degrees, requestCount, requests)

if __name__ == "__main__":
    main()
