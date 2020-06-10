# future upgrade

# find a way to remove the good = 0 and the bad = 0

import que_ans
from termcolor import colored

def question_answer():
	good = 0
	bad = 0
	while True:
		qa = que_ans.QA
		question,answer = qa.new()
		try:
			print("{} = ?".format(question))
			user_answer = input()
			if int(user_answer) != answer:
				print(colored("Wrong! {} = {}","red").format(question,answer))
				bad+=1
			else:
				print(colored("Right!","green")) 
				good+=1
		except:
			return "Your score is {} / {}".format(good,good+bad)			
				

print(question_answer())


