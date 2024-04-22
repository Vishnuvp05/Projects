users=[]
class User:
    def __init__(self,user_id,user_name,email,phone_no,password):
        self.user_id=user_id
        self.user_name=user_name
        self.email=email
        self.phone_no=phone_no
        self.password=password
    
    def view_details(self):
        print(f'user_id : {self.user_id}')
        print(f'user_name : {self.user_name}')
        print(f'email : {self.email}')
        print(f'phone_no : {self.phone_no}')

    def validate_login(self,email,password):
        for user in users:
            if user.email==email and user.password==password:
                return user
class BalanceException(Exception):
    pass
class BankAccounts:
    def __init__(self,initial_amount,accname,passkey):
        self.balance=initial_amount
        self.name=accname 
        self.passkey=passkey
    
    def get_balance(self):
        print(f"Account {self.name} balance =${self.balance:.2f}")
    
    def deposit(self,amount):
        self.balance=self.balance+amount
        print("Amount deposit successful")
        self.get_balance()

    def viableTransaction(self,amount):
        if self.balance>=amount:
            return
        else:
            raise BalanceException(f"\n Sorry Account {self.name} has only ${self.balance:.2f}")
    def withdrawel(self,amount):
     try:
        self.viableTransaction(amount)
        self.balance-=amount
        print("\nwithdrawel successful")
        self.get_balance()
     except BalanceException as error:
         print(f'\nWithdrawel interrupted: {error}')
    def transfer(self,amount,account):
     try:
        print("\n**********\n\nBegining Transfer...")
        self.viableTransaction(amount)
        self.withdrawel(amount)
        account.deposit(amount)
        print("\nTransfer completre !\n\n**********")
     except BalanceException as error:
        print(f'\n Transfer interrupted :{error}')
class interestrewardacc(BankAccounts):
   def deposit(self,amount):
      self.balance=self.balance+(amount*1.05)
      print('\nDeposit complete.')
      self.get_balance()
class savingsacc(interestrewardacc):
    def __init__(self,initial_amount,accname,passkey):
      super().__init__(initial_amount,accname,passkey)
      self.fee=5
    def withdrawel(self,amount):
     try:
       
        self.viableTransaction(amount+self.fee)
        self.balance=self.balance-(amount+self.fee)
        print("\nWithdrawel complete")
        self.get_balance()
     except BalanceException as error:
        print(f'\n Withdrawel interrupted :{error}')
