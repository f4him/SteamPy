import configparser
from datetime import date
from steam_community_market import *
from get_price import get_curr_price

config = configparser.RawConfigParser()
config.read('investments.ini')

def details():
    print("details")
    
    for each_section in config.sections():
        print(each_section)
        print("amount = ", config[each_section]["amount"])
        print("buying price = ",config[each_section]["buying price"])
        current = get_curr_price(each_section)
        print("Current price = ",current)
        
        if(float(config[each_section]["buying price"]) > current):
            print("NET LOSS : ", round(float(config[each_section]["buying price"]) - current,2)*int(config[each_section]["amount"]))
        else:
            print("NET PROFIT : ", round(current - float(config[each_section]["buying price"]),2)*int(config[each_section]["amount"]))

        print("\n\n")
        
    
    
    
    # for each_section in config.sections():
    #     for (each_key, each_val) in config.items(each_section):
    #         print(each_key+" = "+each_val)
    #     print("\n\n")
        
def shortlist():
    for each_section in config.sections():
            print('{} = {}'.format(each_section , config.get(each_section, 'name', raw=False, vars=None)))
            print('Net profit/loss = {}'.format(config.get(each_section, 'Net profit/loss', raw=False, vars=None)))
            print("\n")
       

def change():
    print("To add newly invested items or to change any info on the current item list simply edit the investment.txt file.")