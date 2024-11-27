🔐 SHA-256 Hash Cracker
This project is a simple dictionary-based SHA-256 hash cracker. It attempts to find the original password from a given SHA-256 hash using a password list, commonly known as a "dictionary attack." The tool leverages the pwntools library for progress tracking and logging.

🚀 Features
Dictionary Attack: Attempts to match a given SHA-256 hash with passwords from a file.
Real-time Progress Logging: Displays status updates on each password attempt.
Efficient Processing: Handles large password files using a streamlined approach.
📋 Requirements
Python 3.6 or higher
pwntools library
rockyou.txt or any password list file
🛠️ Installation
Clone this repository:

bash
Copy code
git clone https://github.com/yourusername/sha256-cracker.git
cd sha256-cracker
Install the required library:

bash
Copy code
pip install pwntools
Ensure you have a password list (like rockyou.txt) in the project directory or specify its path in the script.

🔧 Usage
bash
Copy code
python3 sha256_cracker.py <target_SHA256_hash>
Replace <target_SHA256_hash> with the actual SHA-256 hash you want to crack.

Example:
bash
Copy code
python3 sha256_cracker.py 5e884898da28047151d0e56f8dc6292773603d0d6aabbddbb9e6f59fcd16b15a
This example uses the SHA-256 hash for the word "password."
