def show_magicians(magicians):
    for magician in magicians:
        print(magician)

def make_great(magicians):
    for i in range(len(magicians)):
        magicians[i] += " o Grande"


magicians = ["Merlin", "Houdini", "David Copperfield", "Penn", "Teller"]
make_great(magicians)
show_magicians(magicians)



