database={"Sravan":1001,"Kumar":1002,"Pallekonda":1003,"Naveen":1004}
user=input("enter the input:")
if user.capitalize() in database.keys():
    password=int(input("enter the password:"))
    if password == database[user.capitalize()]:
        print("welcome",user.capitalize())
    else:
        print("wrong password")
else:
    print("user doesnt exit")
    option=input("do you want to add the user press [Y|N]:")
    if option == "Y" or "y":
        new_password=int(input("enter the new password"))
        database[user.capitalize()]="new_password"
        print("user added successfully")
    else:
        print("Thank you")