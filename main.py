import qrcode
import os
from datetime import date

name_count = 0
start_dir = os.getcwd()


def main():
    # create the QR Codes folder if it doesn't exist
    today_str = str(date.today())
    for folder in ["QR Codes", f"{today_str} Codes"]:
        create_select_dir(folder)

    # get the name of the QR Code
    while True :
        qrcode_name = input("Enter the name of the QR Code: ")
        if check_name_forbidden_chars(qrcode_name):
            print("Name contains forbidden characters. Please try again.")
            continue
        
        if confirm_name(input("Are you sure? (Y/N): "), qrcode_name):
                break
    
    data = input("Enter the data you want to encode: ")
    
    # create the QR Code
    try:
        img = qrcode.make(data)
        img.save(check_file_exists(qrcode_name))
    except ValueError:
        print("Invalid data. Please try again.")
        os.chdir(start_dir)
        main()
        return
    print("QR Code created successfully!")


def create_select_dir(directory_name):
    # Create the directory if it doesn't exist
    os.makedirs(directory_name, exist_ok=True)
    os.chdir(directory_name)


def confirm_name(user_input, qr_name):
    # Strip removes leading/trailing whitespaces 
    response = user_input.strip().upper()
    
    if response in ("Y", "YES"):
        print(f"'{qr_name}' Confirmed.")
        return True
    return False


def check_file_exists(qr_name):
    # Check if file exists, if it does, add a number to the end of the name
    global name_count

    while True:
        if name_count == 0:
            file_name = f"{qr_name}.png"
        else:
            file_name = f"{qr_name}({name_count}).png"

        if not os.path.exists(file_name):
            return file_name
        name_count += 1
 
        
def check_name_forbidden_chars(name):
    # Return True if length is too long OR if there's any forbidden character
    forbidden_chars = {'\\', '/', ':', '*', '?', '"', "'", '<', '>', '|'}
    return len(name) > 230 or bool(set(name) & forbidden_chars)


if __name__ == "__main__":
    main()