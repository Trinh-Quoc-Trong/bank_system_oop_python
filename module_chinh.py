# module_chinh.py

def chao_mung():
    """Một hàm có thể được tái sử dụng."""
    print("Chào mừng bạn đến với module!")
    print(__name__)

# print("Câu lệnh này nằm ngoài, nó sẽ luôn chạy khi tệp được đọc.")
# print(__name__)
# Khối code này chỉ chạy khi tệp được thực thi trực tiếp.
if __name__ == "__main__":
    print("---")
    print("Tệp này đang được chạy trực tiếp.")
    chao_mung() 