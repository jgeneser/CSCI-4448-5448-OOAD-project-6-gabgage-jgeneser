#User.py
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

def prompt_and_create_user():
    while True:
        user_identification = input("Enter your username or email: ")

        # Check if the user already exists
        existing_user = next((user for user in User.active_users if user.email == user_identification or user.username == user_identification), None)

        if existing_user:
            user_password = input("Enter your password: ")
            # Check if the entered password matches the existing user's password
            if user_password == existing_user.password:
                print("Welcome back, {}!".format(existing_user.full_name))
                return existing_user  # Return the logged-in user
            else:
                print("Incorrect password. Login failed. Goodbye!")
                return None
        else:
            create_new_user = input("Username or email not found. Do you want to create a new user? (yes/no): ").lower()

            if create_new_user == 'yes':
                while True: 
                    full_name = input("Enter your full name: ")
                    username = input("Enter your username: ")
                    user_email = input("Enter your email address: ")
                    user_password = input("Enter your password: ")
                    confirm_password = input("Confirm password: ")
                    if (user_password == confirm_password):
                        new_user = User(user_email, user_password, username, full_name)
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
# Example usage:
# prompt_and_create_user()
# print("Second creation to check exisiting user")
# prompt_and_create_user()

# # Accessing the active_users list:
# for user in User.active_users:
#     print(user.email)
