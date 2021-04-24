from operation import *
import os
import configparser

def main():
    print("Welcome to SCM investment tracker. You can keep track of your investments here more easily and in an interactive way.")
    config = configparser.ConfigParser()
    i=5
    i=str(i)
    config['ITEM_01'] = {'Name': '45',
                         'Date bought': 'yes',
                         'Amount': '9',
                         'Buying price' : '4',
                         'Current price' : '3',
                         'Net profit/loss' : '5' }
    config['ITEM_02'] = {'Name': '4ss5',
                         'Date bought': 'yasdases',
                         'Amount': '9asda',
                         'Buying price' : '4asdas',
                         'Current price' : '3asdas',
                         'Net profit/loss' : 'fgdfg5' }
    config['ITEM_03'] = {'Name': '4tyrty5',
                         'Date bought': 'ysdfsjes',
                         'Amount': '9aa',
                         'Buying price' : 'tyy4',
                         'Current price' : '3tuf',
                         'Net profit/loss' : '5sssssss' }
    with open('investments.ini', 'w') as configfile:
        config.write(configfile)

    
    # if not os.path.exists('files'):
    #     os.makedirs('files')
    #     file = open('files/invest.txt', 'w+')


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
        edit()
    



#asks users a choice of operations
def ask_choice():
    # return int(input("Enter the number beside the option: \n[1] List investments with full details\n[2] Shortlist of your current investments (Name and Net profit)\n[3] Edit current investment info (add/delete items\ns"))
    return 2


if __name__ == "__main__":
    main()
