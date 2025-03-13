import re


def is_strong_password(password):
    return bool(strongPassword.match(password))


 
strongPassword = re.compile(r'''(
    ^                 
    (?=.+[a-z])       
    (?=.+[A-Z])       
    (?=.+\d)         
    .{8,}           
    $                 
)''', re.VERBOSE)


test_passwords = [
    "Weakpass",       
    "12345678",       
    "StrongPass1",    
    "Short1",          
    "NoUppercase1",   
    "ALLUPPER123",    
    "Valid123Pass", 
    "8777hyuuhhWesyed#43443"   
]

for pwd in test_passwords:
    print(f"Password: {pwd} -> {'Strong' if is_strong_password(pwd) else 'Weak'}")