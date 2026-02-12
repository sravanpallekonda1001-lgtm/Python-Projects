contact_list={"Sravan":9177387678,
              "Kumar":9121392708,
              "Shanmukh":9391171682,
              "Rizwan":9346284432,
              "Kranthi":8008590879
              
}
print("\n1.View Contacts,\n2.Search contacts,\n3.UPdate,\n4.addcontacts,\n5.delete contacts,\n6.exit")
def view_contacts():
    print("\n Available Contacts")
    print(" "*20," your_contact_list"," "*20)
    print("-"*60)
    for persons,numbers in contact_list.items():
        print("*"*2,persons,"=",numbers, )
    print("-"*60)

def search_contacts():
    user=input("enter the name who you want to search")
    if user.capitalize() in contact_list:
        print("the contact name are",user.capitalize(),"is",contact_list.get(user.capitalize()))
    else:
        print(user,"un available")
def update_contact():
    user=input("enter the user name ")
    if user.capitalize() not in contact_list:
         print("user not in the list")
    else:
        number=int(input("enter the number:"))
        contact_list.update({user:number})
        print("updated successfully")
    option=input("you want to add the new user press [Y|N]")
    if option =="Y":
        number=int(input("enter the number:"))
        contact_list.update({user:number})
        print("user added successfully")
    else:
        print("thank you if you want update press (2)")

def add_contacts():
    add=input("enter the new conact")
    if add.capitalize() in contact_list:
        print("contact name is",add,"and her number is",contact_list.get(add.capitalize()))
    else:
        print("user not in the contacts if you want to add the user press[Y|N]")
    option=input("enter you want to add the new user[Y|N]")
    if option == "Y":
        number=int(input("enter the new user number:"))
        contact_list[add]=number
        print("added successfully")
    else:
        print("thanks for conformation")

def delete_contact():
    user=input("enter the user name you want to delete")
    if user.capitalize() in contact_list:
        del contact_list[user.capitalize()]
        print("contact is deleted")
    else:
        print("unavailable contact")
def exit():
    print("exit")
    
while True:
    search_the_num=int(input("enter the numbers from 1-6"))
    if search_the_num ==1:
        view_contacts()
    elif search_the_num ==2:
        search_contacts()
    elif search_the_num ==3:
        update_contact()
    elif search_the_num ==4:
        add_contacts()
    elif search_the_num ==5:
        delete_contact()
    elif search_the_num ==6:
        exit()
        break
        