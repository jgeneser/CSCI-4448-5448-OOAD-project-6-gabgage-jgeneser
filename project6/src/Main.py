# GameEngine.py

from Driver import Driver
from User import User, prompt_and_create_user, add_recipe_to_json
from Recipe import Recipe, create_recipe, display_recipe, delete_recipe  # Import the display_recipes function
from Observer import RecipeObserver, RecipeManager, RecipePrinter
from RecipeOrganizer import RecipeOrganizer
# This function imports all of the users from the stored_info.json file and makes them all users

def main():
    driver = Driver()
    user = driver.intalize()


    #OBSERVER PATTERN
    manager = RecipeManager()
    # Create observers
    recipe_observer = RecipePrinter()
    # Add observers to the manager
    manager.add_observer(recipe_observer)

    #SINGLETON PATTERN
    recipe_organizer = RecipeOrganizer()



    while True:
        print("\nOptions:")
        print("1. View your saved recipes")
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
                if 1 <= recipe_number <= len(recipe_organizer.recipes):
                    selected_recipe = recipe_organizer.recipes[recipe_number - 1]
                    print(f"Recipe: {selected_recipe.title}")
                    display_recipe(selected_recipe)
                    delete = input("Would you like to delete this recipe (yes/no): ")

                    #To delete a recipe
                    if delete == "yes" or delete == "y":
                        # remove from Singleton organizer
                        recipe_organizer.remove_recipe(selected_recipe)
                        recipe_organizer.sort_recipes()
                        recipe_organizer.print_recipes()
                        
                        # Notify Observer
                        manager.update_recipe(selected_recipe.title)

                        delete_recipe(selected_recipe, user.recipes)
                    


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

            #Add recipe to JSON
            add_recipe_to_json(user.username, new_recipe.title)

            # Add to singleton organizer
            recipe_organizer.add_recipe(new_recipe)

            # Notify Observer
            manager.update_recipe(new_recipe.title)

            #Print sorted list via singleotn organizer
            recipe_organizer.sort_recipes()
            recipe_organizer.print_recipes()


        elif choice == '3':
            print("Welcome to the BookMarked!")
            user = prompt_and_create_user()

        else:
            print("Invalid choice. Please try again")
            

if __name__ == "__main__":
    main()



