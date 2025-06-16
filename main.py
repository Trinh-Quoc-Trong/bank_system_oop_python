from models.customer import Customer
from models.account import Account

def main():
    
    """ test 
    # print("main.py")
    # print(__name__)
    """
    customer_ai_nhi = Customer("nguyen thi ai nhi", "buon trap, dak lak", "0374813999")
    # print(customer_ai_nhi)
    # print(customer_ai_nhi.name)
    account_ai_nhi = Account("02072003", customer_ai_nhi, 1000000)
    print(account_ai_nhi)
    

if __name__ == "__main__":
    main() 