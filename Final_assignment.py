from datetime import datetime 
#For the history

class Bank:    
    Adaccounts= [{"Username": "Steven", "Email": "steven29@gmail.com"}] #admin accounts
    Accounts= [] #user accounts
    balance= 0
    Loan_amount=0
    def __init__(self,user) -> None:     
        Bank.Accounts.append(user)
        
    def show_accounts(self):
        for account in Bank.Accounts:
            print(f"\nUsername: {account.name}   Email: {account.email}   User Id: {account.user_id}")
            
    def delete_user(self,email):
        flag=0
        for account in Bank.Accounts:
            if account.email==email:
                print(f"\nUser {account.name} with id {account.user_id} has been deleted from bank")
                Bank.Accounts.remove(account)
                flag=1
                break
        if flag==0:
            print(f"\nNo account with this email exists\n")
            
class Admin(Bank):
    def __init__(self,name,email):
        self.name= name
        self.email= email
        # self.Acc_type= Acc_type
        #Bank.Adaccounts.append(self)
        
    def show_available_balance(self):
        print(f"\nTotal bank balance is {Bank.balance} Taka")
        
    def show_loan_amount(self):
        print(f"\nTotal {Bank.Loan_amount} taka is due for the users")
        
class User:
    def __init__(self, name, email, address, Acc_type,user_id):
        self.name= name
        self.email= email
        self.address= address
        self.Acc_type= Acc_type
        self.user_id= user_id
        Bank(self)
        self.balance=0
        self.loan=0
        self.loanNumber=0
        self.transaction= []
        
    def diposit(self, amount, date):
        if amount> 0:
            self.balance+=amount
            Bank.balance+=amount
            print(f"\nYour balance is now {self.balance} taka")
            self.transaction.append((amount,"Diposited", date))
            
    def available_balance(self):
        print(f"\nCurrent balance {self.balance} taka")
     
        
    def withdraw(self, amount, date):
        if self.balance >= amount and amount> 0:
            self.balance-=amount
            Bank.balance-=amount
            print(f"\nYour balance is now {self.balance} taka")
            self.transaction.append((amount,"Withdrawed", date))
            
        else:
            print("\nWithdrawal amount exceeded")
            
    def loan(self, amount, date):
        if amount >0 and amount<= Bank.balance:
            Bank.Loan_amount= amount
            Bank.balance-=amount
            self.loan+=amount
            self.loanNumber+=1
            self.transaction.append(amount, "Taken loan", date)
            print("\n{amount} taka loan has been taken by {self.name}")
            
    def transaction_history(self):
        for trans in self.transaction:
            print(*trans)
            
    def transfer_money(self, amount, name):
        if self.balance>=amount and amount> 0:
            self.balance-=amount
            flag=0
            
            for account in Bank.Accounts:
                if account.name== name:
                    flag=1
                    account.balance+=amount
                    print(f"\n{amount} Taka has been transfered to {account.name}'s")
                    break
            if flag==0:
                print("\nAccount does not exist")
            
        else: 
            print("\nNot enough balance")
            
# Admin info- Steven, steven29@gmail.com, 407         
currentUser= None
num= 1372 #for the user id
admin_code= 407 #admins have to enter it to register
Loan= True

while True:
    if currentUser==None:
        start=input("Choose Option-\n1.Admin\n2.User\n3.exit\n")
        if start=='3':
            break
        elif start=='2':
            LR=input("Login or Register? (L/R) ")
            if LR=='R':
                  name= input("Name: ")
                  email= input("Email: ")
                  address= input("Address: ")
                  acc_type= input("Account type: ")
                  num+=1
                  numm=num
                  currentUser= User(name, email, address, acc_type, numm)
                  print(f"\nNew user account is created. Your user ID is {numm}")
                  
            elif LR=='L':
                  email= input("Email: ")
                  user_id=int(input("User Id: "))
                  flag=0
                  for acc in Bank.Accounts:
                      if acc.email==email and acc.user_id== user_id:
                          flag=1
                          currentUser= acc
                          print("\nLogin Succesful")
                          
                  if flag==0:
                      print("\nWrong info. Login failed.")
                
        elif start=='1':
                name= input("Name: ")
                email= input("Email: ")
                code= int(input("Admin code: "))
                flag=0
                if code==admin_code:
                    for acc in Bank.Adaccounts:
                        if acc["Username"]==name and acc["Email"]==email:
                            print("\nLogin successful ")
                            currentUser= Admin(name,email)
                            flag=1
                        
                if flag==0 or code!=admin_code:
                    print("\nWrong info. Try again")
              
                        
    else:
        if currentUser.__class__==Admin:
            print(f"\n1. Show user account list")
            print(f"2. Delete an account")
            print(f"3. See total bank balance")
            print(f"4. See total loan amount")
            print(f"5. Turn off loan feature")
            print(f"6. Create a user account")
            print(f"7. Logout")
            op= input("Choose option ")
            if op=='1':
                currentUser.show_accounts()
                
            elif op=='2':
                email= (input("Enter the email "))
                sure= input("Are you sure ? ")
                if sure=="Yes" or sure=="yes":
                    currentUser.delete_user(email)
                    
            elif op=='3':
                currentUser.show_available_balance()
                
            elif op=='4':
                currentUser.show_loan_amount()
                
            elif op=='5':
                Loan= False
                
            elif op=='6':                
                name= input("Name: ")
                email= input("Email: ")
                address= input("Address: ")
                acc_type= input("Account type: ")
                num+=1
                numm=num
                print(f"\nNew user account is created. The user ID is {numm}")
                
            elif op=='7':
                currentUser= None
        
        elif currentUser.__class__==User:
            print("\n1. Check balance")
            print("2. Diposit money")
            print("3. Withdraw money")
            print("4. Take a loan")
            print("5. Transfer Money")
            print("6. Transaction history")
            print("7. Logout")
            
            op= input("Choose option ")
            
            if op=='1':
                currentUser.available_balance()
                
            elif op=='2':
                amount= int(input("Amount: "))
                date= datetime.today().date()
                currentUser.diposit(amount, date)
                
            elif op=='3':
                amount= int(input("Amount: "))
                date= datetime.today().date()
                currentUser.withdraw(amount, date)
                
            elif op=='4':
                if Loan and currentUser.loanNumber >=2:
                    amount= int(input("Amount: "))
                    date= datetime.today().date()
                    currentUser.loan(amount, date)
                    
                else: 
                    print("\nLoan not available")
                    
            elif op=='5':
                name= input("\nEnter the person's name: ")
                amount= int(input("Enter amount: "))
                currentUser.transfer_money(amount, name)
                
            elif op=='6':
                currentUser.transaction_history()
                
            else:
                currentUser = None
                
                
        
                
            
        
