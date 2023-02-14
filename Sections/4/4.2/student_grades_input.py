# function to calculate the average score
def average_score(scores):
    return sum(scores) / len(scores)

# number of students
num_students = int(input("Enter the number of students: "))

# list to store the test scores of students
scores = []

# loop to get the test scores from the user
for i in range(num_students):
    score = float(input("Enter the score for student {}: ".format(i + 1)))
    scores.append(score)

# call the average_score function to calculate the average
average = average_score(scores)

# print the average score
print("The average score is:", average)
