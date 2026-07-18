pin = 1234
balance = 5000
entered_pin =int(input("enter the pin"))
if entered_pin == pin:
    while True:
        print("1.check balance")
        print("2.cash deposit")
        print("3.cash withdrawl")
        print("4.exit")
        choice=int(input("enter your choice"))
        if choice == 1:
            print("your balance is ",balance)
        elif choice == 2:
            amount=int(input("enter the amount"))
            balance+=amount
            print("AMOUNT DEPOSITED SUCCESFULLY")
            print("your current balance is ",amount)    
        elif choice == 3:
             amount=int(input("enter the amount to withdrawl"))
             if amount<=balance:
                 balance-=amount
                 print("AMOUNT WITHDRAWL SUCCESFULLY ",)
             else:
                 print("INSUFFICIENT BALANCE")
        elif choice == 4:
            print("THANKYOU!")
        break  
    else:
        print("INVALID CHOICE")
else:
    print("INVALID PIN")      
                     
        


