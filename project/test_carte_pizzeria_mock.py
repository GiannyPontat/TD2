class TestCartePizzeriaMock(unittes.TestCase):
    def  test_is_empty(self):
        carte = CartePizzeria()
        pizza_mock = MagicMock()
        self.assertTrue(carte.is_empty())
        carte.add_pizza(pizza_mock)
        self.assertFalse(carte.is_empty())

    def test_nb_pizzas(self):
        carte = CartePizzeria()
        pizza_mock = MagicMock()
        self.assertEqual(carte.nb_pizzas(), 0)
        carte.add_pizza(pizza_mock)
        self.assertEqual(carte.nb_pizzas(), 1)

    def test_add_pizza(self):
        carte = CartePizzeria()
        pizza_mock = MagicMock()
        carte.add_pizza(pizza_mock)
        self.assertEqual(carte.nb_pizzas(), 1)

    def test_remove_pizza(self):
        carte = CartePizzeria()
        pizza_mock1 = MagicMock()
        pizza_mock1.name = "Margherita"
        pizza_mock2 = MagicMock()
        pizza_mock2.name = "Pepperoni"
        carte.add_pizza(pizza_mock1)
        carte.add_pizza(pizza_mock2)
        carte.remove_pizza("Margherita")
        self.assertEqual(carte.nb_pizzas(), 1)
        self.assertRaises(CartePizzeriaException, carte.remove_pizza, "Hawaïenne")


