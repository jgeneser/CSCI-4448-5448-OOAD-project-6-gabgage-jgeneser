# GameEngine.py

from Driver import Driver
from User import User
from RecipeOrganizer import RecipeOrganizer
# This function imports all of the users from the stored_info.json file and makes them all users

def main():
    driver = Driver()
    #SINGLETON PATTERN
    recipe_organizer = RecipeOrganizer()

    user = driver.intalize(recipe_organizer)
    driver.run_simulation(user, recipe_organizer)
            
            

if __name__ == "__main__":
    main()