class Application:
    def __init__(self):
        self.stay_in=True
        self.bankaccounts=[]
        self.interestrewardacc=[]
        self.savingsacc=[]
        b1=BankAccounts(1000,'adolf',123)
        i1=interestrewardacc(1000,'hulk',123)
        s1=savingsacc(1000,'thor',123)
        self.bankaccounts.append(b1)
        self.interestrewardacc.append(i1)
        self.savingsacc.append(s1)

    def run(self):
        while self.stay_in==True:
            print("-------------------------------")
            print("Welcome to the House Rental App")
            print("1. Register")
            print("2. Login")
            print('3.Exit')
            print('---------------------------------')
            choice =int(input("\nEnter your choice: \n"))
            if choice==1:
                self.register()
            elif choice==2:
                self.login()
            elif choice==3:
                break
            else:
                print("Invalid input please try again")
        print("Thank you for using the app")

    def register(self):
        name=input("Enter your name : ")
        email=input("Enter your mail id : ")
        phone_no=input("Enter your mobile no :")
        password=input('Set your password : ')
        user_id=len(users)+1
        new_user=User(user_id,name,email,phone_no,password)
        users.append(new_user)
        print('Registration Successfull')
    def login(self):
            email=input("Enter your email : ")
            password=input('Enter your password : ')
            user=User.validate_login(self,email,password)
            if user:
                print('Login Succeesful')
                self.user_menu(user)
                self.stay_in=False
            else:
                print("Invalid input please Try again")
    def user_menu(self,user):
        while True:
            print("----------------------------------------------")
            print('User menu')
            print("1.create a Bank account")
            print("2.Interest reward account")
            print("3.create a savings account")
            print('4.log in bankacoount')
            print('5.log in interestreward account')
            print('6.log in savings account')
            print("7.profile")
            print('8.logout')
            print("------------------------------------------------")

            choice=int(input("\nEnter your choice :\n"))

            if choice==1:
                self.create_bankaccount(user)
            elif choice==2:
                self.create_interesrewardacc(user)
            elif choice==3:
                self.create_savingsacc(user)
            elif choice==4:
                self.login_bankaccount()
            elif choice==5:
                self.login_interestrewardacc()
            elif choice==6:
                self.login_savingsacc()
            elif choice==7:
                self.view_profile(user)
            elif choice==8:
                break
            else:
                print("Invalid input please try again")
    def create_bankaccount(self,user):
        accname=input("Enter acc name :")
        amount=int(input("Enter the amount to be deposited :"))
        passkey=int(input('set your passkey :'))
        new_user=BankAccounts(amount,accname,passkey)
        self.bankaccounts.append(new_user)
        print("Bank account created successfully ")
        new_user.get_balance()

    def create_interesrewardacc(self,user):
        accname=input("Enter acc name :")
        amount=int(input("Enter the amount to be deposited :"))
        passkey=int(input('set your passkey :'))
        new_user=interestrewardacc(amount,accname,passkey)
        self.interestrewardacc.append(new_user)
        print("Interest reward account created successfully ")
        new_user.get_balance()

    
    def create_savingsacc(self,user):
        accname=input("Enter acc name :")
        amount=int(input("Enter the amount to be deposited :"))
        passkey=int(input('set your passkey :'))
        new_user=savingsacc(amount,accname,passkey)
        self.savingsacc.append(new_user)
        print("Savings account created successfully ")
        new_user.get_balance()
    
    def view_profile(self,user):
        user.view_details()
    
    def login_bankaccount(self):
        accname=input("Enter the account name :")
        passkey=int(input("Enter the passkey :"))
        for user in self.bankaccounts:
            if user.name==accname and user.passkey==passkey:
                print('---------------------------------')
                print('1.deposit money')
                print("2.withdraw money")
                print("3.transfer to another account")
                print('4.Check balance')
                print('5.Back')
                print("-----------------------------------")

                choice=int(input("Enter your choice :"))
                if choice==1:
                    self.deposit(user)
                elif choice==2:
                    self.withdraw(user)
                elif choice==3:
                    self.transfer(user)
                elif choice==4:
                    user.get_balance()
                elif choice==5:
                    break
                else:
                    print('invalid input')
    def login_interestrewardacc(self):
        accname=input("Enter the account name :")
        passkey=int(input("Enter the passkey :"))
        for user in self.interestrewardacc:
            if user.name==accname and user.passkey==passkey:
                print("---------------------------------")
                print('1.deposit money')
                print("2.withdraw money")
                print("3.transfer to another account")
                print('4.Check balance')
                print('5.Back')
                print("------------------------------------")

                choice=int(input("Enter your choice :"))
                if choice==1:
                    self.deposit(user)
                elif choice==2:
                    self.withdraw(user)
                elif choice==3:
                    self.transfer(user)
                elif choice==4:
                    user.get_balance()
                elif choice==5:
                    break
                else:
                    print('invalid input')

    def login_savingsacc(self):
        accname=input("Enter the account name :")
        passkey=int(input("Enter the passkey :"))
        for user in self.savingsacc:
            if user.name==accname and user.passkey==passkey:
                print("-------------------------------")
                print('1.deposit money')
                print("2.withdraw money")
                print("3.transfer to another account")
                print('4.Check balance')
                print('5.Back')
                print("---------------------------------")

                choice=int(input("Enter your choice :"))
                if choice==1:
                    self.deposit(user)
                elif choice==2:
                    self.withdraw(user)
                elif choice==3:
                    self.transfer(user)
                elif choice==4:
                    user.get_balance()
                elif choice==5:
                    break
                else:
                    print('invalid input')

    def deposit(self,user):
        amount=int(input('Enter the amount to be deposited :'))
        user.deposit(amount)
        

    def withdraw(self,user):
        amount=int(input("Enter the amount to be wothdrawn :"))
        user.withdrawel(amount)
    
    def transfer(self,user):
        amount=int(input("Enter the amount to transfer :"))
        toacc=input("Enter the account name of another account :")
        touser=None
        for i in self.bankaccounts:
            if i.name==toacc:
                touser=i
        for i in self.interestrewardacc:
            if i.name==toacc:
                touser=i
        for i in self.savingsacc:
            if i.name==toacc:
                touser=i
        if touser is None:
            print("Recipient account not found.")
            return

    # Check if the source and target accounts are the same
        if user.name == touser.name:
            print("Cannot transfer to the same account.")
            return

        user.transfer(amount,touser)





if __name__=='__main__':
    user1=User(1,'vishnu','vishnu@gmail','987',"vishnu123")
    user2=User(2,'prasath','prasath@gmail','789',"prasath123")
    users.append(user1)
    users.append(user2)      

    app=Application()
    app.run()
