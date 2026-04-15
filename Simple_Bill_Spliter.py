
check = int(input("How many people Are there in the group ? "))
names = []

for i in range(check):
    name = input(f"Enter your {i+1} name : ").strip()
    names.append(name)

total_bill = int(input("Enter the total bill : "))

share = round(total_bill / check , 2)

for name in names:
    print(f"{name} owes {share} rupees")