#argumentos posicionais
def describe_pet(pet_name, animal_type='cachorro'):
    print(f'\nEu tenho um: {animal_type}')
    print(f'O nome dele é {pet_name}')


describe_pet(pet_name='rex')
describe_pet('wille','gato')
