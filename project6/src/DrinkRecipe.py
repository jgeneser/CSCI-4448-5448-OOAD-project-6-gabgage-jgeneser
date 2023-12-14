from Recipe import Recipe

# Inheritance form the Recipe pattern to make the drink recipe
# Also a part of the Factory pattern
# source: https://www.tutorialspoint.com/design_pattern/factory_pattern.htm
class DrinkRecipe(Recipe):
    def __init__(self, title, category, ingredients, instructions):
        super().__init__(title, category, ingredients, instructions)
        self.type = "drink"