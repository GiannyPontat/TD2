class CartePizzeria:
    def __init__(self):
        self.pizzas = []


    def is_empty(self):
        return len(self.pizzas) == 0

    def nb_pizzas(self):
        return len(self.pizzas)

    def add_pizzas(self,pizzas):
        self.pizzas.append(pizzas)


    def remove_pizza (self, name):
         for pizza in self.pizzas:
            if pizza.name == name:
            self.pizzas.remove(pizza)
            return
         raise CartePizzeriaException("La pizza n'existe plus dans la carte")
