import json
import os
from User import User
from Observer import RecipeManager, RecipePrinter
from RecipeDecorator import RecipeDecorator, CommentDecorator, ReviewDecorator
from Recipe import Recipe, Instructions, Ingredient


class Driver:
    def __init__(self):
        self.users = []

    def importUsers():
        file_path = os.path.join(os.path.dirname(__file__), "stored_info.json")
        with open(file_path, "r") as file:
            data = json.load(file)
        users = data["users"]
        for user in users:
            User(user['email'], user['password'], user['username'], user['full_name'])

    # import the previous recipes 
    def importRecipes(username, current_user, recipe_organizer):
        file_path = os.path.join(os.path.dirname(__file__), "stored_info.json")
        with open(file_path, "r") as file:
            data = json.load(file)

        # Find the user in the list
        for user in data["users"]:
            if user["username"] == username:
                #Check if the user had recipes saved
                if user["recipes"]:
                    for recipe in user["recipes"]:
                        #Making the ingredients arr
                        ingredients = []
                        for ing in recipe["ingredients"]:
                            ingredient = Ingredient(name=ing)
                            ingredients.append(ingredient)

                        #Getting the instructions
                        instructions = Instructions(recipe["cook_time"], recipe["temperature"], recipe["directions"])
                        new_recipe = Recipe(recipe["title"], recipe["catergory"], ingredients, instructions)
                        current_user.add_recipe(new_recipe)
                        recipe_organizer.add_recipe(new_recipe)
   
    def intalize(self, recipe_organizer):
        print()
        print("Welcome to the BookMarked!")
        Driver.importUsers()
        user = Driver.prompt_and_create_user()
        Driver.importRecipes(user.username, user, recipe_organizer)
        return user
    
    # This function prompts the creation or login of a user and returns a User object
    def prompt_and_create_user():
        while True:
            #prompt the user to enter their email or username
            user_identification = input("Enter your username or email: ")
            # Check if the user already exists
            for user in User.active_users:
                if user.email == user_identification or user.username == user_identification:
                    return Driver.exsiting_user_login(user)
            # if the user already exists, pass the exisiting user to the login function
            else:
                return Driver.create_new_user()
            
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
                    Driver.add_user_to_json(user_email, username, user_password, full_name)
                    print("New user {} created!".format(user_email))
                    return new_user  # Return the newly created user
                else:
                    print("Your passwords didn't match please try again")
        else:
            print("Login canceled. Goodbye!")
            return None


    # url reference: https://medium.com/@KaranDahiya2000/modify-json-fields-using-python-1b2d88d16908
    def add_user_to_json(email, username, password, full_name):
        file_path = os.path.join(os.path.dirname(__file__), "stored_info.json")
        with open(file_path, "r") as file:
            data = json.load(file)
        #add new user
        new_user = Driver.format_new_user(email, username, password, full_name)
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

    
    def run_simulation(self, user, recipe_organizer):
        while True:
            #OBSERVER PATTERN
            manager = RecipeManager()
            # Create observers
            recipe_observer = RecipePrinter()
            # Add observers to the manager
            manager.add_observer(recipe_observer)

            # Display Menu Options
            print("\nOptions")
            print("1. View your saved recipes")
            print("2. Create a new recipe")
            print("3. Search Recipes")
            print("4. View Grocery List")
            print("5. Sign out")
            #get the choice from the menu
            choice = input("Enter your choice: ")
            # if the choice is 1: view saved recipes
            if choice == '1':
                Driver.viewSavedRecipes(user, recipe_organizer, manager)
            elif choice == '2':
                Driver.createNewRecipe(user, recipe_organizer, manager)
            elif choice == '3':
                Driver.searchRecipes(user, recipe_organizer, manager)
            elif choice == '4':
                user.grocery_procedure()
            elif choice == '5':
                print()
                print("Welcome to the BookMarked!")
                user = Driver.prompt_and_create_user()
            elif choice == '6':
                return False
            else:
                print("Invalid choice. Please try again")

    
    def searchRecipes(user, recipe_organizer, manager): #https://www.geeksforgeeks.org/python-finding-strings-with-given-substring-in-list/
        search_word = input("Search: ")
        print(search_word)
        searched_recipes = []
        for recipe in user.recipes:
            print(recipe.title)
            if search_word.lower() in recipe.title.lower():
                searched_recipes.append(recipe)
        if not searched_recipes:
            print(f"You have no recipes containing '{search_word}'")
        else:
            print(f"Here are the recipes that contain '{search_word}' in their title:")
            print()
            for i, recipe in enumerate(searched_recipes, start=1):
                print(f"{i}. {recipe.title}")
            print(f"{len(searched_recipes)+1}. None")
            search_choice = input("Which one are you interested in taking a look at: ")
            if int(search_choice) <= len(searched_recipes):
                selected_recipe = searched_recipes[int(search_choice) - 1]
                selected_recipe.display_recipe() 
                Driver.inspectRecipe(user, selected_recipe, recipe_organizer, manager)

    
    def createNewRecipe(user, recipe_organizer, manager):
        print()
        new_recipe = user.create_recipe()

        # Add to singleton organizer
        recipe_organizer.add_recipe(new_recipe)

        # Notify Observer
        manager.update_recipe(new_recipe.title)

        #Print sorted list via singleotn organizer
        recipe_organizer.sort_recipes()
        recipe_organizer.print_recipes()
    
    
    def viewSavedRecipes(user, recipe_organizer, manager):
        print()
        if not user.recipes:
            print("No recipes found on your account!")
        else:
            user.display_current_recipes()
            recipe_number = int(input("Enter the number of the recipe to view: "))
            if 1 <= recipe_number <= len(recipe_organizer.recipes):
                selected_recipe = user.recipes[recipe_number - 1]
                print(f"Recipe: {selected_recipe.title}")
                selected_recipe.display_recipe()
                Driver.inspectRecipe(user, selected_recipe, recipe_organizer, manager)
    
    def inspectRecipe(user, selected_recipe, recipe_organizer, manager):
        # For the Decorator Pattern:
        print("Would you like to do any of the following to your recipe:")
        print("1. Leave a comment")
        print("2. Leave a Review")
        print("3. Add ingredients to grocery list")
        print("4. Delete the Recipe")
        print("5. Edit the Recipe")
        print("6. None of the Above")
        choice = input("Enter numerical choice: ")
        print(choice)
        if choice == '1':
            RecipeDecorator(selected_recipe)
            input_comment = input("Please type your comment: ")
            decorated_recipe = CommentDecorator(selected_recipe, input_comment)
            print()
            decorated_recipe.display(input_comment)
        if choice == '2':
            RecipeDecorator(selected_recipe)
            input_review = input("Please type your review: ")
            decorated_recipe = ReviewDecorator(selected_recipe, input_review)
            print()
            decorated_recipe.display(input_review)
        if choice == '3':
            user.add_ingredients_to_grocery_list(selected_recipe)
        if choice == '4': 
            # Remove from Singleton organizer
            recipe_organizer.remove_recipe(selected_recipe)
            user.recipes.remove(selected_recipe)
            recipe_organizer.sort_recipes()
            recipe_organizer.print_recipes()
            
            # Notify Observer
            manager.update_recipe(selected_recipe.title)

            # Delete the recipe
            user.remove_recipe_from_json(selected_recipe, user.username)
        if choice == '5':
            print("You have selected to update your recipe")
            user.remove_recipe_from_json(selected_recipe, user.username)
            user.recipes.remove(selected_recipe)
            
            updated_recipe = selected_recipe.update_recipe(user)

            recipe_organizer.remove_recipe(selected_recipe)
            recipe_organizer.sort_recipes()

            user.add_recipe_to_json(updated_recipe)
            recipe_organizer.add_recipe(updated_recipe)
            user.recipes.append(updated_recipe)
            recipe_organizer.sort_recipes()