#argumentos posicionais
def describe_pet(animal_type,pet_name):
    print(f'\nEu tenho um: {animal_type}')
    print(f'O nome dele é {pet_name}')


describe_pet(animal_type='gato',pet_name='lalu')
describe_pet(pet_name='nemo', animal_type='peixe')