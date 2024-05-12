import json

def get_stored_username():
    try:
        with open('username.json') as file:
            username = json.load(file)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    username = input("Qual é o seu nome? ")
    with open('username.json', 'w') as file:
        json.dump(username, file)
    return username

def greet_user():
    username = get_stored_username()
    if username:
        correct = input(f"Seu nome é {username}? (s/n) ")
        if correct.lower() == 'n':
            username = get_new_username()
    else:
        username = get_new_username()
    print(f"Bem-vindo de volta, {username}!")

greet_user()
