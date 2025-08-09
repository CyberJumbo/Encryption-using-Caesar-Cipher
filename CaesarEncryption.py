# Encryption Algorithm based on caesar cipher

def encryption(filePath, replacementNum):
    filePathToList = filePath.split("//") # Converting file path string to list to extract file name using indexing for output file name creation
    outputFileName = filePathToList[-1] # accessing the last element of the list which is the file name
    outputFileNameLength = len(outputFileName)
    outputFileName = outputFileName[:outputFileNameLength-4] # Slicing the file name to extract the name before .txt extension.
    outputFileName += "Encrypted.txt" # concatenating "Encrypted" to the file name to make it the output file name
    PlainTextFile = open(filePath) # opening plain text file in read mode
    outputFile = open(outputFileName,"w") # Creating and opening output file in write mode
    for readText in PlainTextFile.read():
        cipherText = chr(ord(readText)+replacementNum) # Converting plain text into cipher text by converting alphabet into ascii and adding the number of places and then again converting it into alphabet
        outputFile.write(cipherText)
    PlainTextFile.close()
    outputFile.close()