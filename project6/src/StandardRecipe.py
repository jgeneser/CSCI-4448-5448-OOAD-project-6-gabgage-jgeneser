from Recipe import Recipe
class StandardRecipe(Recipe):
    def __init__(self, title, category, ingredients, instructions, drink_type):
        super().__init__(title, category, ingredients, instructions)