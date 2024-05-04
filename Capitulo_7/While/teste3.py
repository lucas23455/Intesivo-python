prompt = '\nDida algo:'

prompt += '\ndigite "sair" para terminar o programa'



active = True
while active:
    message = input(prompt)


    if message == 'sair':
        active = False

    else:
        print(message)