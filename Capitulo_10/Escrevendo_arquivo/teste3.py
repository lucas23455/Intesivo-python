filename = 'programa.txt'

#acrecentando coisas no arquivo existente
with open(filename , 'a') as file_object:
    file_object.write('eu tambem ao encontrar coisas \n')
    file_object.write('eu amo criar app!!')