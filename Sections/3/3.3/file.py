bob_salary = 25000
tom_salary = 30000
bob_salary = tom_salary
tom_salary = tom_salary * 1.2
total_salaries = bob_salary + tom_salary


#bob_salary object is created by the interpreter.
#tom_salary object is created by the interpreter.
#bob_salary is assigned tom_salary, and the 25000 object is garbage collected.
#tom_salary is assigned tom_salary * 1.2.
#total_salaries object is created by the interpreter and is assigned bob_salary + tom_salary

