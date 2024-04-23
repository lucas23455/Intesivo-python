# Teste de igualdade e não igualdade com strings

string1 = 'lucas'
string2 = 'LUCAS'

print(string1 == string2)

#funcao lower
print(string1.lower() == string2.lower())


#teste numerico

num1 = 4
num2 = 2

print(num1 > num2)
print(num1 != num2)
print(num1 <= num2)


#palavras and e or

num3 = 15
print(num1 > num2 and num3 < 20)

print(num1 > num2 or num3 > 20)


#listas

frutas = ['maça','banana','laranja']

print('banana' in frutas)
print('limao' not in frutas)