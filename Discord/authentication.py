from logger import log
import os
import json
import time
from dcpannel import Dcpannel

BASE_DIR = "authenticationdata/userdata.json"

class Authentication:
    
    # sign in page
    def sign_in_page (self):

        print("\nSign in")
        print("1. Login")
        print("2. Register")
        print("3. Exit")

    #  login / register logic
    def logic(self):

        while True:
            
            self.sign_in_page()

            try:
                user_choice = int(input("Choose any option (1-3): "))

            except:
                print("Invalid choice type.")

                log (f"Invalid choice type.")

                continue
                
            user = {
                1 : self.login,
                2 : self.register,
                3 : self.exit
            }

            if user_choice in user:
                user[user_choice]()

            else:
                print("Invalid option")

                log (f"Invalid '{user_choice}' option.")

    #  load user to check if user exsist or not   
    def load_users(self):

        if not os.path.exists(BASE_DIR):        # avoid invalid path or crach
            return {"users": {}}
        
        with open(BASE_DIR , "r") as f:
            return json.load(f)

    #  save user input in .josn file
    def save_users(self , data):

        with open(BASE_DIR , "w") as f:
            json.dump(data, f, indent=4) 

    # login start from here
    def login (self):
          
        data = self.load_users()         # to check if user exsist or not in .json file

        if not data["users"]:

            print("No users registered. Please register first.\n")

            log ("Invalid login.")

            self.register()     # if no user data in .json user redirect to register

            return
          
        while True:

            #  user login / register security protocall

            username = input("Enter your name: ").strip().capitalize()
            password = input("Enter 4-digit password: ").strip()

            if username in data["users"] and data["users"][username] == password:

                print("Login successful.")
                
                log (f"User '{username}' login successful.")

                # send them to after login
                print("\nType 'help' to see all commands.")
                print("Press 'exit' to leave.")

                dcp = Dcpannel(username)    #  after login main dc starts from here
                dcp.main()      # after login user will re-direct to main dc pannel (dcpannel.py)      

                return
            
            else:
                
                print("Invalid credentials.")

                log ("Invalid credentials.")
                
                return

    #  user registresion
    def register(self):

        #  user login / register security protocall

        data = self.load_users()

        while True:

            username = input("Enter your name: ").strip().capitalize()
            password = input("Enter 4-digit password: ").strip()

            if len(password) != 4 or not password.isdigit():
                print("Invalid password.")

                log (f"Invalid '{password}' try.")
                
                continue
            
            confirm_password = input("Confirm your password: ").strip()

            if password != confirm_password:
                print("Passwords do not match.")

                log (f"Invalid '{password}' try.")

                continue

            if username in data["users"]:
                print("User already exists.")

                log(f"User '{username}' already exists.")

                return
            
            data["users"][username] = password
            self.save_users(data)

            print("Registration successful.\n")

            log(f"User '{username}' registered.")
            
            self.login()         # after register user will re-direct to login page

            return


    def exit (self):

        print("Exiting...")

        time.sleep(0.3)

        print("Bye.")

        log ("User logged out.")

        quit()  # make sure system will shut down