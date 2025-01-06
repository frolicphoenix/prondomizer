import random
import json

def add_project(projects):
    name = input("Enter project name: ")
    projects.append({"name": name, "locked": False})
    print(f"Added project: {name}")

def get_random_project(projects):
    available_projects = [p for p in projects if not p["locked"]]
    if available_projects:
        chosen = random.choice(available_projects)
        chosen["locked"] = True
        return chosen
    return None

def save_projects(projects):
    with open("projects.json", "w") as f:
        json.dump(projects, f)

def load_projects():
    try:
        with open("projects.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def main():
    print("Welcome to Project Randomizer!")
    projects = load_projects()
    
    chosen_project = None
    
    while True:
        action = input("Enter 'a' to add a project, 'r' for random project, or 'q' to quit: ")
        if action.lower() == 'q':
            break
        elif action.lower() == 'a':
            add_project(projects)
        elif action.lower() == 'r':
            chosen_project = get_random_project(projects)
            if chosen_project:
                print(f"Your random project: {chosen_project['name']}")
            else:
                print("No available projects!")
    
    save_projects(projects)
    
    # Write output to file
    if chosen_project:
        with open('randomizer_output.txt', 'w') as f:
            f.write(f"Your random project for today: {chosen_project['name']}")
    else:
        with open('randomizer_output.txt', 'w') as f:
            f.write("No project was chosen or no projects available.")

if __name__ == "__main__":
    main()

