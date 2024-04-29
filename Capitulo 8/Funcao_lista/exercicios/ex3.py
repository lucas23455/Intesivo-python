def show_magicians(magicians):
    for magician in magicians:
        print(magician)

def make_great(magicians):
    great_magicians = []
    for magician in magicians:
        great_magicians.append(magician + " o Grande")
    return great_magicians

def main():
    magicians = ["Merlin", "Houdini", "David Copperfield", "Penn", "Teller"]
    great_magicians = make_great(magicians[:])  # Passa uma cópia da lista original
    print("Lista original:")
    show_magicians(magicians)
    print("\nLista com 'o Grande' adicionado:")
    show_magicians(great_magicians)


main()
