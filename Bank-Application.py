class Bank:
    def __init__(self,name,acc_no,IFSC_code,branch,amount):
        self.name=name
        self.acc_no=acc_no
        self.IFSC_code=IFSC_code
        self.branch=branch
        self.amount=amount
        print(self.name,self.acc_no,self.IFSC_code,self.branch,self.amount)
    def details(self):
        print("accoun holder name is :",self.name)
        print("your account number is:",self.acc_no)
        print("your branch ifsc code is:",self.IFSC_code)
        print("branch name is :",self.branch)
        print("available amount is:",self.amount)
    def deposit_amount(self):
        self.cash=int(input("how much you want to deposit the amount"))
        self.amount=self.amount+self.cash
        print(f"{self.cash } is deposited successfully")
        print("Available amount is :",self.amount)
    def with_draw(self):
        ask=int(input("enter how much money you want to withdraw:"))
        if self.amount-5000>ask:# 5000 is minimum balance
            self.amount=self.amount - ask
            
            print("please collect your cash",ask)
            print("Available balance is:",self.amount)
        else:
            print("insufficient balance")
    