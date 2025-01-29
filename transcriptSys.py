# This work done by group ##:
# Araja, Prince Jeoff, 2024-04758-MN-0, {contribution}
# Lumabi, Earl Vanesse, 2024-04985-MN-0, {contribution}
# Modesto, Isaiah, 2024-16637-MN-0, {contribution}
# Rivera, Robert Aron, 2024-04019-MN-0, {contribution}

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
    stdDetails = pd.read_csv(filename)
    return stdDetails
    
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
        
    # sleep(1)
    return levels, degrees
    
def menuFeature(stdID, stdDetails, levels, degrees, requestCount):
    
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
        recordRequest(stdID, "Student Details")
    elif featureChoice == 2:
        statisticsFeature(stdID, levels, degrees)
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
    return requestCount + 1

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
    exportInfo = f"std{stdID}details.txt"
    with open(exportInfo, "w") as file:
        file.write(detailInfo)
    print(detailInfo)
    # sleep(1)
    
# Statistics Feature shows student's records
def statisticsFeature(stdID, levels, degrees):
    studentData = pd.read_csv(f'{std_id}.csv')
    
    # major_avg = student_data[student_data['type'] == 'major']['grade'].mean()
    # minor_avg = student_data[student_data['type'] == 'minor']['grade'].mean()
    
    """
    valueCheck = False
    sd = loadDetailsFile(f"{stdID}.csv")
    statsDisplay = ""
    
    for level in levels:
        if level == "U":
            levelName = "Undergraduate"
        else:
            levelName = "Graduate"
        for degree in degrees:
            dataFilter = sd[(sd['Level'] == level) & (sd['Degree'] == degree)]
            if dataFilter.empty:
                continue
            overallAverage = dataFilter['Grade'].mean()
            aveTerm = dataFilter.groupby('Term')['Grade'].mean()
            maxTerm = dataFilter['Grade'].max()
            maxGrades = dataFilter[dataFilter['Grade'] == maxTerm]
            minTerm = dataFilter['Grade'].min()
            minGrades = dataFilter[dataFilter['Grade'] == minTerm]
            
            statsTitle = f"     {levelName} ({degree}) Level     "
            statsDisplay += "=" * 50 + "\n"
            statsDisplay += f"{statsTitle.center(50, *'*')}\n"
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
        	print('No data was found with the data you entered\n')
    # sleep(1)
    """
