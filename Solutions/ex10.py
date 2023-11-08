import re
def main():
    vowelsCount=0
    constCount=0
    word = input("Enter string: ")
    for c in word:
        if re.match("[A,E,I,O,U,a,e,i,o,u]",c):
            vowelsCount+=1
        else:
            constCount+=1
    print(f"Vowels: {vowelsCount}\nConsonants: {constCount}")
if __name__ == '__main__':
    main()