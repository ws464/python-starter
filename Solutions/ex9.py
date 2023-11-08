def main():
    inp = input("Enter a string: ")
    upper = True
    for c in inp:
        if ord(c) <65 or ord(c)>90:
            upper=False
            break
    print(upper)

if __name__ == '__main__':
    main()