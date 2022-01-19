import os
import getpass

os.system("tput setaf 1")
print("\t\t\t Hi, welcome new user tell us what to do")
os.system("tput setaf 7")
print("\t\t\t----------------------------")

passwd=getpass.getpass("Enter your password:")
apass= "*******"

if passwd != apass:
    print("incorrect password")
    exit()

while True:
    print(""" press 1: to see date
              press 2: to check cal
              press 3: to install or remove software
              press 4: to create user
              press 5: to open the web browser
              press 6: exit """)
    print("Enter your choice:",end=" ")  
    ch=input()

    print(ch)

    if int(ch) == 1:
        os.system("date")
    elif int(ch) == 2:
        os.system("cal")
    elif int(ch) == 3:
        print("Enter what you want to install or remove:",end='')
        option = input()
        if option=="install":
            print("Enter package name:",end='')
            package_name=input()
            os.system("yum install {}".format(package_name))
        elif option=="remove":
            print("Enter package name:",end='')
            package_name=input()
            os.system("yum remove {}".format(package_name))
        else:
            print("Wrong choice")
    elif int(ch) == 4:
        print("Enter user name:",end='')
        create_user = input()
        os.system("useradd{}".format(create_user))
    elif int(ch) == 5:
        os.system("firefox")
    elif int(ch) == 6:
        exit()
    else:
        print("Not available")
        input("Press enter for choice")
        os.sytem("Clear")     