# Major Transcript shows students transscript of record based on their major courses
def majorTranscriptFeature(stdID, stdDetails, levels, degrees):
    # Initialize a boolean variable to track if any data was found
    valueCheck = False
    # Load the student details into data frames
    sDetails = pd.read_csv('studentDetails.csv')
    std = pd.read_csv(f'{stdID}.csv')
    # Initialize an empty string to store the output
    mDisplay = ""
    # Iterate over the selected student level and degree of the user
    for level in levels:
        for degree in degrees:
            # Filter the DataFrame to only include data for the selected student stdID, level and degree
            dataFilter = sDetails[(sDetails['stdID'] == int(stdID)) & (
                sDetails['Level'] == level) & (sDetails['Degree'] == degree)]
            # If there is no data found, skip and continue
            if dataFilter.empty:
                continue
            # If matching data was found, add the student details to the output string like name, stdID, college etc
            border = 60 * "=" + "\n"
            footer = f"     Major Transcript for Level ({level} - {degree})     "
            mDisplay += border
            mDisplay += f"{footer.center(60, *'*')}\n"
            mDisplay += f"{border}\n"
            mDisplay += f"Name: {dataFilter['Name'].iloc[0]}\t\t\t"
            mDisplay += f"stdID: {dataFilter['stdID'].iloc[0]}\n"
            mDisplay += f"College: {dataFilter['College'].iloc[0]}\t\t\t\t"
            mDisplay += f"Department: {dataFilter['Department'].iloc[0]}\n"
            mDisplay += f"Major: {dataFilter['Major'].iloc[0]}\t\t\t"
            mDisplay += f"Minor: {dataFilter['Minor'].iloc[0]}\n"
            mDisplay += f"Level: {dataFilter['Level'].iloc[0]}\t\t\t\t"
            mDisplay += f"Number of terms: {dataFilter['Terms'].sum()}\n\n"
            # Filter the DataFrame to only include data for the selected student level and degree
            stdDataFilter = std[(std['Level'] == level) & (
                std['Degree'] == degree)]
            # Get a list of terms to be counted
            terms = stdDataFilter['Term'].unique()
            # Iterate over each term
            for term in terms:
                # Filter the DataFrame to only include data for the term
                termDataFilter = stdDataFilter[(
                    stdDataFilter['Term'] == term)]
                # Filter the DataFram to only include data for major courses
                majorDataFilter = termDataFilter[termDataFilter['courseType'] == 'Major']
                # Add the major courses information like type, name, grade to the output string
                titleTerm = f"     Term ({term})     "
                border = 60 * "=" + "\n"
                mDisplay += border
                mDisplay += f"{titleTerm.center(60, *'*')}\n"
                mDisplay += border
                mDisplay += "{:^15} {:^15} {:^15} {:^15}\n".format(
                    "courseID", "courseName", "creditHours", "Grade")
                for row in majorDataFilter.itertuples(index=False):
                    mDisplay += "{:^15} {:^15} {:^15} {:^15}\n".format(
                        row.courseID, row.courseName, row.creditHours, row.Grade)
                    
                majorAve = majorDataFilter['Grade'].mean()
                overallAve = termDataFilter['Grade'].mean()
                
                
                mDisplay += "\n\n"
                mDisplay += f"Major Average: {majorDataFilter['Grade'].mean():.2f}   \t\t\t"
                mDisplay += f"Overall Average: {termDataFilter['Grade'].mean():.2f}\n\n"
            footer = f"     End of Transcript for Level ({level} - {degree})     "
            mDisplay += border
            mDisplay += f"{footer.center(60, *'*')}\n"
            mDisplay += border
            # Set foundData to True to indicate that data has been found for this student
            valueCheck = True

    # If any data was found, write the output string to store in text file and print it
    if valueCheck:
        # Write the output string to a TXT file
        exportInfo = f"std{stdID}MajorTranscript.txt"
        with open(exportInfo, 'w') as mdisp:
            mdisp.write(mDisplay)
        # Print output
        print(mDisplay)
    else:
        # If no data was found, print a message
        print('No data found with the stdID, level, and degree you entered!\n')

