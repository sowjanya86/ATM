print("")
print("Welcome to ATM")
print("")
print()
accounts = {
    7661 : ["rupa","24-08-2004",10000,2408],
    7036 : ["anu","16-07-2004",20000,1234],
    8688 : ["sowji","20-01-2004",5000,8716],
    9347 : ["komali","10-03-2003",10000,None],
    8796 : ["akanksha","12-05-2004",10500,8965]
    }
dobm = {1:"January",2:"Feb",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"Sep",10:"Oct",11:"Nov",12:"Dec"}
while True:
    print("Choose Your Option")
    print("1. Withdrawal")
    print("2. Deposit")
    print("3. Pin Generation")
    print("4. Mini statement")
    print("5. Pin Change")
    print("6. Check Balance")
    print("7. Exit")
    option = int(input("Enter Your Option: "))
    print()
    if option == 1:
        print("")
        accno =  int(input("Enter Account Number: "))
        if accno not in accounts:
            print("Account Does not Exist !")
        else:
            pin = int(input("Enter Pin: "))
            if accounts[accno][-1] == None:
                print("Generate Pin")
            else:
                if accounts[accno][-1] != pin:
                    print("Invalid Pin")
                else:
                    amt = int(input("Enter Amount to Withdraw: "))
                    if amt > accounts[accno][-2]:
                        print("Insufficent Funds ")
                    else:
                        print("Withdraw Sucessfull !")
                        accounts[accno][-2] -= amt
        print("")
    elif option == 2:
        print("")
        accno = int(input("Enter Account Number: "))
        if accno not in accounts:
            print("Account does not Exist")
        else:
            amt = int(input("Enter Amount to Deposit: "))
            accounts[accno][-2] += amt
            print("Deposit Sucessfull")
        print("")
    elif option == 3:
        print("")
        accno = int(input("Enter Account Number: "))
        if accno not in accounts:
            print("Account Does not Exists")
        else:
            if accounts[accno][-1] == None:
                pin = int(input("Enter Pin: "))
                cpin = int(input("Confirm Pin: "))
                if pin != cpin:
                    print("Pin Does not Match")
                else:
                    accounts[accno][-1] = pin
                    print("Pin Generated Sucessfully")
            else:
                print("Pin Already Exist")
        print("")
    elif option == 4:
        print("")
        accno = int(input("Enter Account Number: "))
        if accno not in accounts:
            print("Account Does not Exists")
        else:
            pin = int(input("Enter Pin: "))
            if pin != accounts[accno][-1]:
                print("Invalid Pin")
            else:
                print(f"Name: {accounts[accno][0]}")
                print(f"Account Number: {accno}")
                dob = accounts[accno][1].split("-")
                date = dob[0]
                month = dobm[int(dob[1])]
                year = dob[2]
                dob = date + "-" + month + "-" + year
                print(f"Date of Birth: {dob}")
                print(f"Account Balance: {accounts[accno][-2]}")
        print("")
    elif option == 5:
        print("*")
        accno = int(input("Enter Account Number: "))
        if accno not in accounts:
            print("Account Does not Exist")
        else:
            pin = int(input("Enter Pin: "))
            if pin != accounts[accno][-1]:
                print("Invalid Pin")
            else:
                newpin = int(input("Enter New Pin: "))
                conpin = int(input("Confirm Pin: "))
                if newpin != conpin:
                    print("Pin Does not Match")
                else:
                    accounts[accno][-1] = newpin
                    print("Pin Changed Sucessfully")
        print("*")
    elif option == 6: 
        print("")
        accno = int(input("Enter Account Number:"))
        if accno not in accounts:
            print("Account Does not Exists")
        else:
            pin = int(input("Enter Pin: "))
            if pin != accounts[accno][-1]:
                print("Invalid Pin")
            else:
                print(f"Account Balance: {accounts[accno][-2]}")
        print("")
    else:
        break
