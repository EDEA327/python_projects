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


def draw_department(department_data: pd.DataFrame) -> None:
    """Draw the department on the turtle screen."""
    billie = t.Turtle()
    billie.hideturtle()
    billie.penup()
    billie.goto(int(department_data.x), int(department_data.y))
    billie.write(department_data["Departments"].item())


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
            dep_data = data[data["Departments"] == answer]
            draw_department(dep_data)

    # Keep window open
    screen.mainloop()


if __name__ == "__main__":
    main()
