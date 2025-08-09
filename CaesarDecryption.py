# Decryption Algorithm based on caesar cipher

def decryption(filePath, replacementNum):
    filePathToList = filePath.split("//")  # Converting file path string to list to extract file name using indexing for output file name creation
    outputFileName = filePathToList[-1]  # accessing the last element of the list which is the file name
    outputFileNameLength = len(outputFileName)
    outputFileName = outputFileName[:outputFileNameLength - 4]  # Slicing the file name to extract the name before .txt extension.
    outputFileName += "Decrypted.txt"  # concatenating "Decrypted" to the file name to make it the output file name
    CipherTextFile = open(filePath)  # opening Cipher text file in read mode
    outputFile = open(outputFileName, "w")  # Creating and opening output file in write mode
    for readText in CipherTextFile.read():
        PlainText = chr(ord(readText) - replacementNum)  # Converting Cipher text into plain text by converting alphabet into ascii and subtracting the number of places and then again converting it into alphabet
        outputFile.write(PlainText)
    CipherTextFile.close()
    outputFile.close()