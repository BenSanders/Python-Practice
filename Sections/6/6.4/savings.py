# Counting with a while loop
# 
# Commonly, a loop should iterate a specific number of times, such as 10 times. The programmer can use a variable to count the number of iterations, called a loop variable. To iterate N times using an integer loop variable i, a loop1 with the following form is used:
# 
# 
# 
# A common error is to forget to include the loop variable update (e.g., i = i +1) at the end of the loop, causing an unintended infinite loop.
# 
# The following program outputs the amount of money in a savings account each year for the user-entered number of years, with $10,000 initial savings and 5% yearly interest:


'''Program that calculates savings and interest'''

initial_savings = 10000
interest_rate = 0.05

print('Initial savings of ${}'.format(initial_savings))
print('at {:.0f}% yearly interest.\n'.format(interest_rate*100))

years = int(input('Enter years: '))
print()

savings = initial_savings
i = 1  # Loop variable
while i <= years:  # Loop condition
	print(' Savings at beginning of year {}: ${:.2f}'.format(i, savings))
	savings = savings + (savings*interest_rate)
	i = i + 1  # Increment loop variable

print('\n')
