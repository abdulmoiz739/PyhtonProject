import textwrap

name = input("Enter your name : ").strip()
profession = input("Enter your profession : ").strip()
passion = input("Describe your passion in one line : ").strip()
emoji = input("Enter your favourite Emoji : ").strip()
website = input("Enter your website Name : ").strip()

print("Choose your Style : ")
print("1. Simple Lines ")
print("2. Vertical flair ")
print("3. Emoji sandwich ")

style = input("Enter 1,2 or 3 : ").strip()

def generate_Bio_func(style):
    if style == "1":
        return f" {emoji} {name} | {profession} \n 🔥 {passion} \n {website}"
    elif style == "2":
        return f" {emoji} {name} \n {profession} 🔥 \n {passion} \n {website}"
    elif style == "3":
        return f"{emoji * 5 } \n {name} - {profession}\n {passion} {website}\n {emoji * 5}"

Bio = generate_Bio_func(style)


print("Your stylish Bio ")
print("*" * 50)
print(textwrap.dedent(Bio))
print("*" * 50)

save = input("Do you want to Save your bio to a text file? (y/n) ").lower()

if save == "y":
    fileName = f"{name.lower().replace(" ", "_")}_bio.txt" 
    with open(fileName,"w",encoding="utf-8") as f:
        f.write(Bio)
    print("File Save")
elif save == "n":
    print("File is not save") 
