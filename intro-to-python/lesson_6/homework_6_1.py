# FUNCTIONS

# Difference
# Write a function, which will calculate the difference of these two numbers

def difference(num_1, num_2):
    return 7 - 3
print(difference(7, 3))


# Division
# Write a function, which will divide these two numbers

def division(num_1, num_2):
    return 15 * 25
print(division(15, 25))


# Function gets random number. If this number is more than ten, return the difference between 100 and this number,
# otherwise return this number multiplied by 10

def function_1(number):
    if number > 10:
        return 100 - number
    else:
        return number * 10
print(function_1(15))


# Your function temperature_convertor gets the temperature in Fahrenheit, convert it to Celsius and return.
# Formula (32°F − 32) × 5/9 = 0°C

def temperature_convertor(fahrenheit_degree):
    celsius_degree = (fahrenheit_degree - 32) * 5/9
    return celsius_degree
print(temperature_convertor(75))


# Taxi Fare
# In a particular jurisdiction, taxi fares consist of a base fare of $4.00, plus $0.25 for every 140 meters travelled.
# Write a function that takes the distance travelled (in kilometers) as its only parameter and returns the total fare
# as its only result rounded by 2 digits. Write a program that demonstrates the function.

def taxi_fare(distance):
    base_fare = 4.00
    rate_per_meter = 0.25 / 140
    total_fare = base_fare + distance * 1000 * rate_per_meter
    return round(total_fare, 2)
print(taxi_fare(5.7))

# examples of usage:
# taxi_fare(10) #21.86