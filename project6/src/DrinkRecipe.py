from Recipe import Recipe

class DrinkRecipe(Recipe):
    def __init__(self, title, category, ingredients, instructions):
        super().__init__(title, category, ingredients, instructions)
        self.type = "drink"
