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
    
    def update_recipe(self):
        print()
        while True:
            print("Which section would you like to update: ")
            print("1. Title")
            print("2. Category")
            print("3. Ingredients")
            print("4. Cook time")
            print("5. Temperature")
            print("6. Directions")
            choice = input("Enter the number of the section you would like to update: ")
            if choice == '1':
                new_title = input("Enter the new title: ")
                self.title = new_title
            if choice == '2':
                new_category = input("Enter the new category: ")
                self.category = new_category
            if choice == '3':
                new_ingredients = []
                while True:
                    ingredient_name = input("Enter an ingredient (or 'done' to finish): ").strip()
                    if ingredient_name.lower() == 'done':
                        break
                    ingredient = Ingredient(name=ingredient_name)
                    new_ingredients.append(ingredient)
                self.ingredients = new_ingredients
            if choice == '4':
                new_cooktime = input("Enter the new cook time: ")
                self.instructions.cook_time = new_cooktime
            if choice == '5':
                new_temp = input("Enter the new cooking temp: ")
                self.instructions.temperature = new_temp
            if choice == '6':
                new_directions = []
                while True:
                    step = input("Enter the cooking step (or 'done' to finish): ").strip()
                    if step.lower() == 'done':
                        break
                    new_directions.append(step)
                self.instructions.directions = new_directions
            continue_to_edit = input("Would you like to continue to edit this recipe? (yes/no): ").lower()
            if continue_to_edit == 'no' or 'n':
                return False
        


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

