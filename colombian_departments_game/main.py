import turtle as t
import pandas as pd


def set_up_screen(img: str) -> t.Screen:
    """Set up the turtle screen and shape."""
    screen = t.Screen()
    screen.title("Colombian Departments Game")
    screen.addshape(img)
    t.shape(img)
    return screen


def read_data(file_path: str) -> tuple:
    """Read data from a CSV file and return a list of departments."""
    data = pd.read_csv(file_path)
    departments = data["Departments"].tolist()
    return data, departments


def ask_for_department(data: pd.DataFrame, guessed_dep: list) -> str:
    """Ask the user for another department name and return it."""
    answer_dep = t.textinput(title=f"{len(guessed_dep)}/32 departments guessed",
                             prompt="What's another department name?")
    title_guess = answer_dep.title()
    if title_guess in data["Departments"].tolist() and title_guess not in guessed_dep:
        guessed_dep.append(title_guess)
        return title_guess
    if title_guess == "Exit":
        return "Exit"


def draw_department(department_data: pd.DataFrame) -> None:
    """Draw the department on the turtle screen."""
    billie = t.Turtle()
    billie.hideturtle()
    billie.penup()
    billie.goto(int(department_data.x), int(department_data.y))
    billie.write(department_data["Departments"].item())


def generate_missing_departments_file(data: pd.DataFrame, guessed_dep: list) -> None:
    """Create a CSV file with the names of the departments that were not guessed."""
    missing_dep = []
    for dep in data["Departments"]:
        if dep not in guessed_dep:
            missing_dep.append(dep)
    new_data = pd.DataFrame(missing_dep)
    new_data.to_csv("departments_to_learn.csv", index=False)


def main() -> None:
    # Set up the screen
    img = "mapa_colombia.gif"
    screen = set_up_screen(img)

    # Extract data from CSV file
    data, departments = read_data("colombian_departments.csv")

    # Interaction with user
    guessed_dep = []
    while len(guessed_dep) < 32:
        answer = ask_for_department(data, guessed_dep)
        if answer:
            if answer == "Exit":
                generate_missing_departments_file(data, guessed_dep)
                break
            dep_data = data[data["Departments"] == answer]
            draw_department(dep_data)


if __name__ == "__main__":
    main()
