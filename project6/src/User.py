from RecipeOrganizer import RecipeOrganizer
from Recipe import Recipe, Ingredient, Instructions
from RecipeFactory import RecipeFactory
import os  
import json 

class User:
    active_users = []
    def __init__(self, email, password, username, full_name):
        self.username = username
        self.email = email
        self.password = password
        self.full_name = full_name
        self.recipes = []
        User.active_users.append(self)  # Add the new user to the active_users list

    def display_info(self):
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")

    def add_recipe(self, recipe):
        self.recipes.append(recipe)
    
    def display_current_recipes(self):
        for i, recipe in enumerate(self.recipes, start=1):
            print(f"{i}. {recipe.title}")
        print()

    # Get user input for ingredients
    def get_ingredients():
        ingredients = []
        while True:
            ingredient_name = input("Enter an ingredient (or 'done' to finish): ").strip()
            if ingredient_name.lower() == 'done':
                break
            ingredient = Ingredient(name=ingredient_name)
            ingredients.append(ingredient)
        return ingredients

    # Get user input for instructions
    def get_instructions(recipe_type):
        cook_time = input("Enter the prep time for instructions: ")
        if recipe_type != 'drink':
            temperature = input("Enter the cooking temperature: ")
        else: temperature = None
        directions = []
        while True:
            step = input("Enter the steps (or 'done' to finish): ").strip()
            if step.lower() == 'done':
                break
            directions.append(step)
        return Instructions(cook_time=cook_time, temperature=temperature, directions=directions)

    # Get user input for a recipe
    def create_recipe(self):
        #create a new instance of the factory class
        recipeFactory = RecipeFactory()

        title = input("Enter the recipe title: ")
        category = input("Enter the recipe category: ")
        recipe_type = input("Enter the recipe type (standard/dessert/soup/drink/meal): ")
        # Get ingredients
        ingredients = User.get_ingredients()
        instructions = User.get_instructions(recipe_type)
        new_recipe = recipeFactory.create_recipe_types(recipe_type, title=title, category=category, ingredients=ingredients, instructions=instructions)
        new_recipe = new_recipe.format_new_recipe()
        self.add_recipe_to_json(new_recipe)

        # self.recipes.append(new_recipe)
        return new_recipe

    
    #this function adds the recipe to the json of the user
    def add_recipe_to_json(self, recipe):
        file_path = os.path.join(os.path.dirname(__file__), "stored_info.json")
        with open(file_path, "r") as file:
            data = json.load(file)
        print("Searching through users")
        for user in data['users']:
            if user['username'] == self.username:
                print("Found a matching username!")
                user['recipes'].append(recipe)
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=2)
    

    # this function removes the recipe from the json
    def remove_recipe_from_json(self, recipe):
        file_path = os.path.join(os.path.dirname(__file__), "stored_info.json")
        with open(file_path, "r") as file:
            data = json.load(file)
        print("Searching through users")
        for user in data['users']:
            if user['username'] == self.username:
                print("Found a matching username!")
                user['recipes'].remove(recipe)
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=2)
        