# Minor Transscript shows students transcript of record based on their minor courses
def minorTranscriptFeature(stdID, stdDetails, levels, degrees):
    # Initialize a boolean variable to track if any data was found
    foundData = False
    # Load the student details into data frames
    detailsDF = pd.read_csv('studentDetails.csv')
    stdDF = pd.read_csv(f'{stdID}.csv')
    # Initialize an empty string to store the output
    output = ""
    # Iterate over the selected student level and degree of the user
    for level in levels:
        for degree in degrees:
            # Filter the DataFrame to only include data for the selected student stdID, level and degree
            detailsfilteredData = detailsDF[(detailsDF['stdID'] == int(stdID)) & (
                detailsDF['Level'] == level) & (detailsDF['Degree'] == degree)]
            # If there is no data found, skip and continue
            if detailsfilteredData.empty:
                continue
            # If matching data was found, add the student details to the output string like name, stdID, college etc
            border = 60 * "=" + "\n"
            footer = f"     Minor Transcript for Level ({level} - {degree})     "
            output += border
            output += f"{footer.center(60, *'*')}\n"
            output += f"{border}\n"
            output += f"Name: {detailsfilteredData['Name'].iloc[0]}\t\t\t\t\t\t"
            output += f"stdID: {detailsfilteredData['stdID'].iloc[0]}\n"
            output += f"College: {detailsfilteredData['College'].iloc[0]}\t\t\t\t\t\t\t"
            output += f"Department: {detailsfilteredData['Department'].iloc[0]}\n"
            output += f"Major: {detailsfilteredData['Major'].iloc[0]}\t\t\t\t\t\t"
            output += f"Minor: {detailsfilteredData['Minor'].iloc[0]}\n"
            output += f"Level: {detailsfilteredData['Level'].iloc[0]}\t\t\t\t\t\t\t\t"
            output += f"Number of terms: {detailsfilteredData['Terms'].sum()}\n\n"
            # Filter the DataFrame to only include data for the selected student level and degree
            stdfilteredData = stdDF[(stdDF['Level'] == level) & (
                stdDF['Degree'] == degree)]
            # Get a list of terms to be counted
            terms = stdfilteredData['Term'].unique()
            # Iterate over each term
            for term in terms:
                # Filter the DataFrame to only include data for the term
                termFilteredData = stdfilteredData[(
                    stdfilteredData['Term'] == term)]
                # Filter the DataFrame to only include data for minor courses
                minorFilteredData = termFilteredData[termFilteredData['courseType'] == 'Minor']
                # Add the minor courses information like type, name, grade to the output string
                titleTerm = f"     Term ({term})     "
                border = 60 * "=" + "\n"
                output += border
                output += f"{titleTerm.center(60, *'*')}\n"
                output += border
                output += "{:^15} {:^15} {:^15} {:^15}\n".format(
                    "courseID", "courseName", "creditHours", "Grade")
                for row in minorFilteredData.itertuples(index=False):
                    output += "{:^15} {:^15} {:^15} {:^15}\n".format(
                        row.courseID, row.courseName, row.creditHours, row.Grade)
                output += "\n\n"
                output += f"Minor Average: {minorFilteredData['Grade'].mean():.2f}   \t\t\t\t"
                output += f"Overall Average: {termFilteredData['Grade'].mean():.2f}\n\n"
            footer = f"     End of Transcript for Level ({level} - {degree})     "
            output += border
            output += f"{footer.center(60, *'*')}\n"
            output += border
            # Set foundData to True to indicate that data has been found for this student
            foundData = True
    # If any data was found, write the output string to store in text file and print it
    if foundData:
        # Write the output string to a TXT file
        outputTXTFile = f"std{stdID}MinorTranscript.txt"
        with open(outputTXTFile, 'w') as f:
            f.write(output)
        # Print output
        print(output)
    else:
        # If no data was found, print a message
        print('No data found with the stdID, level, and degree you entered!\n')


