def get_formatted_name(first_name,last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()

resultado = get_formatted_name('lucas','passos')
print(resultado)