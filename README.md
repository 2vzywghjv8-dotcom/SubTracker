# SubTracker

A lightweight, terminal-based Python application designed to help users track their monthly subscriptions (e.g., Netflix, Spotify, Gym) and calculate total yearly spending. 

Originally developed as a final project for **COMP9001**.

## How to Run

Simply execute `python main.py` in your terminal. 
The program relies strictly on Python's built-in standard library (`json`). No extra external libraries or installations are required!

```bash
python main.py
```

## Advanced Concepts Implemented

To fulfill the requirements for the Advanced Concepts section and ensure program robustness, this project implements the following features:

### 1. File I/O & Data Persistence (`json`)
Utilized the built-in `json` library to safely serialize and save the user's subscription dictionary into a local file (`sub_data.json`). 
- When the user gracefully exits the app, the `save_data()` function writes the current data to the file. 
- When the program is launched again, `load_data()` reads the file so that previous subscriptions are seamlessly restored and never lost.

### 2. Exception Handling & Defensive Programming
To prevent the application from crashing and to improve user experience, robust exception handling was implemented:
- **Input Validation:** In the `add_subscription` function, a `try-except` block specifically catches `ValueError`. If a user accidentally inputs non-numeric characters (like "abc") instead of a numerical value for the cost, the program intercepts the error and prompts them to try again.
- **File System Safety:** In the `load_data` function, exception handling is used to gracefully manage cases where the JSON file might be missing or corrupted upon startup.

## Author
**Yang Chao** (Student ID: 540867369)
