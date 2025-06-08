"""
this model is for account
    """

from customer import Customer

class Account:
    """
    dai dien cho 1 account in the bank
    """
    def __init__(self, so_tai_khoan: str, chu_tai_khoan: Customer, so_du: float = 0):
        """
        create a new bank account
        
        :param so_tai_khoan: Số tài khoản.
        :param chu_tai_khoan: Đối tượng KhachHang là chủ tài khoản.
        :param so_du: Số dư ban đầu, mặc định là 0. 
        """
        self.so_tai_khoan = so_tai_khoan
        self.chu_tai_khoan = chu_tai_khoan
        self.so_du = so_du
        
        
    def nap_money(self, so_tien: float):
        """
        nap 1 so tien vao tai khoan 
        voi dieu kien la so tien can nap phai lon hon 0
        Args:
            so_tien (float): so tien can nap
        """
        if so_tien > 0:
            self.so_du += so_tien
            print(f"ban da nap thanh cong {so_tien} vao tai khoan cua ban, so du hien tai la {self.so_du}")
        else:
            pritn("so tien nap phai lon hon 0")
    
    def rut_tien(self, so_tien = float):
        """
        rut tien ra khoi tai khoan

        Args:
            so_tien (float): so tien can rut
        """
        
        if so_tien >0:
            if so_tien <= (self.so_du - 1000):
                self.so_du -= so_tien
                print(f"ban da rut thanh cong {so_tien} vao tai khoan cua ban, so du hien tai la {self.so_du}")
            else:
                
                print("so tien rut phai lon hon 0 va nho hon so du")
        else:
            print("so tien rut phai lon hon 0")
