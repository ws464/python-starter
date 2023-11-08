from datetime import datetime

def main():
    datestr = datetime.today().strftime('%m/%d/%Y')
    File_object = open(r"output.txt", "w")
    File_object.write(f'Today\'s date is: {datestr}.')
    File_object.close()

if __name__ == '__main__':
    main()

