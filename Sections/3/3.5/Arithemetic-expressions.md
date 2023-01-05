# Arithmetic expressions
## Basics
* Expression is a combination of items, like variables, literals, operators, and parentheses, that evaluates to a value, like 2*(x+1).

* '+' is the addition operator, as in x + y
* '-' is the subtraction operator, as in x - y. Also, the - operator is for negation, as in -x + y or x + -y
* '*' is the multiplication operator, as in x * y
* '/' is the division operator, as in x / y
* '**' is the exponent operator, as in x `**` y (x to the power of y)

# Evaluation of expressions
Expression evaluates to a value, which replaces the expression

Example:
	If x is 5, then x + 1 evaluates to 6, and y = x + 1 assigns y with 6.
	
	
# Example: Calorie expenditure:
A website lists the calories expended by men and women during exercise as follows (Source)[https://web.archive.org/web/20120422154143/http://fitnowtraining.com/2012/01/formula-for-calories-burned/]:

```
Men: Calories = [(Age × 0.2017) + (Weight × 0.09036) + (Heart Rate × 0.6309) — 55.0969] × Time / 4.184

Women: Calories = [(Age × 0.074) — (Weight × 0.05741) + (Heart Rate × 0.4472) — 20.4022] × Time / 4.184 
```
Below are those expressions written using programming notation: 
```

calories_man = ( (age_years * 0.2017) + (weight_pounds * 0.09036) + (heart_bpm * 0.6309) - 55.0969 ) * time_minutes / 4.184

calories_woman = ( (age_years * 0.074) - (weight_pounds * 0.05741) + (heart_bpm * 0.4472) - 20.4022 ) * time_minutes/ 4.184
```