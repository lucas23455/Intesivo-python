def greet_users(names):

    for name in names:
        msg = 'Ola ' + name.title() + '!'
        print(msg)



usernames = ['lucas','pedro','maria']


greet_users(usernames)