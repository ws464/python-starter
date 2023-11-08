import random

def main():
    num = random.randint(1, 100)
    if num < 10:
        print(f'{num}: You lose.' )
    elif num < 50:
        print(f'{num}: Try again.')
    else:
        print(f'{num}: You win!')

if __name__ == '__main__':
     main()