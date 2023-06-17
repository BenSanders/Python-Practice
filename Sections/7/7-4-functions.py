
def mph_and_minutes_to_miles(mph,min):
    hours = min /60
    distance = mph * hours
    return distance

miles_per_hour = float(input())
minutes_traveled = float(input())

print('Miles: {:f}'.format(mph_and_minutes_to_miles(miles_per_hour, minutes_traveled)))