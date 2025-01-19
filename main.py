import qrcode
import os
from datetime import date

def main():
    today = date.today()

    try:
        os.mkdir("QR Codes")
    except:
        print("Directory already exists")
        
    os.chdir("QR Codes")    
    try:
        os.mkdir(f"{today} Codes")
    except:
        print("Directory already exists")

        
    os.chdir(f"{today} Codes")    

    # Data to be encoded
    data = 'QR Code using make() function'

    # Encoding data using make() function
    img = qrcode.make(data)

    # Saving as an image file
    img.save('MyQRCode1.png')



    print("Hello World")
    pass

if __name__ == "__main__":
    main()