contact = {
    
}

#infinite loop to continue asking the user what they would like to do
while True:

    print("Contact Book Menu: ")
    print("1. Add contact ")
    print("2. Delete Contact ")
    print("3. List Contacts ")
    print("4. Exit")
    #allows the user to use options 1 - 4
    choice = input("Enter your choice: ")

    #this function only works if they choose 1
    if choice == "1":
        name = input("Enter the contact's name: ")
        number = int(input("Enter the contact's phone number: "))
        while len(number) == 10:
            contact[name] = number
        print('contact saved!')
    else: 
        print("Number too long or too short!")
    if choice == "2":
        delete = input("Which contact would you like to delete/edit?: ")
        if name in contact:
            new_number = input("Enter the new phone number: ")
        else: 
            del contact[delete]
    if choice == "3":
        for x in contact:
            print(x)
            print(contact[x])
    if choice == "4":
        break
