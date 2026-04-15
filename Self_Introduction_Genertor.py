import datetime

name = input("What is your Name? ").strip()
age = input("How old are you? " ).strip()
city = input("Which city do you live In? ").strip()
profession = input("What is your profession? ").strip()
hobby = input("What is your favourite hobby? ").strip()

intro_message = (
    f"Hello! My name is {name}, I'm {age} years old and live in {city}, "
    f"I work as a {profession} and i Absolutely enjoy {hobby} in free time. "
    f"Nice to meet you!\n"
    )

# Add Current Date:
current_date = datetime.date.today().isoformat()
intro_message += f"Logged on : {current_date}"

# Add some "*" for border and show final output:

border = "*" * 70
final_output = f"{border}\n{intro_message}\n{border}"
print(f"\n" + final_output)

