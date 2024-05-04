filename = 'text_files/pi_millon_digits.txt'

with open(filename) as file_object:
    lines = file_object.readline()

pi_string = ''
for line in lines:
    pi_string +=line.rstrip()

print(pi_string + '....')
print(len(pi_string))

aniversario = input('coloque sua data de anivesario:')

if aniversario in pi_string:
    print('seu anivesario aparece no numero pi')
else:
    print('naão aparece!!')