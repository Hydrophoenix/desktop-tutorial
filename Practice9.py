# find the sum of even number in a list of numbers gotten 4rm a user
num = []
num_even = []
Num_Inputed = 10
# lets collect 10 random numbers from the user
# while on it, lets assign it to a list
while Num_Inputed > 0:
	inputed_num = int(input("Enter number: "))
	Num_Inputed -= 1
	num.append(inputed_num)
	continue

for i in num:
	if i % 2 == 0:
		num_even.append(i)
print("\n")
print(sum(num_even))
