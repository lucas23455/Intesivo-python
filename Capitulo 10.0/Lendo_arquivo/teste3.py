filename = 'text_files/pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readline()

for line in lines:
    print(line.strip())
    