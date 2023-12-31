
def main():

    # for each name in invited_names.txt
    with open("Input/Names/invited_names.txt") as f:
        names = [name.strip() for name in f.readlines()]
    with open("Input/Letters/starting_letter.txt") as f:
        starting_letter = f.read()
    # Replace the [name] placeholder with the name
    for name in names:
        new_letter = starting_letter.replace("[name]", name)
        # Save the letters in the folder "ReadyToSend".
        with open(f"Output/ReadyToSend/letter_for_{name}.txt", "w") as f:
            f.write(new_letter)


if __name__ == '__main__':
    main()

