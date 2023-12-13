# GameEngine.py

from Driver import Driver
from User import User
from Recipe import Recipe, display_recipe, delete_recipe, add_recipe_info_to_json # Import the display_recipes function
from Observer import RecipeObserver, RecipeManager, RecipePrinter
from RecipeOrganizer import RecipeOrganizer
from RecipeDecorator import RecipeDecorator, CommentDecorator, ReviewDecorator
from RecipeFactory import RecipeFactory
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
                    selected_recipe = user.recipes[recipe_number - 1]
                    print(f"Recipe: {selected_recipe.title}")
                    display_recipe(selected_recipe)

                    # For the Decorator Pattern:
                    comment = input("Would you like to leave a comment for this recipe (yes/no): ")
                    if comment == "yes" or comment == "y":
                        RecipeDecorator(selected_recipe)
                        input_comment = input("Please type your comment: ")
                        decorated_recipe = CommentDecorator(selected_recipe, input_comment)
                        decorated_recipe.display(input_comment)

                    review = input("Would you like to leave a review for this recipe (yes/no): ")
                    if review == "yes" or review == "y":
                        RecipeDecorator(selected_recipe)
                        input_review = input("Please type your review: ")
                        decorated_recipe = ReviewDecorator(selected_recipe, input_review)
                        decorated_recipe.display(input_review)

                    #To delete a recipe
                    delete = input("Would you like to delete this recipe (yes/no): ")
                    if delete == "yes" or delete == "y":
                        # remove from Singleton organizer
                        recipe_organizer.remove_recipe(selected_recipe)
                        recipe_organizer.sort_recipes()
                        recipe_organizer.print_recipes()
                        
                        # Notify Observer
                        manager.update_recipe(selected_recipe.title)

                        delete_recipe(selected_recipe, user.recipes)
                    

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
            new_recipe = user.create_recipe()
            user.add_recipe(new_recipe)

            #Add recipe to JSON
            driver.add_recipe_to_json(user.username, new_recipe.title)
            add_recipe_info_to_json(new_recipe)

            # Add to singleton organizer
            recipe_organizer.add_recipe(new_recipe)

            # Notify Observer
            manager.update_recipe(new_recipe.title)

            #Print sorted list via singleotn organizer
            recipe_organizer.sort_recipes()
            recipe_organizer.print_recipes()


        elif choice == '3':
            print("Welcome to the BookMarked!")
            user = driver.prompt_and_create_user()

        else:
            print("Invalid choice. Please try again")
            

if __name__ == "__main__":
    main()



