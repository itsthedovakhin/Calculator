

while True:
#Author: Asad Aftab
#This is a calculator program


	print("Welcome to Calculator v3!")
	print("1:Addition")
	print("2:Subtraction")
	print("3:Multiplication")
	print("4:Division")
	var = int(raw_input("What would you like to do? "))

	if var == 1:
		def add (): #addition function
			print("Note: Enter an empty space to execute operation")
			total = float(raw_input('enter a number: '))
			while True:
				number = raw_input('enter a number: ')
				if number == '':
					break
				total+=float(number)
			print 'the total is', total

		add()

		while True:
			answer = raw_input('Run again? (y/n): ')
			if answer in ('y', 'n'):
				break
			print 'Invalid input.'
		if answer == 'y':
			continue
		else:
			print 'Goodbye!'
			break
			
	if var == 2: #subtraction function
		def subtract ():
			print("Note: Enter an empty space to execute operation")
			total = float(raw_input('enter a number: '))
			while True:
				number = raw_input('enter a number: ')
				if number == '':
					break
				total-=float(number)
			print 'the total is', total

		subtract()

		while True:
			answer = raw_input('Run again? (y/n): ')
			if answer in ('y', 'n'):
				break
			print 'Invalid input.'
		if answer == 'y':
			continue
		else:
			print 'Goodbye'
			break
			
		while True:
			answer = raw_input('Run again? (y/n): ')
			if answer in ('y', 'n'):
				break
			print 'Invalid input.'
		if answer == 'y':
			continue
		else:
			print 'Goodbye!'
			break
			
	if var == 3: #multiplication function
		def multiply ():
			print("Note: Enter an empty space to execute operation")
			total = float(raw_input('enter a number: '))
			while True:
				number = raw_input('enter a number: ')
				if number == '':
					break
				total*=float(number)
			print 'the total is', total

		multiply()

		while True:
			answer = raw_input('Run again? (y/n): ')
			if answer in ('y', 'n'):
				break
			print 'Invalid input.'
		if answer == 'y':
			continue
		else:
			print 'Goodbye!'
			break
			
	if var == 4:
		def divide (): #division function
			print("Note: Enter an empty space to execute operation")
			total = float(raw_input('enter a number: '))
			while True:
				number = raw_input('enter a number: ')
				if number == '':
					break
				total/=float(number)
			print 'the total is', total

		divide()

		while True:
			answer = raw_input('Run again? (y/n): ')
			if answer in ('y', 'n'):
				break
			print 'Invalid input.'
		if answer == 'y':
			continue
		else:
			print 'Goodbye!'
			break




