# Program to convert the path entered by the user to the path which the code can understand by replacing backslash by forward slash

def convertPath(inputPath):
    pathToList = inputPath.split("\\") # converting string path to List
    finalPathString = "" # initialize final variable for string path
    for stringIterator in pathToList:
        # below condition checks that if the current iterator index is the last element then only concatenate the iterator string not the slashes(//)
        if pathToList.index(stringIterator) == len(pathToList)-1:
            finalPathString += stringIterator
        # if the above condition is not met that it concatenates both the iterator string and the slashes(//)
        else:
            finalPathString += stringIterator + "//"
    return finalPathString
