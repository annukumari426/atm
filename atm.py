print("Welcome to Sharawat Bank : ")
print("Insert Your ATM card ")
pin = int(input("Enter your 4 digit Pin "))
if pin ==1234 :
    print("Your Number is correct:")
    print("1 For Amount check")
    print("2 for Withdrawal balance")
    print("3 for deposite balance")
    print("4 Close")

    option = input(("Enter Your Option : "))
    balance = 200000
    if option=="1":
        print("Your account Balance is :",balance)
    if option == "2":
        withdrawal = int(input("Enter Your Amount to withdrawal :\t"))

        if withdrawal > 10000:
            print("Sorry not allowed withdrawal more than 10000")
        else: 
            print(("Amount you want withdrawal: ",withdrawal))
            print("Your Amonut Sucessfully Withdrawal")
            balance -= withdrawal
            print("Your available balance is :", balance)
    if option == "3":
        depostie = int(input("Enter Your Amount to deposite"))
        
        if depostie<=10000:
            print("Amount you want to deposite ",depostie)
            print("Your sucessfully deposite amount", depostie)
            balance += depostie
            print(("Your new Balance is  "))
        else:
            print("Pease Deposite amount less than or equal to 10000")
    if option == 4:
            print("Thanks For coming in Sharawat Bank")
        




    
    
