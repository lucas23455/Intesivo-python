arquivo = 'apredizagem.txt'

with open(arquivo) as file_object:
    contents = file_object.read()

# quando o valor não é necessario usamos '_' para a variavel
for _ in range(3):
    print(contents.rstrip())
    print(' ')
