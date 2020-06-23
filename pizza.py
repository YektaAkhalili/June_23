def askForToppings(n):
    tps = ()
    for i in range(n):
        tp = input("topping: ")
        tps += (tp,)
        i += 1
    return tps

def makePizza(*top):
    print("You want a pizza with the following toppings: ")
    for t in top:
        print("\n- " + str(t))
    print("We've got you!")    






