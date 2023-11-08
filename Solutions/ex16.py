import hashlib
def main():
    passwords = {}
    while(True):
        user = input("Enter username: ")
        if(user=="exit"):
            break
        pin = input("Enter password: ")
        if(pin=="exit"):
            break
        passwords[user] = hashlib.sha256(pin.encode()).hexdigest()
    for k,v in passwords.items():
        print(f'{k} : {v}\n')

if __name__ == '__main__':
    main()