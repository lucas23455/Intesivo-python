arquivo = 'apredizagem.txt'

with open(arquivo) as file_object:
    contents = file_object.read()

print(contents.replace('simplifica','melhora'))
print(contents.replace('python','java'))
