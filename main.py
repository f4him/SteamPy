from operation import *
import os
import configparser
import argparse


def get_arguments():
    parser = argparse.ArgumentParser(description="A python script to track your SCM investment profits easily.To make this programm give an efficient output, be as accurate as you can when filling up the investment.ini file. It is recommended that you put the name exactly as they are on SCM.",
    epilog="N.B. profit/loss is calculated after deducting the 15% steam tax.")
    parser.add_argument("-s", "--short",action='store_true', help="generate a short report: name and net profit/loss")
    parser.add_argument("-l","--long",action='store_true', help="generate a full detailed report of your investments")
    return parser.parse_args()
    
def operations(choice):
    if choice.long and choice.short:
        print("Use either -s or -l to generate a report, not both.")
    elif choice.long:
        details()
    elif choice.short:
        shortlist()
    else:
        print("Please use -s or -l with the command to generate a report. For more help, use -h")


def main():
    option = get_arguments()
    operations(option)



if __name__ == "__main__":
    main()
