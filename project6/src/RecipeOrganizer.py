from Recipe import Recipe, display_recipe  # Import the display_recipes function
import os  
import json 

oragnizer_recipes = []

class RecipeOrganizer:
    instance = None
    recipes = []

    def newSingle(single):
        # Create a new instance only if it doesn't exist
        if not single.instance:
            single.instance = super(RecipeOrganizer, single).newSingle(single)
        return single.instance

    def add_recipe(self, recipe):
        print()
        RecipeOrganizer.recipes.append(recipe)

    def remove_recipe(self, recipe):
        if recipe in RecipeOrganizer.recipes:
            RecipeOrganizer.recipes.remove(recipe)

    def print_recipes(self):
        print()
        print("Current Recipes:")
        for i, recipe in enumerate(RecipeOrganizer.recipes, start=1):
            print(f"{i}. {recipe.title}")
        print()

    def sort_recipes(self):
        length = len(RecipeOrganizer.recipes)
        for i in range(length):
            for j in range (length - i - 1):
                if RecipeOrganizer.recipes[j].title > RecipeOrganizer.recipes[j + 1].title:
                    RecipeOrganizer.recipes[j], RecipeOrganizer.recipes[j + 1] = RecipeOrganizer.recipes[j + 1], RecipeOrganizer.recipes[j]
        return RecipeOrganizer.recipes
    
