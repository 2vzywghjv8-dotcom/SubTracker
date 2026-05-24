"""
Project Name: SubTracker
Course: COMP9001 Final Project

Description:
A simple terminal program to help students track their monthly subscriptions 
(like Netflix, Spotify) and calculate their total yearly spending.

Advanced Concepts Used (For Marking Rubric C):
1. File I/O (JSON): Saves the dictionary data to a json file so it is not lost 
   when the program closes.
2. Exception Handling (try-except): Prevents the program from crashing if the 
   user inputs letters instead of numbers for the cost.
"""

import json

FILE_NAME = "sub_data.json"

def load_data():
    """Load saved data from the JSON file when the program starts."""

    try:
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        print("Warning: Data file is corrupted. Starting fresh.")
        return {}
    except Exception as e:
        print(f"Error loading data: {e}. Starting fresh.")
        return {}

def save_data(subs_dict):
    """Save the dictionary data to a JSON file before quitting."""
    try:
        with open(FILE_NAME, 'w') as file:
            # indent=4 makes the json file easy to read
            json.dump(subs_dict, file, indent=4)
    except Exception as e:
        print(f"Error saving data: {e}")

def add_subscription(subs_dict):
    """Ask the user for a new subscription and add it to the dictionary."""
    name = input("\nEnter subscription name (e.g., Netflix): ").strip().title()
    
    # Make sure the name is not empty
    if name == "":
        print("Name cannot be empty. Please try again.")
        return
    
    is_update = name in subs_dict
    if is_update:
        print(f"Note: '{name}' already exists. Entering a new cost will update it.")
    
    # Use a while loop to keep asking until the user enters a valid number
    while True:
        try:
            # Try to convert the input into a float (decimal number)
            cost = float(input(f"Enter monthly cost for {name} ($): "))
            
            # Cost shouldn't be negative
            if cost < 0:
                print("Cost cannot be negative. Try again.")
                continue
                
            break # Break the loop if the input is valid
            
        except ValueError:
            # Catch the error if the user types letters like "abc"
            print("Invalid input! Please enter a number (e.g., 15.99).")
    
    # Add the new subscription to the dictionary
    subs_dict[name] = cost
    
    if is_update:
        print(f"Successfully UPDATED '{name}' to ${cost:.2f}/month.")
    else:
        print(f"Successfully added '{name}' for ${cost:.2f}/month.")

def view_summary(subs_dict):
    """Print all subscriptions and calculate the total costs."""
    print("\n" + "="*35)
    print("         MY SUBSCRIPTIONS ")
    print("="*35)
    
    # Check if the dictionary is empty
    if len(subs_dict) == 0:
        print("You have no subscriptions. Great job saving money!")
    else:
        total_monthly = 0
        
        sorted_subs = sorted(subs_dict.items(), key=lambda item: item[1], reverse=True)
        
        # Loop through the sorted dictionary to display items
        for name, cost in sorted_subs:
            print(f"- {name:<15}: ${cost:>6.2f}")
            total_monthly += cost
            
        print("-" * 35)
        print(f"Total MONTHLY Cost: ${total_monthly:.2f}")
        
        # Multiply by 12 to get the yearly cost
        total_yearly = total_monthly * 12
        print(f"Total YEARLY Cost:  ${total_yearly:.2f}") 
    print("="*35)

def remove_subscription(subs_dict):
    """Remove a subscription from the dictionary."""
    name = input("\nEnter the exact name of the subscription to remove: ").strip().title()
    
    # Check if the subscription is actually in the dictionary
    if name in subs_dict:
        del subs_dict[name]
        print(f"'{name}' has been removed.")
    else:
        print(f"Could not find '{name}' in your list.")

def main():
    """Main menu loop."""
    print("Welcome to SubTracker! ")
    print("Let's track your subscriptions.")
    
    # Load previous data when we start
    my_subs = load_data()
    
    # Main menu loop
    while True:
        print("\nMain Menu:")
        print("1. Add a new subscription")
        print("2. View summary and costs")
        print("3. Remove a subscription")
        print("4. Save & Exit")
        
        choice = input("\nSelect an option (1-4): ").strip()
        
        if choice == '1':
            add_subscription(my_subs)
        elif choice == '2':
            view_summary(my_subs)
        elif choice == '3':
            remove_subscription(my_subs)
        elif choice == '4':
            # Save data before exiting the program
            save_data(my_subs) 
            print("\nData saved. Have a great day! ")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()