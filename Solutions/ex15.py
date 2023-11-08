from datetime import datetime
def main():
    File_object = open(r"output.txt", "w")
    while(True):
        first = input("Enter first integer: ")
        if first == "exit":
            File_object.close()
            break
        second = input("Enter second integer: ")
        if second == "exit":
            File_object.close()
            break
        op = input("Enter operation (add, sub, mul, div): ")
        if op == "exit":
            File_object.close()
            break
        elif op == "add":
            result=float(first)+float(second)
        elif op == "sub":
            result= float(first) - float(second)
        elif op == "mul":
            result = float(first) * float(second)
        elif op == "div":
            try: 
                result = float(first)/float(second)
            except:
                print("cannot divide by zero!")
                continue
        else:
            print("invalid op")
            continue
        print(f'Answer: {result}')
        datestr = datetime.today().strftime('%m/%d/%Y %I:%M:%S %p')
        File_object.write(f'{datestr} {float(first)} {op} {float(second)} = {float(result)}\n')

if __name__ == '__main__':
    main()