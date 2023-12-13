from StandardRecipe import StandardRecipe
from DrinkRecipe import DrinkRecipe

class RecipeFactory:
    @staticmethod
    def create_recipe(recipe_type, **kwargs):
        if recipe_type == "standard":
            return StandardRecipe(**kwargs)
        # elif recipe_type == "dessert":
        #     return DessertRecipe(**kwargs)
        # elif recipe_type == "soup":
        #     return SoupRecipe(**kwargs)
        elif recipe_type == "drink":
            return DrinkRecipe(**kwargs)
        # elif recipe_type == "meal":
        #     return MealRecipe(**kwargs)
        else:
            raise ValueError(f"Invalid recipe type: {recipe_type}")
        