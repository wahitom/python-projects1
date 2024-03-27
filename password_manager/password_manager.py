# Password manager 
from cryptography.fernet import Fernet

# this is for encrypting the key 
# this function only needs to run once
# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key", "wb") as key_file:
#         key_file.write(key)

# write_key()

# load our key
def load_key():
    file = open("key.key", "rb")
    key = file.read()

    # you have to close the file every time you open it
    # file.close()
    return key


master_pwd = input("What is the master password? ")

# convert master password to bytes using .encode()
key = load_key() + master_pwd.encode()
fer = Fernet(key)

def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            # use rstrip to strip the carriage return '/n' when reading the file
            data = line.rstrip()
            
            user, passw = data.split('|')

            # use decode to remove the 'b' for bytes
            decrypted_passw = fer.decrypt(passw.encode()).decode()

            print("User:", user, "| Password:", decrypted_passw)


def add():
    name = input('Account name: ')
    pwd = input('Password: ')

    with open('password.txt', 'a') as f:
        # .encode() will turn your password into bytes
        encrypted_pwd = fer.encrypt(pwd.encode()).decode()
        f.write(name + "|" + encrypted_pwd + "\n")

while True:
    mode = input('Would you like to add a new password or view existing ones?(Type view/add or q to quit) ')

    if mode.lower() == "q":
        quit()

    if mode.lower() == "view":
        view()
    elif mode.lower() == "add":
        add()
    else:
        print("Invalid mode. ")
        continue