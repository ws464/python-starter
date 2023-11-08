def main():
    while(True):
        first = input("Enter first integer: ")
        if first == "exit":
            break
        second = input("Enter second integer: ")
        if second == "exit":
            break
        print(f'Answer: {int(first) + int(second)}')

if __name__ == '__main__':
    main()