import pizza
from pizza import askForToppings as top

print("Hey, welcome to your pizza maker!")
n_tps = int(input("How many toppings do you want?"))
pizza.makePizza(top(n_tps))

