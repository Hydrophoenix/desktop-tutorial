# to test the While, if, else, break and continue statement
# run this script from an OS shell prompt.
while True: # this run a risk of going on infinitely
	s = input("Enter a word of atleast 4 character or enter\
 q to quit: ")
	if s == 'q':
		break
	if len(s) < 4:
		print("Value is too small, Try Again")
		continue
	else:
		print("The word is of sufficient length")
	raise SystemExit # this code here closes the program