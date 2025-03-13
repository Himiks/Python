#Given 3 natural numbers m, n and k.Print those numbers between m and n what can be divided with k with no reminder.
#Create program both in C++, and Python. Input from keyboard all given values and print on screen all output. 
#Program should output error message for incorrect input data. 
#Program should allow repeated execution without quitting the program.

option = 'y' # variable for repeated execution
while option == 'y' or option == 'Y': # while user enter y or Y the program will continue its execution
        
    print("Enter tree numbers m < n and k : ")
    m = int(input("Enter first number : "))
    n = int(input("Enter second number : "))
    k = int(input("Enter third number : "))
    while  m >= n or m == 0 or k ==0 or n <=k or m < 0: #  while user entering incorrect values, the while loop will repeat asking to enter a valid values untill user will enter a corrrect numbers and this loop will ended
        print("Incorrect values! Please try again : ")
        if m >= n: # if m >= n the program will finish execution becouse of incorrect input
            print("m must be smaller than n!!! ")
        if m < 0: #if m < 0 then the program will finish execution because numbers before 0 dont natural
            print("m must be greater than 0!!!")
        if n <= k:
            print("k must be less than n!!! ")
        if m == 0 or k == 0: #if m or k = 0 the program will finish execution because 0 is not natural number
            print("Enter natural numbers !!!! ")  
        m = int(input("Enter first number : "))
        n = int(input("Enter second number : "))
        k = int(input("Enter third number : "))
         
    
    
    for i in range(m, n + 1): #the for loop check if i less than n and while it less then n the program executed by checking the reminder and if reminder = 0 the i will be displayed
        if  i % k == 0:
                 print("The numbers which can be devided with k is : ", i)
           
    print("Would you like to continue y/n ? : ")
    option = input()
    if option == 'n' or option == 'N': #if answer n or N the program stops execution
    
        break
