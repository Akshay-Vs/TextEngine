import sys, os
import time
import random
from tqdm import tqdm
from termcolor import colored, cprint


def type(text: str,color="green",typing_speed=50):
    for character in text:
        sys.stdout.write(colored(character,color))
        sys.stdout.flush()
        time.sleep(random.random() * 10.0 / typing_speed )

def display_text(lines: list):
    for line in lines:
       type('c',line + os.linesep)
       time.sleep(0.1)
    print()

def get_input(valid_input: list) -> str:  
    while True:    
        user_entered = input()            
        if user_entered not in valid_input:      
            print(colored("Invalid input. Enter a valid input: ",'red'),end="")
            user_entered = None            
        else:
            return user_entered

def get_response(options: list) -> int:
   
    for index, option in enumerate(options): 
        print(colored(str(index) + f'.)"{option[0]}"','green'))
    
    print()
    print(colored("Please choose an option: ", 'cyan'),end="")

    valid_inputs = [str(num) for num in range(len(options))]
    option_index = int(get_input(valid_inputs))
 
    return options[option_index][1]
    

def show(story: dict):  
    curr_page = 1   
    while curr_page != None:    
        page = story.get(curr_page, None)
        if page == None:
            curr_page = None
            
            break
  
        display_text(page['Text'])
        
        if len(page['Options']) == 0:      
            curr_page = None      
            break     
        
        curr_page = get_response(page['Options'])
        
        if curr_page==101:
        	print(colored('\n\tWarning⚠\n','red'))

def progress(loop,update_by,percent=100,delay=.5):
	load=tqdm(total=percent)
	for i in range(loop):
		time.sleep(delay)
		load.update(update_by)
	load.close()

def exit_with_message(message,color="green"):
    type(message,color)
    os.system("exit()")
def exit():os.system("exit()")

if __name__=="__main__":
    type("Starting Game")
    progress(10,10)
    exit_with_message("Game Over")        
