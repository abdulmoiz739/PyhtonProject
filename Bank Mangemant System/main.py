import json
import  random
import string
from pathlib import Path

class Bank:

    database = 'data.json'
    data = []
    
    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("No such file Exits")
    except Exception as err:
        print(f"an Exception occured as {err}")    

    @classmethod
    def __update(cls):
        with open(Bank.database,'w') as fs:
            fs.write(json.dumps(Bank.data))
     
    @classmethod
    def __accoungenerate(cls):
        alpha = random.choices(string.ascii_letters,k=3)      
        num = random.choices(string.digits,k=3)      
        spChar = random.choices("!@#$%^&*",k=1)      
        id = alpha + num + spChar
        random.shuffle(id)
        return "".join(id)

    def createAccount(self):
        info = {
            "Name" : input("Tell your Name : "),
            "Age" : int(input("Tell your Age : ")),
            "Email" : (input("Tell your Email : ")),
            "Pin" : int(input("Tell your 4 number pin : ")),
            "Account No" : Bank.__accoungenerate(),
            "Balance" : 0
        }
        if info["Age"] < 18 or len(str(info["Pin"])) != 4 :
            print("Sorry, you cannot create your account")
        else:
            print("Account has been Successfully")
            for i in info:
                print(f"{i}" , f"{info[i]}")
            print("Please Note down your account")    
            
            Bank.data.append(info)
            
            Bank.__update()
    
    def depositMoney(self):
        
        checkAccountNo = input("Please enter your Account No : ")
        checkPin = int(input("Please enter your Pin : "))
          
        userdata = [i for i in Bank.data if i['Account No'] == checkAccountNo and i['Pin'] == checkPin]
          
        if userdata == False:
            print("Sorry, Data not found")
        
        else:
            amount = int(input("How much you want to deposit : "))

            if amount > 10000 or amount < 0 :
                print("Sorry, The amount is too much You can Deposit Below 10,000 and Above 0.")
            
            else:
                userdata[0]['Balance'] += amount
                
                Bank.__update()
                
                print("Money deposit Successfully")
                    
    
    def withdrawMoney(self):
        
        checkAccountNo = input("Please enter your Account No : ")
        checkPin = int(input("Please enter your Pin : "))
          
        userdata = [i for i in Bank.data if i['Account No'] == checkAccountNo and i['Pin'] == checkPin]
          
        if userdata == False:
            print("Sorry, Data not found")
        
        else:
            amount = int(input("How much you want to Withdraw : "))

            if userdata[0]['Balance'] < amount:
                print("Sorry, Enter Correct Amount")
            
            else:
                userdata[0]['Balance'] -= amount
                
                Bank.__update()
                
                print("Money Withdraw Successfully")
                
                
    def detailAccount(self):
        
        checkAccountNo = input("Please enter your Account No : ")
        checkPin = int(input("Please enter your Pin : "))
          
        userdata = [i for i in Bank.data if i['Account No'] == checkAccountNo and i['Pin'] == checkPin]
        
        if userdata == False:
            print("Sorry, Data not Found")
        
        else:
            print("Your Information are \n\n")
            for i in userdata[0]:
                print(f"{i}  {userdata[0][i]}")   


    def updateDetail(self):
         
        checkAccountNo = input("Please enter your Account No : ")
        checkPin = int(input("Please enter your Pin : "))
          
        userdata = [i for i in Bank.data if i['Account No'] == checkAccountNo and i['Pin'] == checkPin]
          
        if userdata == False:
            print("Sorry, Data not found")
        
        else:
            print("You cannot Change the Age, Account Number and Balance.")
            print("Fill the details for change or leave it empty no change")
            
            newdata = {
                "Name" : input("please tell new Name or press Enter to skip : "),
                "Email" : input("please tell new Email or press Enter to skip: "),
                "Pin" : input("please tell new pin or press Enter to skip : "),
            }
            
            if newdata == "":
                newdata["Name"] = userdata[0]["Name"]
            if newdata == "":
                newdata["Email"] = userdata[0]["Email"]
            if newdata == "":
                newdata["Pin"] = userdata[0]["Pin"]
            
            newdata["Age"] = userdata[0]["Age"]    
            newdata["Account No"] = userdata[0]["Account No"]    
            newdata["Balance"] = userdata[0]["Balance"]    
            
            if type(newdata["Pin"] == str):
                newdata["Pin"] = int(newdata["Pin"])
              
            for i in newdata:
                if newdata[i] == userdata[0][i]:
                    continue
                else:
                    userdata[0][i] = newdata[i]

                Bank.__update()
                print("Detail update Successfully")
        
    def deleteAccount(self):
        
        checkAccountNo = input("Please enter your Account No : ")
        checkPin = int(input("Please enter your Pin : "))
          
        userdata = [i for i in Bank.data if i['Account No'] == checkAccountNo and i['Pin'] == checkPin]
          
        if userdata == False:
            print("Sorry, Data not found")
        else:
            check = input("Press y if you want to delete Account or Press No :")
            if check == "n" or check == "N":
                print("Bypassed")
            else:
                index = Bank.data.index(userdata[0])
                Bank.data.pop(index)
                print("Account Delete Successfully")
                Bank.__update()
             
user = Bank()


print("Press 1 for creating an account")
print("Press 2 for Depositing Money in the Bank")
print("Press 3 for Withdrawing the Money")
print("Press 4 for Detail your Account")
print("Press 5 for Update the Detail")
print("Press 6 for Detele your Account")



check = int(input("Tell your response : "))

if check == 1:
    user.createAccount()
    
if check == 2:
    user.depositMoney() 
    
if check == 3:
    user.withdrawMoney() 

if check == 4:
    user.detailAccount() 

if check == 5:
    user.updateDetail() 
    
if check == 6:
    user.deleteAccount() 
    
    
