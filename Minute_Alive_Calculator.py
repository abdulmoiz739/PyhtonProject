def minute_calculator_func(your_age):
    DAYS_IN_YEAR = 365.25
    HOUR_IN_DAY = 24
    MINUTES_IN_HOUR = 60
    
    total_days = your_age * DAYS_IN_YEAR
    total_hours = total_days * HOUR_IN_DAY
    total_minutes = total_hours * MINUTES_IN_HOUR
    
    return total_days, total_hours, total_minutes


while True:
    try:
        # User se age input lena
        your_age = float(input("Enter your age: "))
        
        # Function call karke values store karna
        days, hours, minutes = minute_calculator_func(your_age)
        
        # Result neatly print karna
        print("\n🔹 Your approximate age in time units:")
        print(f" - Total days   : {days:,.2f}")
        print(f" - Total hours  : {hours:,.2f}")
        print(f" - Total minutes: {minutes:,.2f}\n")
        
        # User ko dobara try ka option
        again = input("Would you like to try again? (y/n): ").strip().lower()
        if again != "y":
            print("👋 Good Bye!")
            break

    except ValueError:
        print("❌ Please enter a valid number.\n")
