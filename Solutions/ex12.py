def main():
    num = input("Enter an integer: ")
    if num.isnumeric() or (num[0]=="-" and num[1:].isnumeric()):
        print(int(num)*-1)
    else:
        print(ValueError(f'{num} is not an integer.'))

if __name__ == '__main__':
    main()