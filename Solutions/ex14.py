def main():
    while(True):
        first = input("Enter first integer: ")
        if first == "exit":
            break
        second = input("Enter second integer: ")
        if second == "exit":
            break
        third = input("Enter operation (add, sub, mul, div): ")
        if third == "exit":
            break
        elif third == "add":
            print(f'Answer: {float(first) + float(second)}')
        elif third == "sub":
            print(f'Answer: {float(first) - float(second)}')
        elif third == "mul":
            print(f'Answer: {float(first) * float(second)}')
        elif third == "div":
            try: 
                print(f'Answer: {float(first) / float(second)}')
            except:
                print("cannot divide by zero!")
        else:
            print("invalid op")
if __name__ == '__main__':
    main()