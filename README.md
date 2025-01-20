# QR-Generator
[![Open Source Love](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)

A simple Python script to generate and save QR Codes with customizable names, ensuring no invalid or forbidden file characters are used. It also automatically handles duplicate filenames by appending an incremental counter.

## Table of Contents

1. [Features](#features)  
2. [Prerequisites](#prerequisites)  
3. [Installation](#installation)  
4. [Usage](#usage)  
5. [Customization](#customization)  
6. [License](#license)  


## Features

- **Interactive Terminal Prompts**:
  - Prompts the user to enter a name for the QR code.
  - Validates the input to ensure it doesn't contain any forbidden characters.
  - Asks for final confirmation before proceeding.

- **Automatic Directory Creation**:
  - Creates a folder named `QR Codes`.
  - Also creates a date-specific folder named `YYYY-MM-DD Codes` based on the current date.

- **File Naming and Collision Handling**:
  - Checks if a file with the chosen name already exists in the target directory.
  - If a file exists, it appends an incremental index (`(1)`, `(2)`, etc.) to avoid overwriting existing files.

- **Invalid Data Handling**:
  - Catches invalid QR data errors and prompts the user to retry.


## Prerequisites

- **Python 3.7+** (Recommended 3.8 or newer)
- [**qrcode**](https://pypi.org/project/qrcode/) Python package (`pip install qrcode`)
- [**Pillow**](https://pypi.org/project/Pillow/) package is usually installed with `qrcode`, but make sure it's installed if needed.


## Installation

1. **Clone** the repository or **download** the script:

   ```bash
   git clone https://github.com/YourUsername/qr-code-generator.git
   ```

2. **Navigate** to the cloned directory:
   ```bash
   cd qr-code-generator
   ```

3. **Install** required dependencies:
   ```bash
   pip install qrcode Pillow
   ```


## Usage

1. **Run** the script:
  
 ```bash
 python qr_code_generator.py
 ```

2. **Follow** the terminal prompts:
   - You will be asked to enter a name for your QR code.
   - Confirm that the name is correct.
   - Enter the data to be encoded into the QR code.

3. **Check** the output:
   - A `QR Codes` folder and a date-specific folder in the format `YYYY-MM-DD Codes` will be created if they do not already exist.
   - The script will place the generated QR code image (`.png`) in the date-specific folder.


## Customization

Feel free to modify this script to suit your needs:

- **Default Directories**: Change the folder names in the `main()` function if you prefer a different structure.
- **Default Filename**: Adjust how filenames are generated in `check_file_exists` to follow your custom naming rules.
- **QR Code Error Correction / Box Size / Border**:  
  The script uses the basic `qrcode.make` function. For advanced customization, replace it with a `QRCode` object to control error correction levels, box sizes, and borders. For example:

```python
import qrcode
from qrcode.constants import ERROR_CORRECT_L

qr = qrcode.QRCode(
    version=1,
    error_correction=ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
```


## License

This project is open-source and available under the MIT License.

[Creative Commons Zero v1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/)