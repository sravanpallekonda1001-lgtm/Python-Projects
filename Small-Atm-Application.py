data_base = {}  

class Bank:
    def __init__(self, name, acc_no, IFSC_code, branch, amount, mobile):
        self.name = name
        self.acc_no = acc_no
        self.IFSC_code = IFSC_code
        self.branch = branch
        self.amount = amount
        self.mobile = mobile

    def set_pin(self):
        pin = int(input("Create the 4 digit pin: "))
        data_base[self.mobile] = [None, pin]   
        print("PIN created !!!")

    def generate_otp(self):
        import random
        otp = random.randint(111111, 999999)
        print("OTP sent to your mobile:", otp)
        data_base[self.mobile][0] = otp

    def details(self):
        print("Account holder name:", self.name)
        print("Account number:", self.acc_no)
        print("IFSC code:", self.IFSC_code)
        print("Branch:", self.branch)
        print("Available balance:", self.amount)

    def deposit_amount(self):
        cash = int(input("How much do you want to deposit? "))
        self.amount += cash
        print(f"{cash} deposited successfully")
        print("Available amount:", self.amount)

    def with_draw(self):
        option = input("Withdraw using [otp / pin]: ").lower()

        
        if option == "pin":
            pin = int(input("Enter your 4 digit PIN: "))

            if pin == data_base[self.mobile][1]:
                ask = int(input("Enter amount to withdraw: "))

                if self.amount - ask >= 5000:  
                    self.amount -= ask
                    print("Please collect your cash:", ask)
                    print("Available balance:", self.amount)
                else:
                    print("Insufficient balance")
            else:
                print("Invalid PIN")

        
        elif option == "otp":
            self.generate_otp()
            otp = int(input("Enter OTP: "))

            if otp == data_base[self.mobile][0]:
                ask = int(input("Enter amount to withdraw: "))

                if self.amount - ask >= 5000:
                    self.amount -= ask
                    print("Please collect your cash:", ask)
                    print("Available balance:", self.amount)
                else:
                    print("Insufficient balance")
            else:
                print("Invalid OTP")

        else:
            print("Invalid option! Choose otp or pin.")
