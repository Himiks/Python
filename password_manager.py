from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    print("hello")
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    file = open("key.key", "rb")
    key_n = file.read()
    file.close()
    return key_n





key = load_key()
fer = Fernet(key)



def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print(f"User: {user}, password: {(fer.decrypt(passw.encode()).decode())}")

def add():
    name = input('Account Name: ')
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


mode = ""
while mode != "quit":
    mode = input("Would you like to add new password or view existing ones (view/add), press q to quit\n").lower()
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid input")
