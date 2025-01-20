import qrcode
import os
from datetime import date

name_count = 0
start_dir = os.getcwd()


def main():
    today = date.today()
    create_select_dir("QR Codes")
    create_select_dir(f"{today} Codes")

    while True :
        qrcode_name = input("Enter the name of the QR Code: ")
        if check_name_forbidden_chars(qrcode_name):
            print("Name contains forbidden characters. Please try again.")
            continue
        else:
            if confirm_name(input("Are you sure? (Y/N): "), qrcode_name):
                break
    
    data = input("Enter the data you want to encode: ")
    
    try:
        img = qrcode.make(data)
    except ValueError:
        print("Invalid data. Please try again.")
        os.chdir(start_dir)
        main()
        return
    
    img = qrcode.make(data)
    img.save(check_file_exists(qrcode_name))
    
    print("QR Code created successfully!")


def create_select_dir(directory_name):
    os.makedirs(directory_name, exist_ok=True)
    os.chdir(directory_name)


def confirm_name(user_input, qr_name):
    if user_input.upper() == "Y" or user_input.upper() == "YES":
        print(f"'{qr_name}' Confirmed.")
        return True
    return False


def check_file_exists(qr_name):
    global name_count
    file_name = f"{qr_name} ({name_count}).png"
    
    while True:
        file_name = f"{qr_name} ({name_count}).png"    
        try:
            #print(f"Checking for {file_name}")
            if not os.path.exists(file_name):
                #print(f"File {file_name} not found.")
                return file_name
        except FileNotFoundError:
            print(f"Exception")
        
        name_count += 1
 
        
def check_name_forbidden_chars(name):
    forbidden_chars = ["\\", "/", ":", "*", "?", "\"","\'", "<", ">", "|"]
    if len(name) > 230:
        return True
    for char in forbidden_chars:
        if char in name:
            return True
    return False

if __name__ == "__main__":
    main()