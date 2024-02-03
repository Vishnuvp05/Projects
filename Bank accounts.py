class BalanceException(Exception):
    pass
class BankAccounts:
    def __init__(self,initial_amount,accname):
        self.balance=initial_amount
        self.name=accname
        print(f"\n Account {self.name} created.\nBalance =${self.balance:.2f}")#.2f to show to decimal points 
    
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
        self.balance=self.balance-amount
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
    def __init__(self,initial_amount,accname):
      super().__init__(initial_amount,accname)
      self.fee=5
    def withdrawel(self,amount):
     try:
       
        self.viableTransaction(amount+self.fee)
        self.balance=self.balance-(amount+self.fee)
        print("\nWithdrawel complete")
        self.get_balance()
     except BalanceException as error:
        print(f'\n Withdrawel interrupted :{error}')

vishnu=BankAccounts(1000,"Vishnu")
prasath=BankAccounts(2000,"prasath")
vishnu.get_balance()
vishnu.deposit(500)
vishnu.withdrawel(10)
vishnu.transfer(10,prasath)
sabik=interestrewardacc(1000,"sabik")
sabik.get_balance()
sabik.deposit(100)
sabik.transfer(100,vishnu)
yogi=savingsacc(1000,"yogi")
yogi.get_balance()
yogi.withdrawel(990)