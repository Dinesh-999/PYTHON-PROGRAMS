# email slicer

s = "asdfg23@gmail.com"
st = s.split("@")  # using split method
print("Using split method")
print(f"Email is : {s},  Username is : {st[0]} and Domain is : {st[1]}")

index = s.index('@')  # using index and slicing method eg: s[:8]  s[9:]
username = s[:index]
domain = s[index + 1:]
print("\nUsing index and slicing method eg: s[:8]  s[9:]")
print(f"Email is : {s}, Your Username is {username} & Domain is {domain}")

'''
# for n numbers of emails
n = int(input("Enter the number of emails : "))
for i in range(n):
    email = input("enter email : ")
    email1 = email.split("@")
    print(f"Your username is {email1[0]} & domain is {email1[1]}")
'''

# from a external file
print("\nReading emails from a external file : ")
with open("email_slicer.txt", "r") as f:
    data = f.read()

print(data + "\n")
ss = data.split("\n")

for i in ss:
    u = i.split("@")
    usn = u[0]
    dom = u[1]
    print(f"Email is : {i}, Your Username is {usn} & Domain is {dom}")
