from RecipeOrganizer import RecipeOrganizer
from Recipe import Recipe, Ingredient, Instructions
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
    def get_instructions():
        cook_time = input("Enter the cook time for instructions: ")
        temperature = input("Enter the cooking temperature: ")
        directions = []
        while True:
            step = input("Enter the cooking step (or 'done' to finish): ").strip()
            if step.lower() == 'done':
                break
            directions.append(step)
        return Instructions(cook_time=cook_time, temperature=temperature, directions=directions)

    # Get user input for a recipe
    def create_recipe(self):
        title = input("Enter the recipe title: ")
        category = input("Enter the recipe category: ")
        recipe_type = input("Enter the recipe type (standard/dessert/soup/drink/meal): ")
        # Get ingredients
        ingredients = User.get_ingredients()
        instructions = User.get_instructions()
        self.recipes.append(Recipe(title=title, category=category, ingredients=ingredients, instructions=instructions)) 

        return Recipe(title=title, category=category, ingredients=ingredients, instructions=instructions)


# This function prompts the creation or login of a user and returns a User object
def prompt_and_create_user():
    while True:
        #prompt the user to enter their email or username
        user_identification = input("Enter your username or email: ")
        # Check if the user already exists
        for user in User.active_users:
            if user.email == user_identification or user.username == user_identification:
                return exsiting_user_login(user)
        # if the user already exists, pass the exisiting user to the login function
        else:
            return create_new_user()
            
# This function carries out the login of an exisiting user
def exsiting_user_login(existing_user):
    #prompt the exisiting user to enter their password
    user_password = input("Enter your password: ")
    # Check if the entered password matches the existing user's password
    if user_password == existing_user.password:
        print()
        print("Welcome back, {}!".format(existing_user.full_name))
        return existing_user  # Return the logged-in user
    else:
        print("Incorrect password. Login failed. Goodbye!")
        return None

# This function carries out the creation of a brand new user
def create_new_user():
    # Asks if they want to create a new user since they dont already have an account
    create_new_user = input("Username or email not found. Do you want to create a new user? (yes/no): ").lower()
    if create_new_user == 'yes' or 'y':
        # if they want to create an account -> get all of their information inorder to create a new user
        while True: 
            full_name = input("Enter your full name: ")
            username = input("Enter your username: ")
            user_email = input("Enter your email address: ")
            user_password = input("Enter your password: ")
            confirm_password = input("Confirm password: ")
            if (user_password == confirm_password):
                # create the new user
                new_user = User(user_email, user_password, username, full_name)
                # update the json file with the new user information
                add_user_to_json(user_email, username, user_password, full_name)
                print("New user {} created!".format(user_email))
                return new_user  # Return the newly created user
            else:
                print("Your passwords didn't match please try again")
    else:
        print("Login canceled. Goodbye!")
        return None


def add_user_to_json(email, username, password, full_name):
    file_path = os.path.join(os.path.dirname(__file__), "stored_info.json")
    with open(file_path, "r") as file:
        data = json.load(file)
    #add new user
    new_user = format_new_user(email, username, password, full_name)
    data["users"].append(new_user)
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)


def format_new_user(email, username, password, full_name):
    return {
        "username": username,
        "email": email,
        "full_name": full_name,
        "password": password,
        "recipes": []
    }

def add_recipe_to_json(username, new_recipe):
    file_path = os.path.join(os.path.dirname(__file__), "stored_info.json")
    with open(file_path, "r") as file:
        data = json.load(file)
    # Find the user in the list
    for user in data["users"]:
        if user["username"] == username:
            # Add the recipe to the user's recipes
            user["recipes"].append(new_recipe)
            break

    # Save the updated data back to the file
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)
