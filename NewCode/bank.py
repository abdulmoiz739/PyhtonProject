import json
import random
import string
from pathlib import Path

class Bank:
    database = 'data.json'
    data = []

    # Load data on class load
    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.load(fs)
        else:
            print("No database found, starting fresh!")
    except Exception as err:
        print(f"Error loading data: {err}")

    @classmethod
    def __update(cls):
        with open(cls.database, 'w') as fs:
            json.dump(cls.data, fs, indent=4)

    @classmethod
    def __account_generate(cls):
        alpha = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits, k=3)
        spChar = random.choices("!@#$%^&*", k=1)
        id = alpha + num + spChar
        random.shuffle(id)
        return "".join(id)

    def __find_user(self, account_no, pin):
        return next((user for user in self.data if user['Account No'] == account_no and user['Pin'] == pin), None)

    def create_account(self):
        name = input("Enter your Name: ")
        age = int(input("Enter your Age: "))
        email = input("Enter your Email: ")
        pin = int(input("Enter 4-digit Pin: "))

        if age < 18 or len(str(pin)) != 4:
            print("Sorry, cannot create account. Age < 18 or invalid pin.")
            return

        account_no = self.__account_generate()
        user_info = {
            "Name": name,
            "Age": age,
            "Email": email,
            "Pin": pin,
            "Account No": account_no,
            "Balance": 0
        }
        self.data.append(user_info)
        self.__update()
        print(f"Account created! Your Account No: {account_no}")

    def deposit_money(self):
        account_no = input("Account No: ")
        pin = int(input("Pin: "))
        user = self.__find_user(account_no, pin)
        if not user:
            print("User not found!")
            return

        amount = int(input("Deposit Amount: "))
        if amount <= 0 or amount > 10000:
            print("Invalid amount. Must be 1-10000.")
            return

        user['Balance'] += amount
        self.__update()
        print(f"Deposited successfully! New Balance: {user['Balance']}")

    def withdraw_money(self):
        account_no = input("Account No: ")
        pin = int(input("Pin: "))
        user = self.__find_user(account_no, pin)
        if not user:
            print("User not found!")
            return

        amount = int(input("Withdraw Amount: "))
        if amount > user['Balance']:
            print("Insufficient balance!")
            return

        user['Balance'] -= amount
        self.__update()
        print(f"Withdrawn successfully! Remaining Balance: {user['Balance']}")

    def show_details(self):
        account_no = input("Account No: ")
        pin = int(input("Pin: "))
        user = self.__find_user(account_no, pin)
        if not user:
            print("User not found!")
            return

        for key, value in user.items():
            print(f"{key}: {value}")

    def update_details(self):
        account_no = input("Account No: ")
        pin = int(input("Pin: "))
        user = self.__find_user(account_no, pin)
        if not user:
            print("User not found!")
            return

        print("Leave empty to skip updating field.")
        name = input(f"New Name ({user['Name']}): ") or user['Name']
        email = input(f"New Email ({user['Email']}): ") or user['Email']
        pin_input = input(f"New Pin ({user['Pin']}): ")
        pin = int(pin_input) if pin_input else user['Pin']

        user.update({"Name": name, "Email": email, "Pin": pin})
        self.__update()
        print("Details updated successfully!")

    def delete_account(self):
        account_no = input("Account No: ")
        pin = int(input("Pin: "))
        user = self.__find_user(account_no, pin)
        if not user:
            print("User not found!")
            return

        confirm = input("Confirm delete? (y/n): ").lower()
        if confirm == 'y':
            self.data.remove(user)
            self.__update()
            print("Account deleted successfully!")
