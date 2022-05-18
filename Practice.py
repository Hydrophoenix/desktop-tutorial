''' This calculator would be used to do either simple or compound intrest'''


def simp_intr(P, R, T):
    # this function does the simple interest calculation & rounds up the answer to 2dp.
    ans = P * R * T
    return round(ans, 2)


def cmpd_intr(P, R, T):
    # this function does the compound interest calculation & rounds up the answer to 2dp.
    ans = P * R**T
    return round(ans, 2)


# Lets first welcome our user
print("Welcome to the Intrest Calculator designed by SUN")

# Find out what activity the user want to do
print("What would you love to do? \n1 Simple Intrest\n2 Compound Intrest")
response = int(
    input("Please choose your preferred activity from the menu above: "))

# Allow the user input the numbers
# The 'int' was used to case the value given to P, r, t
P = int(input("Enter Principal: "))
r = int(input("Enter the rate: "))
t = int(input("Enter the time: "))

# Here we do both intrests
SAA = simp_intr(P, r, t)
CAA = cmpd_intr(P, r, t)
SI = SAA - P
CI = CAA - P

# Now we give the preferred answer to the user
if(response == 1):
    # I used the ',' to nest an int within a str
    print("Your Intrest is", SI)
    print("Your Accured Amount is", SAA)
elif(response == 2):
    print("Your Intrest is", CI)
    print("Your Accured Amount is", CAA)
else:
    print("Invalid selection")
