from pwn import *  
import sys        
import hashlib

if len(sys.argv) != 2:
    print("Invalid arguments!")
    print("Usage: {} <sha256sum>".format(sys.argv[0]))
    exit()

wanted_hash = sys.argv[1] 

attempts = 0


with log.progress(f"Attempting to crack: {wanted_hash}") as p:
    try:
        with open(password_file, "r", encoding='latin-1') as password_list:
            for password in password_list:
                password = password.strip("\n").encode('latin-1')
                password_hash = hashlib.sha256(password).hexdigest()

                p.status("[{}] {} == {}".format(attempts, password.decode('latin-1'), password_hash))

                if password_hash == wanted_hash:
                    p.success("Password found after {} attempts! '{}' hashes to '{}'!".format(attempts, password.decode('latin-1'), password_hash))
                    exit()
                attempts += 1
                
        p.failure("Password hash not found!")

    except FileNotFoundError:
        print(f"Error: Password file '{password_file}' not found.")
    except KeyboardInterrupt:
        print("\nProcess interrupted by user.")
