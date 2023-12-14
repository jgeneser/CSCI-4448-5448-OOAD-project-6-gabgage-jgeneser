from Recipe import Recipe

# Inheritance form the Recipe pattern to make the standard recipe
# Also a part of the Factory pattern
class StandardRecipe(Recipe):
    def __init__(self, title, category, ingredients, instructions):
        super().__init__(title, category, ingredients, instructions)
        self.type = "standard"