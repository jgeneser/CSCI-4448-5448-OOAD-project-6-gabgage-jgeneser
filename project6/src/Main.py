# GameEngine.py

from Driver import Driver
from User import User
# This function imports all of the users from the stored_info.json file and makes them all users

def main():
    driver = Driver()
    user = driver.intalize()
    driver.run_simulation(user)
            
            

if __name__ == "__main__":
    main()



