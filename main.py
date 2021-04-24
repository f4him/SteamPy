from operation import *
import os
import configparser

def main():
    option = ask_choice()

    if(option<1 or option >3):
        print("Please select a valid option")
        ask_choice()
    else:
        operations(option)

# executes individual operations
def operations(choice):
    if choice == 1:
        details()
    elif choice == 2:
        shortlist()
    elif choice == 3:
        change()
    



#asks users a choice of operations
def ask_choice():
    return int(input("What do you want to do? \n[1] List investments with full details\n[2] Shortlist of investments\n[3] Set/Change current investment info (add/delete items\ns"))
    


if __name__ == "__main__":
    main()
