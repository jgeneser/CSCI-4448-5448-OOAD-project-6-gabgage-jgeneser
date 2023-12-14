from Recipe import Ingredient, Instructions
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
        self.grocery_list = []
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

    def add_ingredients_to_grocery_list(self, selected_recipe):
        #NEED TO CHECK FOR DUPLICATES
        for ingredient in selected_recipe.ingredients:
            self.grocery_list.append(ingredient.name)

    def grocery_procedure(self):
        self.view_grocery_list()
        self.grocery_list_actions()
    
    def view_grocery_list(self):
        print()
        print(f"{self.full_name}'s Grocery List:")
        for i, item in enumerate(self.grocery_list, start=1):
            print(f"{i}. {item}")
    
    def grocery_list_actions(self):
        print("\nWould you like to do any of the following to your grocery list:")
        print("1. Add Individual Item")
        print("2. Remove Items")
        print("3. Clear All Items")
        print("4. None")
        choice = input("Input your choice here: ")
        if choice == '1':
            self.add_to_grocery_list()
            print("Updated Grocery List:")
            self.view_grocery_list()
        if choice == '2':
            self.remove_from_grocery_list(False)
            print("Updated Grocery List:")
            self.view_grocery_list()
        if choice == '3':
            self.remove_from_grocery_list(True)
            print("Updated Grocery List:")
            self.view_grocery_list()
        

    
    def remove_from_grocery_list(self, remove_all):
        #if removed items is one larger then the length of the list cleat the whole list
        if remove_all: #if the user has selected to remove all of the grocery list contence clear the grocery list
            self.grocery_list.clear()
        else:
            removed_list = []
            removed_items = input("Enter the number next to the items that you would like to remove (seperated by a comma): ")
            removed_items = removed_items.split(",") 
            for num in removed_items:
                removed_list.append(self.grocery_list[int(num)-1])
            for item in removed_list:
                self.grocery_list.remove(item)

    def add_to_grocery_list(self):
        #NEED TO CHECK FOR DUPLICATES
        added_items = input("Enter the number the names of the items you would like to add (seperated by a comma): ")
        added_items = added_items.split(",")
        for item in added_items:
            self.grocery_list.append(item)
            print(item)


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
        recipe_type = input("Enter the recipe type (standard/dessert/drink): ")
        # Get ingredients
        ingredients = User.get_ingredients()
        instructions = User.get_instructions(recipe_type)
        new_recipe = recipeFactory.create_recipe_types(recipe_type, title=title, category=category, ingredients=ingredients, instructions=instructions)
        self.add_recipe_to_json(new_recipe)
        self.add_recipe(new_recipe)
        # self.recipes.append(new_recipe)
        return new_recipe

    
    #this function adds the recipe to the json of the user
    def add_recipe_to_json(self, recipe):
        file_path = os.path.join(os.path.dirname(__file__), "stored_info.json")
        with open(file_path, "r") as file:
            data = json.load(file)
        for user in data['users']:
            if user['username'] == self.username:
                new_recipe_json = recipe.format_new_recipe()
                user['recipes'].append(new_recipe_json)
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=2)
    

    # this function removes the recipe from the json
    def remove_recipe_from_json(self, delete_this_recipe, username):
        file_path = os.path.join(os.path.dirname(__file__), "stored_info.json")
        with open(file_path, "r") as file:
            data = json.load(file)

        # Find the user by username
        user_index = None
        for i, user in enumerate(data['users']):
            if user['username'] == username:
                user_index = i
                break

        # If the user is found, remove the recipe by title
        if user_index is not None:
            recipes = data['users'][user_index]['recipes']
            updated_recipes = [recipe for recipe in recipes if recipe['title'] != delete_this_recipe.title]
            data['users'][user_index]['recipes'] = updated_recipes

            # Save the modified data back to the file
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=2)
        else:
            print(f"User with username '{username}' not found.")

