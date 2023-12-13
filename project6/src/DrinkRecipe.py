from Recipe import Recipe
class DrinkRecipe(Recipe):
    def __init__(self, title, category, ingredients, instructions, drink_type):
        super().__init__(title, category, ingredients, instructions)
        self.drink_type = drink_type
