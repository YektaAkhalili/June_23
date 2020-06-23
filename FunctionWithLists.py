names = ["dolores","teddy","maeve"]

def greet_hosts(l):
    """ l is a list of names that we'll greet"""
    for i in range(len(l)):
        print("\nHello " + l[i].title())

greet_hosts(names)