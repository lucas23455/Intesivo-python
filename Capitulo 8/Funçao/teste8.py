def get_formatted_name(first_name,last_name,middle_name = ''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name

    return full_name.title()


resultado = get_formatted_name('lucas','passos', 'souza')
print(resultado)

resultado = get_formatted_name('pedro','pereira')
print(resultado)