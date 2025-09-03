'''
Developer Shell Creator (DSC)
Author: filcher
2025, Copyright (C)

FOR FREE USE!
'''

# import modules
import os
import time

from colorama import *

# functions
def cvenv():
    print('Create venv', end='\r')
    os.system("python -m venv .venv")
    print('Create venv [ OK ]', end='\n')
    os.system('clear')

def cfolder():
    print('Create folders', end='\r')
    os.mkdir("src")
    os.mkdir("texture")
    os.mkdir("build")
    print('Create folders [ OK ]', end='\n')
    os.system('clear')

def gitInit():
    print('Git Init', end='\r')
    os.system("git init")
    os.system("touch README.md")
    os.system("touch .gitignore")
    with open(".gitignore", 'w') as file:
        file.write("__pycache__/\n.venv/")
        file.close()
    print('Git Init [ OK ]', end='\n')

# main function
def main():
    percents = 0

    print(f"{Fore.GREEN}Developer Shell Creator{Fore.RESET}")
    print('Creating a Shell: {}%'.format(percents), end='\r\n')
    time.sleep(1)
    cvenv()

    percents += 25
    print('Creating a Shell: {}%'.format(percents), end='\r\n')
    cfolder()
    
    percents += 25
    print('Creating a Shell: {}%'.format(percents), end='\r\n')
    gitInit()

    percents += 50
    print('Creating a Shell: {}%'.format(percents), end='\r\n')
    if (percents == 100):
        print("Done!")

# launch
if __name__ == '__main__':
    init()
    main()