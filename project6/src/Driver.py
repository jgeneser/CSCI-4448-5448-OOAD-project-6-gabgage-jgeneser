import json
import os
from User import User, prompt_and_create_user

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
    
    def intalize(self):
        print("Welcome to the BookMarked!")
        Driver.importUsers()
        user = prompt_and_create_user()
        