from StandardRecipe import StandardRecipe
from DrinkRecipe import DrinkRecipe

class RecipeFactory:
    @staticmethod
    def create_recipe_types(recipe_type, **kwargs):
        if recipe_type == "standard":
            return StandardRecipe(**kwargs)
        elif recipe_type == "drink":
            return DrinkRecipe(**kwargs)
        else:
            raise ValueError(f"Invalid recipe type: {recipe_type}")
        