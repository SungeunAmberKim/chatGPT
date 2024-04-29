import csv
import re

line = "Moe s2342tole $882 sldfkjsa 34 alksdjf 234234 123123. 444323432"
regex = r"\d+"
match = re.search(regex, line)
print(match.group())

# input_file = 'wah.csv'
# output_file = 'sda.csv'
# li = ['a','b','c']

# with open(input_file, 'r') as infile:
#     # Open the output file for writing
#     with open(output_file, 'w', newline='') as outfile:
#         # Create CSV reader and writer objects
#         reader = csv.reader(infile)
#         writer = csv.writer(outfile)
#         index = 0
#         # Iterate over each row in the input file
#         for row in reader:
#             # Add the new element to each row
#             row.append(li[index])
#             # Write the modified row to the output file
#             writer.writerow(row)
#             index += 1