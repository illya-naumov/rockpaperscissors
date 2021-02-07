from random import randint

def user_input():
	
	user_choice = 0
	while not (user_choice) in range(1,4):
		try:
			user_choice = int(input("Please enter your choice (1 - 3) : "))
		except ValueError:
			print("Incorrect choice...")
	return user_choice - 1

## user_input asks user for input (1-3), and returns their selection

def convert_rps(user_input: int) -> str: 
	
	switcher={
		0:'ROCK',
		1:'PAPER',
		2:'SCISSORS'
	}
	return switcher.get(user_input, "Invalid Choice")

## convert_rps takes int as input and returns rock, paper, or scissors

def computer_selection() -> int:

	return randint(0,2)

## conputer_selection uses randint from the random library to return a choice for the opponent 

def check_win(user_num: int, computer_num: int) -> str:
    result_table = [[2, 0, 1],
           		    [1, 2, 0],
             	    [0, 1, 2]]
    results = ["Lost", "Won", "Tied"]         	    
    return results[result_table[user_num][computer_num]]

## check_win() takes user_num and computer_num as inputs and returns the game result
## based on the result_table matrix


def rps_instructions():
 
    print()
    print("Select ROCK, PAPER, OR SCISSORS : ")
    print()
    print("1) Rock")
    print("2) Paper")
    print("3) Scissors")
    print()


def intro():

	print("=========================================")
	print("==     Welcome to ROCK                 ==")
	print("==                  PAPER              ==")
	print("==                    SCISSORS         ==")
	print("==   COVID SELF EDUCATION EPISODE 1    ==")
	print("==                                     ==")
	print("==          Implemented by             ==")
	print("==           ILLYA NAUMOV              ==")
	print("=========================================")


def game():

	user_choice = user_input()
	computer_choice = computer_selection()


	print('You have selected {}.'.format(convert_rps(user_choice)))
	print('The computer has selected {}.'.format(convert_rps(computer_choice)))
	print('You have {}.'.format(check_win(user_choice, computer_choice)))
	print()
	if input('Type \'n\' to play again! ') in 'n':
		game()



intro()
rps_instructions()
game()	