import random
while(1):

	str1 = """
	1. rock
	2. paper
	3. scissor
	
	4. Quit the game
	"""

	print("Give any input")
	print(str1)
	p = int(input(""))
	if(p == 4):
		break
	q = random.randint(1,3)
	dict1 = {1: "Rock", 2:"Paper", 3:"Scissor"}
	print("Your Choise({}): {}".format(p, dict1[p]))
	print("Computer's Choise({}): {}".format(q, dict1[q]))

	if(p - q == 0):
		print("Game Draw")
	elif(p-q == 1):
		print("You Won")
	elif(p-q == -1):
		print("Computer Won")
	elif(p-q == 2):
		print("Computer Won")
	elif(p-q == -2):
		print("You Won")  
