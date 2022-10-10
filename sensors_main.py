import sys
import os

# We need to import sys to use the command line argument. That's why it is imported.
# This is the main function for controlling the flow of the
# implementation.


def main():

    # Here in main, I just called all the functions to print
    # the warnings if there is any as well as printing the
    # readings from each sensor.
    limits = parse_limits()
    sensor_data = []
    warningLength = displayLimitsWarning(limits)

    if len(limits) > 0 and check_limits(limits):
        sensor_data = read_sensors()
        if (len(warningLength) > 0):
            print(
                "\nWarning!!!.........Warning!!!.........Warning!!!\n")
            for row in warningLength:
                print("{0} °C measured from Sensor {1} at {2}:00 is {3} of {4} °C\n".format(
                    row[2], (row[0] + 1), row[1], row[3], row[4]))
        else:
            print("No abnormal measurements")
        for i, rows in enumerate(sensor_data):
            print("Sensor {0} data \n{1}\n".format(i + 1, rows))
    else:
        print("Error: Incorrect command line arguments.")

# This is the parse_limits function for getting the temperature
# limits from the command line parameters. Returns an array
# that has the limits (limits[0] has min. temperature limit and
# limits[1] has max. temperature limit). If there is an exception
# reading the command line paratmeters, the limits array is empty.


def parse_limits():
    limits = []

    try:
        limits = [int(sys.argv[1]), int(sys.argv[2])]
    except Exception:
        pass

    return limits

# This is the check_limits function that gets an array containing the
# limits as a parameter and checks that the lower limit is smaller
# than the higher limit. If this is the case, the function returns
# True. Otherwise, it returns False.


def check_limits(limits):
    if limits[0] < limits[1]:
        return True
    else:
        return False

# This function is used to open and read each of the text files
# given to it as a parameter representing each of the sensors readings.


def openAndReadFiles(directory):
    sensorList = []
    with open(directory) as f:
        for line_ in f:
            line = line_.strip().split(",")
            sensorList.append(float(line[1]))
    f.close()
    return sensorList

# The read_sensors function scans through the "testdata" directory
# located in the current directory, gets each of the text files in
# the location and calls the openAndReadFiles function to read and
# process the contents of each file. Finally it returns the list of
# all the files readings representing the sensors readings.


def read_sensors():
    allSensorsReadingsList = []
    base_path = "testdata"
    with os.scandir(base_path) as files:
        for file_ in files:
            file_data = openAndReadFiles(file_)
            allSensorsReadingsList.append(file_data)
    files.close()
    return allSensorsReadingsList

# Other parts of the implementation such as printing the information
# for the operator are also missing and to be implemented.

# Let's add this comment to test commit to the source on GitHub

# This function (minMaxAveFunction) take a list of lists and returns
# the daily highest and lowest temperatures.


def minMaxFunction(sensorsDataList):
    allElements = []
    for eachList in sensorsDataList:
        for item in eachList:
            allElements.append(item)
    allElements.sort()
    max_E, min_E = allElements[-1], allElements[0]

    return max_E, min_E

# This function displayLimitsWarning takes limits as parameter and
# return the list of temperatures that are above or below the limits.


def displayLimitsWarning(limits):
    listSet = []
    sensor_data = read_sensors()

    for index1, row in enumerate(sensor_data):
        for index2, item in enumerate(row):
            if (item < limits[0]):
                message1 = "lower than the minimum limit"
                listSet.append([index1, index2, item, message1, limits[0]])
            if (item > limits[1]):
                message2 = "greater than the maximum limit"

                listSet.append([index1, index2, item, message2, limits[1]])

    return listSet


main()
