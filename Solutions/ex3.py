def main():
    inputlist = input("Enter a list of numbers: ").split(",")
    print(float(inputlist[0]) == float(inputlist[-1]) )

if __name__ == '__main__':
     main()