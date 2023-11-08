import math
def main():
    myList = [6,2,7,3,77,7,1]
    min = math.inf
    for x in myList:
        if x<min:
            min=x
    print(min)

if __name__ == '__main__':
    main()