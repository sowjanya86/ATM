# ATM
ATM System - README
Overview
This Python program simulates an ATM system where users can perform basic banking operations such as withdrawal, deposit, PIN generation, and checking account details (mini-statement). The system manages multiple accounts and ensures security by verifying account numbers and PINs before processing transactions.
Features
Withdrawal - Allows users to withdraw money from their account after PIN verification.
Deposit - Enables users to deposit money into their account.
PIN Generation - Users can generate a PIN if they haven't set one before.
Mini Statement - Displays account details including name, date of birth, and balance.
Exit - Allows users to quit the ATM system.
Account Structure
The accounts are stored in a dictionary with the following structure:
accounts = {
      7661 : ["rupa","24-08-2004",10000,2408],
    7036 : ["anu","16-07-2004",20000,1234],
    8688 : ["sowji","20-01-2004",5000,8716],
    9347 : ["komali","10-03-2003",10000,None],
    8796 : ["akanksha","12-05-2004",10500,8965]
}
Each account consists of:
Account Holder Name
Date of Birth (DD-MM-YYYY format)
Account Balance
PIN (if set, otherwise None)
How the Program Works
The program starts by displaying a welcome message and the main menu.
The user selects an option (1-5) to perform a banking operation.
The program processes the selected option:
Withdrawal: The system verifies the account and PIN, checks for sufficient funds, and deducts the amount.
Deposit: The system verifies the account and adds the deposited amount to the balance.
PIN Generation: If the PIN is not set, the user can generate and confirm a new PIN.
Mini Statement: Displays account details such as name, date of birth (formatted), and balance.
The process repeats until the user chooses to exit.
Error Handling
If an invalid account number is entered, the system notifies the user.
If an incorrect PIN is entered, access to transactions is denied.
If the withdrawal amount exceeds the balance, an insufficient funds message is displayed.
If the PIN confirmation does not match during PIN generation, the user is prompted again.
Example Run
**********************
Welcome to ATM
**********************
Choose Your Option
1. Withdrawal
2. Deposit
3. Pin Generation
4. Mini statement
5. Pin Change
6. Check Balance
7. Exit
Enter Your Option: 1
**********************
Enter Account Number: 1001
Enter Pin: 2408
Enter Amount to Withdraw: 5000
Withdraw Successful!
**********************
Notes
The program runs in a loop until the user selects Exit (Option 7).
The date of birth is formatted with the corresponding month name (e.g., 16-July-2024 instead of 16-07-2024).
The PIN is required for sensitive operations like withdrawal and viewing account details.
Future Improvements
Implement a real database to store user data.
Add more security measures such as PIN masking.
Introduce transaction history for better tracking.
Provide an option to reset the PIN securely.
This ATM system is a simple but effective implementation of basic banking functionalities in Python.
