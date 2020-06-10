# future upgrade

# use in the new method, the enum instead of using if

# use the lines below for change when randval == 3

#numbers = [randrange(1, 17) for _ in range(randrange(2,6))]
#question = 'The question is: ' + ' + '.join(map(str, numbers))
#answer = sum(numbers)

from random import randrange

class QA:

	def new(rand_val=None):

		rand_val = randrange(0,7)
		
		if rand_val == 0:
			a = randrange(4,60)
			question = "question is {}/2".format(a*2)
			answer = a
		elif rand_val == 1:
			a,b = (randrange(1,40),randrange(1,30))
			question = "question is {} - {}".format(a,b)
			answer = a-b
		elif rand_val == 2:
			a,b = randrange(2, 9),randrange(2, 12)
			question = "question is {} x {}".format(a,b)
			answer = a*b
		elif rand_val == 3:
			answer = randrange(1,21)
			question = str(answer)
			for i in range(randrange(2,6)):
				a = randrange(1,17)
				if randrange(100) < 70:
					answer += a
					question += " + {}".format(a)
				else:
					answer -= a
					question += " - {}".format(a)
			question = "question is {}".format(question)
		elif rand_val == 4:
			a = randrange(20,60) * randrange(25,55) * randrange(2,15)
			b = randrange(25,50) * randrange(15,65) * randrange(2,10)
			question = "question is {} + {}".format(a,b)
			answer = a+b
		else: #ok
			a,b = randrange(1,120), randrange(1,80)	
			question = "question is {} + {}".format(a,b)
			answer = a+b
		return question,answer