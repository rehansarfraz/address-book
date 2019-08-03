# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 11:57:30 2019

@author: Rehan
"""

                         # Address Book
# definition of menu function
def menu():
    print("Please select one of the following actions")
    print("press 1 for Add contact")
    print("press 2 for View contact")
    print("press 3 for Adit contact")
    print("press 4 for Delete contact")

# initilizing of lists of fields
name_list= []
no_list = []
email_list = []
address_list =[]
                        
                                               

i=0             # no. of iterations of main loop
iteration = 0   # var for iterations in checking loop
input_name ='' # var for inputing name from user
while i>=0:
        menu() # Menu Code
        input_loop_check = True  #flag variable for input check loop
        while input_loop_check:
            user_input = int(input(":"))
            if user_input== 1 or user_input==2 or user_input==3 or user_input==4 or user_input==5:
                break
            else:
                print("user value is not valid, please re-enter")
                # Code for option 1
       
        if user_input == 1:
            name_list.append(input("Name is: "))
            no_list.append(input("No is: "))
            email_list.append(input("email is: "))
            address_list.append(input("address is "))
            # option 2
            
        elif user_input == 2:
            input_name = (input(" please Enter name. :"))
            for iteration in range(0,len(name_list)):
                if input_name == name_list[iteration]:
                    print(" Name", name_list[iteration])
                    print(" Address", address_list[iteration])   
                    print("Phone", no_list[iteration])
                    print("Email", email_list[iteration])
          # option 3
        elif user_input ==3:
            input_name = (input(" please Enter name. :"))
            for iteration in range(0,len(name_list)):
                    if input_name == name_list[iteration]:
                        name_list[iteration]= input(" Edited Name: ")
                        address_list[iteration]= input(" Edited Address: ")   
                        no_list[iteration]= print(" Edited Phone: ")
                        email_list[iteration]= print(" Edited Email: ")             
            else:
                print("Entered name is incorrect")
          # option 4
        elif user_input ==4:
            input_name = (input(" please Enter name. :"))
            for iteration in range(0,len(name_list)):
                    if input_name == name_list[iteration]:
                        name_list.pop(iteration) 
                        address_list.pop(iteration)   
                        no_list.pop(iteration) 
                        email_list.pop(iteration)              
            else:
                print("Entered name is incorrect")
        i +=1
            # Code for continuaiton of transaction
        print("Do you want another transaction ? Y/N")
        user_check_2 = True  #flag variable for continuation loop
        while user_check_2:
            user_input_continuation = input()
            if user_input_continuation == 'y':
                break
            elif user_input_continuation == 'n':
                i= -1        #condition for exiting loop
                break
            else: 
                print("wrong value, press again")
                continue
        
print("Program is being closed") 
           
         
            
                                        
    
 
 