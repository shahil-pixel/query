class Atm(object):
    """
    Error-
    <bound method Atm.BalanceEnquiry of <__main__.Atm object at 0x000002BCE4ED7FA0>>
    """

    # Ma'am pls help me with this error

    def __init__(self,cardNumber,pinNumber):
        self.cardNumber = cardNumber
        self.pinNumber = pinNumber

    def CashWithdrawal(self,cardNumber,pinNumber):
        cardN = input("Enter cardNumber: ")
        pinN = input("Enter pin number: ")

        if(cardN == cardNumber & pinN == pinNumber):
            Money = input("How much money would you like to withdraw: ")
            print(Money," Has been successfully withdrawed")
        else:
            print("The card number/pin number is incorrect")

    def BalanceEnquiry(self,cardNumber,pinNumber):
        cardN = input("Enter cardNumber: ")
        pinN = input("Enter pin number: ")

        if(cardN == cardNumber & pinN == pinNumber):
            print("Contact 109838282 to check your account balance")    
        else:
            print("The card number/pin number is incorrect")
        

    def DepositCash(self,cardNumber,pinNumber):
        cardN = input("Enter cardNumber: ")
        pinN = input("Enter pin number: ")

        if(cardN == cardNumber & pinN == pinNumber):
            Cash = input("How much cash would you like to deposit: ") 
            print(Cash," Has been successfully deposited")
        else:
            print("The card number/pin number is incorrect")
        
Card = Atm(5555555555554444,5621)

print(Card.BalanceEnquiry)