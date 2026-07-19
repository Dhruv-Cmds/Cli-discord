
# CLI Discord (Python)

A terminal-based messaging application built with Python. This project simulates core Discord-like features such as authentication, direct messaging, and temporary encrypted chats within a command-line interface.

---

## Project Overview

This project was developed as a learning exercise to explore:

- JSON-based data storage
- Python file handling
- Multi-threading for real-time updates
- Modular project architecture
- CLI application design

---

## Features

- User authentication (login and registration)
- Command-line interface (Linux-style commands)
- Direct messaging (DM system)
- Temporary encrypted chat (E2E-style messaging)
- JSON-based message storage
- Event logging system
- Real-time message updates using threading
- Clean and modular code structure


## Technical Challenges

▸ Real-time messaging without a network layer — solved 
  using Python threading to poll JSON files for new 
  messages, simulating live chat in a single-machine 
  environment

▸ Session isolation for E2E chats — implemented 
  temporary chat files that are cleared on session end, 
  preventing message persistence between private sessions

▸ Modular CLI design — separated concerns across 8 
  modules (auth, client, server, commands, logger) to 
  mirror how real chat backends are structured

---


## Technologies Used

- Python
- JSON (data storage)
- Threading (real-time updates)
- File system management
- CLI-based interface

---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Dhruv-Cmds/Cli-discord.git
   ```
   
2. Navigate into the project directory:
  ```bash
  cd Cli-discord
  ```
3. Run the program:
  python main.py

---

## Project Structure

```
Discord-Simulator/
│
├── authenticationdata/
│   └── userdata.json
│
├── Discord/
│   ├── authentication.py
│   ├── client.py
│   ├── cmds.py
│   ├── dc.py
│   ├── dcpannel.py
│   ├── logger.py
│   ├── main.py
│   └── server.py
│
├── DM/
│   └── (stored DM conversations).json
│
├── Logs/
│   └── logs.json
│
├── Pvtchat/
│   └── (temporary encrypted chats).json
│
├── screenshots/
│   └── Screenshots
│
├── .gitattributes
├── .gitignore
├── LICENSE
└── README.md
```
---

## How It Works

1. The application starts with a boot menu.
2. Users can register or log in.
3. After authentication, the command panel is displayed.
4. Users interact using CLI commands.
5. Messages are stored in JSON files within the DM directory.
6. Threading enables real-time message updates.

---

## Available Commands
```

help           Show all available commands  
dm <user>      Start a direct message with a user  
e2e_chat       Start a temporary encrypted chat  
clear          Clear the terminal  
exit           Close the application  
```
---

## Example Usage
```
DS> dm Alex 
Press '/e' to leave the chat.

msg > hello  
msg > how are you  
msg > /e  
```
---

## License

This project is licensed under the MIT License.

## Author

Dhruv
