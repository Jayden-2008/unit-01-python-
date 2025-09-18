#this will ask for students name
name = input("whats your name?: ")

#once the student enters their name, the input will check for rather they have a pass or not 
pass_1 = input(f"{name}, do you have a pass? Yes or No: ")

#this if else statement will justify rather or not the student will be able to go or not
if pass_1 == "Yes":
    
#This will check when they received the pass

    time_pass = int(input("What time was your pass issued?: "))

 #This will check for time the student returned 
  
    time_return = int(input("What time did you return?: "))
 
 #Asking the location that the student went to
    location = input("Where are did you go?: Nurse, Bathroom, Office ")
    
    if location == "Nurse" or location == "Bathroom" or location == "Office": 
        if time_return - time_pass <= 2:
            print('You can go.')
        elif time_return - time_pass >= 2:
            print('Time is expired')
else:
    print("No you dont have a pass")
