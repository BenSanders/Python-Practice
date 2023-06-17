def calc_pizza_area():
    pi_val = 3.14159265

    pizza_diameter = 12.0
    pizza_radius = pizza_diameter / 2.0
    pizza_area = pi_val * pizza_radius * pizza_radius
    return pizza_area

print('{:.1f} inch pizza is {:.3f} square inches'
      .format(12, calc_pizza_area()))

def hello_world():
    print("Hello World!")

print(hello_world())

def compute_sum(num1,num2):
    num1 = 2
    num2 = 2
    return num1 + num2

def get_minutes_as_hours(orig_minutes):

    return orig_minutes / 60

minutes = float(input())
print(get_minutes_as_hours(minutes))

def eric_age(name,age):
    return print(f"Hello, {name}. You are {age}")

name = "Eric"
age = 74