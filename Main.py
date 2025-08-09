# Main Program Menu

import CaesarEncryption as ce
import CaesarDecryption as cd
import PathConversion as pc

while(True):
    print("SIMPLE ENCRYPTION APPLICATION\n"
          "MAIN MENU:\n"
          "Make sure the file being used in the below operation should only be text files\n"
          "0. EXIT\n"
          "1. Encrypt a file\n"
          "2. Decrypt a file\n"
          "Press the respective number to initiate that operation")
    operationInput = int(input())
    match operationInput:
        case 0:
            exit()
        case 1:
            print("Enter the full path of the file")
            plainTextFilePath = input()
            convertedPlainTextFilePath = pc.convertPath(plainTextFilePath)
            print("Enter the number for with which you want to do the encryption")
            encryptionReplacementNum = int(input())
            try:
                ce.encryption(convertedPlainTextFilePath,encryptionReplacementNum)
                print("The file is encrypted in the same folder with the plain text file.")
            except Exception:
                print("\n\nOops! An unexpected error occured\n\n")
        case 2:
            print("Enter the full path of the file")
            cipherTextFilePath = input()
            convertedCipherTextFilePath = pc.convertPath(cipherTextFilePath)
            print("Enter the number with which encryption was performed")
            decryptionReplacementNum = int(input())
            try:
                cd.decryption(convertedCipherTextFilePath,decryptionReplacementNum)
                print("The file is decrypted in the same folder with the Cipher text file.")
            except Exception:
                print("\n\nOops! An unexpected error occured\n\n")