# Program to convert the path entered by the user to the path which the code can understand by replacing backslash by forward slash

def convertPath(inputPath):
    pathToList = inputPath.split("\\") # converting string path to List
    finalPathString = "//".join(pathToList)
    return finalPathString