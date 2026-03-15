import os
from logger import log
from cmds import Commands
from dc import Discord

class Dcpannel:

    def __init__(self, username):
        self.username = username

    def main(self):

        cmds = Commands()   # import Commands from cmds.py
        dc = Discord(self.username)      # import Discrod form dc.py

        while True:

            user_choice = input(f"{self.username}@DS> ").strip()     # avoid extra spaceses

            if user_choice == "": # avoid breaks
                continue

            if user_choice == "exit": #  program exit

                print("Shutting down Discord...")

                log("Discord shutdown.")    # Logs

                break

            if user_choice == "clear":      # os cmd that clear terminal

                os.system("cls" if os.name == "nt" else "clear")

                log ("Chat cleared.")

                continue

            parts =  user_choice.split()    # break user_input into parts
            cmd = parts[0].lower()          # avoid invlaid userinput

            commands = {                    # main cmds menu
                "help" : cmds.dc_command,
                "e2e_chat" : dc.encrypted_chat,
                "dm" : dc.dm
            }

            if cmd in commands:
                commands[cmd](parts)
            
            else:
                print("Unknown command.")
                
                log("Unknown command.")
