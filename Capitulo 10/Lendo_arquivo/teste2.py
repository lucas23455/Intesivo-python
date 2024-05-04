filename = 'text_files/pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.strip())