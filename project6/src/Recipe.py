class Recipe:
    def __init__(self, title, category, ingredients, instructions):
        self.title = title
        self.category = category
        self.ingredients = ingredients
        self.instructions = instructions
        self.type = None
        
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
    
    # this function formats the recipe so that it can be added to the json file
    def format_new_recipe(recipe):
        ings = []

        #go through the ingredient Objects and get the title
        for ingredient in recipe.ingredients:
            ings.append(ingredient.name)

        return {
            "title": recipe.title,
            "type": recipe.type,
            "catergory": recipe.category,
            "ingredients": ings,
            "cook_time": recipe.instructions.cook_time,
            "temperature": recipe.instructions.temperature,
            "directions": recipe.instructions.directions
        }

    
    # This fuction updates a selected recipe
    def update_recipe(self):
        print()
        loop = True
        while loop == True:
            # prompt the user to select which part of the recipe they would like update
            print("Which section would you like to update: ")
            print("1. Title")
            print("2. Category")
            print("3. Ingredients")
            print("4. Cook time")
            print("5. Temperature")
            print("6. Directions")
            choice = input("Enter the number of the section you would like to update: ")
            if choice == '1': # update the title
                new_title = input("Enter the new title: ")
                self.title = new_title
            if choice == '2': # update the category
                new_category = input("Enter the new category: ")
                self.category = new_category
            if choice == '3': # update the ingredients
                new_ingredients = []
                while True:
                    ingredient_name = input("Enter an ingredient (or 'done' to finish): ").strip()
                    if ingredient_name.lower() == 'done':
                        break
                    ingredient = Ingredient(name=ingredient_name)
                    new_ingredients.append(ingredient)
                self.ingredients = new_ingredients
            if choice == '4': #update the cooktime
                new_cooktime = input("Enter the new cook time: ")
                self.instructions.cook_time = new_cooktime
            if choice == '5': #update the temperature
                new_temp = input("Enter the new cooking temp: ")
                self.instructions.temperature = new_temp
            if choice == '6': # update the directions
                new_directions = []
                while True:
                    step = input("Enter the cooking step (or 'done' to finish): ").strip()
                    if step.lower() == 'done':
                        break
                    new_directions.append(step)
                self.instructions.directions = new_directions
            # see if the user would like to make any more updated
            continue_to_edit = input("Would you like to continue to edit this recipe? (yes/no): ").lower()
            if continue_to_edit == 'no' or 'n':
                loop = False
        return self


class Instructions:
    def __init__(self, cook_time, temperature, directions):
        self.cook_time = cook_time
        self.temperature = temperature
        self.directions = directions

class Ingredient:
    def __init__(self, name):
        self.name = name