
# Simple script to generate a list of entries that is a subset
# of entries from a larger file. Use case might be a password
# dictionary that isn't as ponderous as some larger password
# lists.

import random
import linecache

## BEGIN STRINGIO SECTION
##import StringIO
#
## create a multi-line string and pass it into StringIO
#f = StringIO.StringIO('''first line
#second line
#third
#fourth
#fifth''')
#
## now work with f as though it were an opened file
#for line in f:
#    line = line.strip()
#    print line
#
## END STRINGIO SECTION

def file_length(filename):
    i = 0
    for i, lines in enumerate(filename, 1):
    	pass
    return i

#def random_line_number(line_count):
#    random_number = random.randint(0, line_count)
#    return random_number

def list_generator(seed_file, list_length, line_count):
    used_numbers = []
    new_list = []
    while len(new_list) < list_length:
	random_number = random.randint(0, line_count)
        newline = str()
	if random_number not in used_numbers:
            used_numbers.append(random_number)
            newline = linecache.getline(seed_file, random_number)
            new_list.append(newline)
#            new_file.write(newline)
    return new_list

def list_to_file(source_list, output_file):
    for i in range(len(source_list)):
        output_file.write(source_list[i])
        i += 1
    return output_file
#
seed_file = raw_input("Enter the filename that will seed your " \
                      "password list: ")
#
destination_file = raw_input("Enter your new filename: ")
list_length = int(raw_input("Enter the number of entries you would " \
                        "like in your list: "))
#
#seed = open("rockyou.txt", "r")
seed = open(seed_file, "r")
line_count = file_length(seed)
#random_line = random_line_number(line_count)
new_file = open(destination_file, "a")
temp_list = list_generator(seed_file, list_length, line_count)
new_file = list_to_file(temp_list, new_file)
#
#list_generator(seed, new_file, list_length)
seed.close()
new_file.close()
