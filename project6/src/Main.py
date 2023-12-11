# GameEngine.py
from User import User, prompt_and_create_user
from Recipe import Recipe, create_recipe, display_recipe  # Import the display_recipes function

import json
import os
def importUsers():
    file_path = os.path.join(os.path.dirname(__file__), "stored_info.json")
    with open(file_path, "r") as file:
        data = json.load(file)
    users = data["users"]
    for user in users:
        User(user['email'], user['password'], user['username'], user['full_name'])


def main():
    print("Welcome to the BookMarked!")
    importUsers()
    user = prompt_and_create_user()

    while True:
        print("\nOptions:")
        print("1. View previous recipes")
        print("2. Create a new recipe")
        print("3. Sign out")

        choice = input("Enter your choice: ")

        if choice == '1':
            print()
            if not user.recipes:
                
                print("No recipes found on your account!")
            else:
                user.display_current_recipes()
                recipe_number = int(input("Enter the number of the recipe to view: "))
                if 1 <= recipe_number <= len(user.recipes):
                    selected_recipe = user.recipes[recipe_number - 1]
                    print(f"Recipe: {selected_recipe.title}")
                    display_recipe(selected_recipe)
                    # print("1. View Recipe")
                    # print("2. Exit")
                    # inner_choice = input("Enter your choice: ")
                    # if inner_choice == 1:
                        # display_recipe(selected_recipe)
                    

                #     
                #     print("Ingredients: ", ', '.join(ingredient.name for ingredient in selected_recipe.ingredients))
                #     print("Instructions: ")
                #     print("  Cook Time:", selected_recipe.instructions.cook_time)
                #     print("  Temperature:", selected_recipe.instructions.temperature)
                #     print("  Directions:")
                #     for step in selected_recipe.instructions.directions:
                #         print("    -", step)
                # else:
                #     print("Invalid recipe number.")

        elif choice == '2':
            print()
            new_recipe = create_recipe()
            user.add_recipe(new_recipe)
            print("Recipe added successfully!")

        elif choice == '3':
            print("Welcome to the BookMarked!")
            user = prompt_and_create_user()

        else:
            print("Invalid choice. Please try again")
            

if __name__ == "__main__":
    main()



