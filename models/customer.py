"""
this model is for customer

"""

class Customer:
    """
    this class is for customer
    """
    def __init__(self, name: str, address: str, phone_number: str, ):
        """
        create a new customer

        Args:
            name (str): name of customer
            address (str): address of customer
            phone_number (str): phone number of customer
        """
        self.name = name
        self.address = address
        self.phone_number = phone_number
    
    def __str__(self) -> str:
        """
        tra ve 1 chuoi de biet information of customer
        """
        return f"Customer: {self.name}, Address: {self.address}, phone number: {self.phone_number}"