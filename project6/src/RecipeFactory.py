from StandardRecipe import StandardRecipe
from DrinkRecipe import DrinkRecipe
from DessertRecipe import DessertRecipe

# this is the factory pattern to create the different types of recipe
# source: https://www.tutorialspoint.com/design_pattern/factory_pattern.htm
class RecipeFactory:
    @staticmethod
    def create_recipe_types(recipe_type, **kwargs):
        if recipe_type == "standard":
            return StandardRecipe(**kwargs)
        elif recipe_type == "drink":
            return DrinkRecipe(**kwargs)
        elif recipe_type == "dessert":
            return DessertRecipe(**kwargs)
        else:
            raise ValueError(f"Invalid recipe type: {recipe_type}")
        