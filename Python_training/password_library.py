import sys
import pyperclip

PASSWORDS = {"email": "duusbhjshs@gmail.com",
             "blog": "hdwcwhdeu", "luggage": "12345678"}

if len(sys.argv) < 2:
    print("Using : python pw.py [name] - copy of password of your account")
    sys.exit()


account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print(f"Password for {account} has been copied in buffer.")
else:
    print(f"There is no such account: {account}")