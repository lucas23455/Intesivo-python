def info(first_name,last_name , age = ''):

    pessoa = {'first': first_name ,'last': last_name}

    if age:
        pessoa ['age'] = age

    return pessoa


resultado = info('maria','silva')
print(resultado)

resultado = info('lucas','passos',21)
print(resultado)