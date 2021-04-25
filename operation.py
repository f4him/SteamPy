import configparser
from datetime import date
from steam_community_market import *
from get_price import get_curr_price

config = configparser.RawConfigParser()
config.read('investments.ini')

def details():    
    for each_section in config.sections():
        print(each_section)
        print("amount = ", config[each_section]["amount"])
        print("buying price = ",config[each_section]["buying price"])
        current = float(get_curr_price(each_section))
        get = round((current/1.15-0.01),2)
        bp = round(float(config[each_section]["buying price"]),2)
        Amount = int(config[each_section]["amount"])
        print("Current price = ",current)
        
        if(bp > get):
            print("NET LOSS : ", round((bp-get)*Amount,2) )
        else:
            print("NET PROFIT : ", round((get-bp)*Amount,2))

        print("\n\n")
        
    
        
def shortlist():    
    for each_section in config.sections():
        print(each_section)
        current = float(get_curr_price(each_section))
        get = round((current/1.15-0.01),2)
        bp = round(float(config[each_section]["buying price"]),2)
        Amount = int(config[each_section]["amount"])
        if(bp > get):
            print("NET LOSS : ", round((bp-get)*Amount,2) )
        else:
            print("NET PROFIT : ", round((get-bp)*Amount,2))
        print("\n")
        
    