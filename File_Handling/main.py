from pathlib import Path
import os

# File Management System using pathlib:3
def readFileAndFolder():
    path = Path("")
    items = list(path.rglob("*"))
    for i, items in enumerate(items):
        print(f"{i+1} : {items} ")
    
# Create File Function:
def createFile():
    try:
        readFileAndFolder()
        name = input("Please tell your file name : ")
        p =  Path(name)
        
        if not p.exists():
            with open(p,"w") as fs:
                data = input("What you want to write in this file : ")
                fs.write(data)
            print("File Created Successfully") 
        else:
            print("File is already exists")  
            
    except Exception as err:
        print(f"An Error occurred as {err}")
         
# Read File Function:
def readFile():
    try:
        readFileAndFolder()
        name = input("which file to want to read : ")
        p = Path(name) 
        
        if p.exists() and p.is_file():
            with open( p,"r") as fs:
                data = fs.read()  
                print(data)
            print("File read Successfully")
            
        else:
            print("File is not exists")  
                  
    except Exception as err:
        print(f"An Error occurred as {err}")
            

# Update File Function:
def updateFile():
    try:
        readFileAndFolder()
        name = input("Which file you want to update : ")   
        p = Path(name)
        if p.exists() and p.is_file():
            
            print("Press 1 for changing the file name : ")
            print("Press 2 for overWriting the file : ")
            print("Press 3 for appending Some content in your file : ")
         
            check = int(input("Tell your choice : "))
           
            if check == 1:
                name2 = input("Tell Tou new file name : ")
                p2 = Path(name2)
                p.rename(p2)
                
            if check == 2:
                with open(p ,"w") as fs:
                    data = input("What you want to overwrite the data : ")
                    fs.write(data)
                    
            if check == 3:
                 with open(p ,"a") as fs:
                    data = input("What you want to append the data : ")
                    fs.write(data)
                
        else:
            print("File is not exist")    
        
    except Exception as err:
        print("An error occurred as {err}")    



# Delete File Function:
def deleteFile():
    try:
        readFileAndFolder()
        name = input("WHch file you want to delete :")
        p = Path(name)
        if p.exists() and p.is_file():
            os.remove(p)
            print("File deleted Successfully")
        else:
            print("File is not exist")
    except Exception as err:
        print(f"An Error occurred as {err}")    


print("Press 1 for Creating a file")
print("Press 2 for Reading a file")
print("Press 3 for Updating a file")
print("Press 4 for Deletion a file")

check = int(input("Enter your choice: "))

if check == 1:
    createFile()
    
if check == 2:
    readFile()
    
if check == 3:
    updateFile()
    
if check == 4:
    deleteFile()