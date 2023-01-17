# The following equations estimate the calories burned when exercising (source:https://web.archive.org/web/20121021230025/http://fitnowtraining.com/2012/01/formula-for-calories-burned/):
# 
# Women: Calories = ( (Age x 0.074) — (Weight x 0.05741) + (Heart Rate x 0.4472) — 20.4022 ) x Time / 4.184
# 
# Men: Calories = ( (Age x 0.2017) + (Weight x 0.09036) + (Heart Rate x 0.6309) — 55.0969 ) x Time / 4.184
# 
# Write a program using inputs age (years), weight (pounds), heart rate (beats per minute), and time (minutes), respectively. Output calories burned for women and men.
# 
# Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
# print('Men: {:.2f} calories'.format(calories_man))

# Example input
# 49
# 155
# 148
# 60
# 
# output
# Women: 580.94 calories
# Men: 891.47 calories

print('This program will output calories burned during a workout')

def ask_sex() -> str:
	return str(input("First off is your biological sex male or female?")).lower()

valid_sexes = ["male", "female"]
sex = None

sex = ask_sex()
while sex not in valid_sexes:
	print("Unknown sex, try again")
	sex = ask_sex()
	
print("You have chosen ", sex)

if sex == 'female':
	age = input('Please input your age: ')
	
	# double-checking it's type
	# print(type(women_age))
	# exit()
	
	weight = input('Please input your current weight: ')
	heart_rate =  input('Please input your heart rate: ')
	time = input('Please input the time it took: ')
	
	calories_women = round(( (float(age) * 0.074) - (float(weight) * 0.05741) + (float(heart_rate) * 0.4472) - 20.4022 ) * float(time) / 4.184, 2)
	
	print('Women: {:.2f} calories' . format(calories_women))
if sex == 'male':
	age = input('Please input your age: ')
	weight = input ('Please input your weight: ')
	heart_rate = input('Please input your heart rate: ')
	time = input('Please input your time: ')
	
	calories_men = round(( (float(age) * 0.074) - (float(weight) * 0.05741) + (float(heart_rate) * 0.4472) - 20.4022 ) * float(time) / 4.184, 2)
	
	print('Men: {:2f} calories' . format(calories_men))


	# Sources https://stackoverflow.com/questions/60321405/asking-for-user-input-between-2-genders-using-a-while-loop-and-to-be-stored-in-a