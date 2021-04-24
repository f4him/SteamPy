# SteamPy
## A tool to track steam market profit



SteamPy is a SCM investment profit tracker for CS:GO items. 
## Features
- All items with buying price and amount are set in a plain text file
- Realtime market price comparison
- Easily tweakable as users personal preferences.




## Tech
- Fully on python


## Installation

SteamPy requires [python](https://www.python.org/) to run.

Download all the files and [create a virtual environment](https://www.geeksforgeeks.org/python-virtual-environment/) in the same directory.
Install all the required libraries:
```sh
pip install -r requirements.txt
```
Fill up the ```investment.ini``` file (price in USD without the $ sign).
Example:
```
[Desert Eagle | The Bronze (Field Tested)]
amount = 3
buying price = 0.41
```
Do this for each of your investment item.
Finally, run the program.
```
python main.py -l
```
## Usage
For a detailed report with all your given info:
```
python main.py -l
```
For a shorter report:
```
python main.py -s
```
For help:
```
python main.py -h
```

## Development

Want to contribute? Great! Feel free to fork or drop any ideas to improve the efficiency and functionality of the tool.
