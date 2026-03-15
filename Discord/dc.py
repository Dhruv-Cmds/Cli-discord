import os
import json
import time
import threading
from logger import log

BASE_DIR_DM = "DM"
BASE_DIR_PVT = "Pvtchat"

os.makedirs(BASE_DIR_DM, exist_ok=True)
os.makedirs(BASE_DIR_PVT, exist_ok=True)

class Discord:

    def __init__(self, username):
        self.username = username

    def dm(self, parts):

        print("\n-----------------------------")
        print(" DM Chat")
        print("Press '/e' to leave the chat.")
        print("-----------------------------\n")

        if len(parts) < 2:
            print("Usage: dm <user>\n")
            return

        target = parts[1].capitalize()

        users = sorted([self.username, target])

        filename = "_".join(users) + ".json"

        filepath = os.path.join(BASE_DIR_DM, filename)

        if not os.path.exists(filepath):

            with open(filepath, "w") as f:
                json.dump({"users": users, "messages": []}, f)

        self.chat(filepath)


    def chat(self, filepath):

        running = True
        last_seen = 0

        print("\nChat started...\n")

        log ("Chat STARTED.")

        def receive():

            nonlocal last_seen

            while running:

                with open(filepath, "r") as f:
                    data = json.load(f)

                msgs = data["messages"]

                if len(msgs) > last_seen:

                    for m in msgs[last_seen:]:

                        print(f"\n{m['sender']}: {m['msg']}")

                        print()

                    last_seen = len(msgs)

                time.sleep(1)

        def send():

            nonlocal running

            while True:

                msg = input("msg > ")

                if msg == "/e":

                    running = False

                    print("\nLeaving chat...\n")

                    log ("Chat ENDED")

                    break

                with open(filepath, "r") as f:
                    
                    data = json.load(f)

                data["messages"].append({
                    "sender": self.username,
                    "msg": msg
                })

                with open(filepath, "w") as f:
                    json.dump(data, f, indent=2)

        threading.Thread(target=receive, daemon=True).start()
        send()

    def encrypted_chat(self, parts):

        print("\n=============================")
        print(" Encrypted Private Chat")
        print("Press '/e' to leave the chat.")
        print("=============================\n")

        if len(parts) < 2:
            print("Usage: e2e_chat <user>\n")
            return

        target = parts[1].capitalize()

        users = sorted([self.username, target])

        filename = "_".join(users) + ".json"

        filepath = os.path.join(BASE_DIR_PVT, filename)

        if not os.path.exists(filepath):

            with open(filepath, "w") as f:

                json.dump({"users": users, "messages": []}, f)

        self.chat(filepath)

        os.remove(filepath)

        print("\nPrivate chat deleted.\n")