import configparser

config = configparser.ConfigParser()
config.read('investments.ini')

def details():
    print("details")
    
    
    for each_section in config.sections():
        for (each_key, each_val) in config.items(each_section):
            print(each_key+" = "+each_val)
            print("/n/n")
        
def shortlist():
    for each_section in config.sections():
            print('{} = {}'.format(each_section , config.get(each_section, 'name', raw=False, vars=None)))
            print('Net profit/loss = {}'.format(config.get(each_section, 'Net profit/loss', raw=False, vars=None)))
            print("/n")
       

def edit():
    print("Would you like to edit, remove or add an instance?\n[1] Add\n[2] Remove\n[3] Edit  ")
