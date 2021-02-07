import random

def user_input():
	
	user_choice = 0
	while not (user_choice) in range(1,4):
		try:
			user_choice = int(input("Please enter your choice (1 - 3) : "))
		except ValueError:
			print("Incorrect choice...")
	return user_choice

def convert_rps(user_input: int) -> str: 
	
	switcher={
		1:'rock',
		2:'paper',
		3:'scissors'
	}
	return switcher.get(user_input, "Invalid Choice")

## convert_rps takes int as input and returns rock, paper, or scissors

##randombly select from computer

##def check_win(user_input: int) -> bool

##evaluate the winner

##print result

# Set of instructions for Rock-Paper-Scissors
def rps_instructions():
 
    print()
    print("Instructions for Rock-Paper-Scissors : ")
    print()
    print("Rock crushes Scissors")
    print("Scissors cuts Paper")
    print("Paper covers Rock")
    print()