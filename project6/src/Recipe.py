
recipeList = []

class Recipe:
    def __init__(self, title, category, ingredients, instructions):
        self.title = title
        self.category = category
        self.ingredients = ingredients
        self.instructions = instructions

class Instructions:
    def __init__(self, cook_time, temperature, directions):
        self.cook_time = cook_time
        self.temperature = temperature
        self.directions = directions

class Ingredient:
    def __init__(self, name):
        self.name = name

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
def create_recipe():
    title = input("Enter the recipe title: ")
    category = input("Enter the recipe category: ")
    # Get ingredients
    ingredients = get_ingredients()
    instructions = get_instructions()
    recipeList.append(Recipe(title=title, category=category, ingredients=ingredients, instructions=instructions)) 

    return Recipe(title=title, category=category, ingredients=ingredients, instructions=instructions)

#display the recipe
def display_recipe(recipe):
    print("\nTitle:", recipe.title)
    print("Category:", recipe.category)
    print("Ingredients:")
    for ingredient in recipe.ingredients:
        print("  -", ingredient.name)
    print("Instructions:")
    print("  Cook Time:", recipe.instructions.cook_time)
    print("  Temperature:", recipe.instructions.temperature)
    print("  Directions:")
    for step in recipe.instructions.directions:
        print("    -", step)
    print("\n")

def delete_recipe(recipe, user_recipes):
    for rec in user_recipes:
        if rec.title == recipe.title:
            user_recipes.remove(recipe)
            return
  
# create_recipe()
# display_recipes(recipeList)