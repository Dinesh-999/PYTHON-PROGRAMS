# contact list program
# list is stored in contact_list.txt file

print("=====================================")
print("            contact book             ")
print("=====================================")
n = int(input("Enter the number of persons : "))
for i in range(n):
    print(f"Enter the details of {i+1}st person")
    name = input("Enter the Full name : ")
    nickname = input(f"Enter the Nickname for {name} : ")
    number1 = input(f"Enter the 1st Phone number of {name} : ")
    number2 = input(f"Enter the 2nd Phone number(optional) of {name} : ")
    email = input(f"Enter the Email address(example@gmail.com) of {name} : ")
    dob = input(f"Enter the Date of birth[DOB] (format: DD/MM/YYYY) of {name} : ")
    address = input(f"Enter the Address(location) of {name} : ")
    notes = input(f"Enter notes about {name} : ")

    data = f" Name : {name.upper()}\n Nick Name : {nickname.upper()}\n Phone Numbers : {number1, number2}\n EMAIL : {email}\n Address : {address.capitalize()}\n Date-of-birth : {dob}\n Notes : {notes}\n"
    print(data)

    with open("contact_list.txt", "a") as w:
        w.write(data + "\n")