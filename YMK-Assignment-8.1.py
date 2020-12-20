# Yitzchok Kaplan - Assignment 8.1
# 12/20/2020
import os #imports os

def GetInput(): #function to get user input
    global fileDir, fileName, UserName, UserNumber, UserAddress
    fileDir = input("\nPlease input the file directory (without an extra / at the end): ")
    if fileDir[-1] == "/": #if statement to check for directory end slash
        print("An end / was detected. Please try again without an ending /")
        GetInput()
    else: #get the rest of the inputs
        fileName = input("Please input the file name: ")
        UserName = input("Please input your name: ")
        UserNumber = input("Please input you phone number: ")
        UserAddress = input("Please input your address: ")
    

def validateDir(): #function to validate directory
    CheckDir = os.path.isdir(fileDir)
    print("\nProgram log...")
    if CheckDir == True: #if directory exists print 
        print("Directory Validation complete...")
        CreateFile()
    elif CheckDir == False: #if function does not exists print
        print("Directory Validation complete...")
        CreateDir()
        CreateFile()
    else: #if any other input print
        print("Sorry, an unexpected error occurred")


def CreateDir(): #function to create directory
    os.mkdir(fileDir)
    ("Directory creation complete...")

def CreateFile(): #function to create file and write data to file 
    os.chdir(fileDir)
    data = UserName + ", " + UserNumber + ", " + UserAddress 
    file = open(fileName, "w")
    file.write(data)
    file.close()
    print("File Writing Complete...")

def readFile(): #function to display file content
    file = open(fileName, "r")
    print("\nThe path to file is: " + fileDir + "/" + fileName)
    print("Here is the contents of " + fileName + ":\n")
    for line in file: #for loop to get each line
        print(line, end='')
    file.close() 
    print("\n\nFile content display complete...")
    print("Thank you for using this program.") #end message 
    input("Press enter to exit...")

def Main(): #function initiation controller 
    GetInput()
    validateDir()
    readFile()

print("Welcome to the file creator and writer.") #prints welcome message
Main() #calls main function