# Full Transscript shows students transcript of record on both major and minor courses
def fullTranscriptFeature(stdID, stdDetails, levels, degrees):
    # Initialize a boolean variable to track if any data was found
    foundData = False
    # Load the student details into data frames
    detailsDF = pd.read_csv('studentDetails.csv')
    stdDF = pd.read_csv(f'{stdID}.csv')
    # Initialize an empty string to store the output
    output = ""
    # Iterate over the selected student levels and degrees of the user
    for level in levels:
        for degree in degrees:
            # Filter DataFrame for rows matching the given stdID, level, and degree
            detailsfilteredData = detailsDF[(detailsDF['stdID'] == int(stdID)) & (
                detailsDF['Level'] == level) & (detailsDF['Degree'] == degree)]
            if detailsfilteredData.empty:
                continue  # skip and continue to next if no matching data were found
            # If matching data was found, append student's name, stdID, college, department, major, minor, level, and no of terms to output string
            border = 60 * "=" + "\n"
            footer = f"     Full Transcript for Level ({level} - {degree})     "
            output += border
            output += f"{footer.center(60, *'*')}\n"
            output += f"{border}\n"
            output += f"Name: {detailsfilteredData['Name'].iloc[0]}\t\t\t\t\t\t"
            output += f"stdID: {detailsfilteredData['stdID'].iloc[0]}\n"
            output += f"College: {detailsfilteredData['College'].iloc[0]}\t\t\t\t\t\t\t"
            output += f"Department: {detailsfilteredData['Department'].iloc[0]}\n"
            output += f"Major: {detailsfilteredData['Major'].iloc[0]}\t\t\t\t\t\t"
            output += f"Minor: {detailsfilteredData['Minor'].iloc[0]}\n"
            output += f"Level: {detailsfilteredData['Level'].iloc[0]}\t\t\t\t\t\t\t\t"
            output += f"Number of terms: {detailsfilteredData['Terms'].sum()}\n\n"
            # Filter DataFrame for rows matching the selected student level and degree
            stdFilteredData = stdDF[(stdDF['Level'] == level) & (
                stdDF['Degree'] == degree)]
            # count the no. of terms for this level and degree
            terms = stdFilteredData['Term'].unique()
            # Iterate over the terms for selected student level and degree
            for term in terms:
                # Filter DataFrames for rows matching the given term
                termFilteredData = stdFilteredData[(
                    stdFilteredData['Term'] == term)]
                minorFilteredData = termFilteredData[termFilteredData['courseType'] == 'Minor']
                majorFilteredData = termFilteredData[termFilteredData['courseType'] == 'Major']
                # Append the courseID, courseName, creditHours, and average grades for each course in this term to the output
                titleTerm = f"     Term ({term})     "
                border = 60 * "=" + "\n"
                output += border
                output += f"{titleTerm.center(60, *'*')}\n"
                output += border
                output += "{:^15} {:^15} {:^15} {:^15}\n".format(
                    "courseID", "courseName", "creditHours", "Grade")
                for row in termFilteredData.itertuples(index=False):
                    output += "{:^15} {:^15} {:^15} {:^15}\n".format(
                        row.courseID, row.courseName, row.creditHours, row.Grade)
                output += "\n\n"
                output += f"Major Average: {majorFilteredData['Grade'].mean():.2f}   \t\t\t\t"
                output += f"Minor Average: {minorFilteredData['Grade'].mean():.2f}\n"
                output += f"Term Average: {termFilteredData['Grade'].mean():.2f}   \t\t\t\t"
                output += f"Overall Average: {stdFilteredData['Grade'].mean():.2f}\n\n"
            footer = f"     End of Transcript for Level ({level} - {degree})     "
            output += border
            output += f"{footer.center(60, *'*')}\n"
            output += border
            # Set foundData to True to indicate that data has been found for this student
            foundData = True
    # If data was found for the student, write the output string to a TXT file and print it
    if foundData:
        # Write the output string to a TXT file
        outputTXTFile = f"std{stdID}FullTranscript.txt"
        with open(outputTXTFile, 'w') as f:
            f.write(output)
        # Print output
        print(output)
    else:
        # If no data was found, print a message
        print('No data found with the stdID, level, and degree you entered!\n')
        
# New Student Feature allows another student after clearing all previous data
def newStudentFeature():
    print("Clearing cache...")
    cls()
    # sleep(1)
    # main()


# Terminate Feature shows the number of request during the session
def terminateFeature(requestCount):
    print(f"Number of requests this session: {requestCount}")
    print("Thank you for using the system!")
    # sleep(1)
    exit()

def recordRequest(stdID, request, requests):
    timestamp = datetime.datetime.now()
    new_entry = {
        'request': request,
        'date': timestamp.strftime("%d/%m/%Y"),
        'time': timestamp.strftime("%I:%M %p")
    }
    
    if stdID not in requests:
        requests[stdID] = []
    
    requests[stdID].append(new_entry)
    
    # Write to file immediately
    with open(f"std{stdID}PreviousRequests.txt", "a") as f:
        f.write(f"{request}\t{new_entry['date']}\t{new_entry['time']}\n")
    
    return requests

def previousRequestsFeature(stdID, requests):
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
    return requests  # Return unmodified requests as we read from file

def main():
    requests = {}
    # Loads the csv file as a dataframe
    stdDetailsFile = "studentDetails.csv"
    stdDetails = loadDetailsFile(stdDetailsFile)
    
    # Get user input for student level and degree
    levels, degrees = startFeature()
    
    # Gets studentID and checks if it matches the stdID in the database
    stdID = input("Enter your student ID: ").strip()
    stdID = studentIDCheck(stdID, stdDetails)
    
    requestCount = 0
    while True:
        requestCount = menuFeature(stdID, stdDetails, levels, degrees, requestCount)

if __name__ == "__main__":
    main()
