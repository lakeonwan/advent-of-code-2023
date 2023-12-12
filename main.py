import os
import re

cwd = os.getcwd()  # Get the current working directory (cwd)
# files = os.listdir(cwd)  # Get all the files in that directory
# print("Files in %r: %s" % (cwd, files))

result = 0
with open('day1.dat', 'r') as reader:
    input_data = reader.read().splitlines()

    for line in input_data:
        print(line)
        # use regular expression to filter string on numbers six7sixqrdfive3twonehsk -> 73
        numbers = re.findall(r'\d+', line)
        # get all numbers in list concetenate them together as a string
        digits = ''
        for number in numbers:
            digits += '' + number

        number = digits[0] + digits[-1]
        result += int(number)

print('result: {}'.format(result))

