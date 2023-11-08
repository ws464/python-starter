def main():
    mylist = [11, 100, 101, 999, 1001]
    left = 0
    right = len(mylist)-1
    while(left < right):
        mylist[left],mylist[right]=mylist[right],mylist[left]
        left+=1
        right=right-1
    print(mylist)

if __name__ == '__main__':
     main()
