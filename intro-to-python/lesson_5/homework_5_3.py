# WHILE LOOPS EXERCISES

# Enter a random string in the variable string_1, then enter a character and save it in the variable char_1.
# Write code, which will count how many times your character is included in your string.
# Save result to result_1 variable

string_1 = "Hello, Children!"
char_1 = "l"

result_1 = string_1.count(char_1)

print(result_1)


# Enter a random number and save it in variable number_1. Then create code to multiply all the digits together
# and save result in the result_2 variable.

number_1 = "54321"
result_2 = 1

for digit in str(number_1):
    result_2 *= int(digit)

print(result_2)


# Enter a random number and save it in variable number_2. Then create code which will return
# a number with digits of number_1 in reverse order. Save it in result_3 variable

number_2 = "561703"
result_3 = int(str(number_2)[::-1])

print(result_3)