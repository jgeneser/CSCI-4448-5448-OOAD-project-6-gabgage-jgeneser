import os
import json

recipeList = []

class Recipe:
    def __init__(self, title, category, ingredients, instructions):
        self.title = title
        self.category = category
        self.ingredients = ingredients
        self.instructions = instructions
        
        #display the recipe
    def display_recipe(self):
        print("\nTitle:", self.title)
        print("Category:", self.category)
        print("Ingredients:")
        for ingredient in self.ingredients:
            print("  -", ingredient.name)
        print("Instructions:")
        print("  Cook Time:", self.instructions.cook_time)
        print("  Temperature:", self.instructions.temperature)
        print("  Directions:")
        for step in self.instructions.directions:
            print("    -", step)
        print("\n")

class Instructions:
    def __init__(self, cook_time, temperature, directions):
        self.cook_time = cook_time
        self.temperature = temperature
        self.directions = directions

class Ingredient:
    def __init__(self, name):
        self.name = name


def delete_recipe(recipe, user_recipes):
    for rec in user_recipes:
        if rec.title == recipe.title:
            user_recipes.remove(recipe)
            return

def format_new_recipe(recipe):
    ings = []

    for intredient in recipe.ingredients:
        ings.append(intredient.name)

    return {
        "title": recipe.title,
        "catergory": recipe.category,
        "ingredients": ings,
        "cook_time": recipe.instructions.cook_time,
        "temperature": recipe.instructions.temperature,
        "directions": recipe.instructions.directions
    }


def add_recipe_info_to_json(recipe):
    file_path = os.path.join(os.path.dirname(__file__), "recipe_info.json")
    with open(file_path, "r") as file:
        data = json.load(file)
    #add new user
    new_recipe = format_new_recipe(recipe)
    data["recipes"].append(new_recipe)
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

