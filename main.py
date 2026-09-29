import random


def main():
    """Ask for a name and print a random friendly personalized message."""
    sprueche = [
        "Du machst die Welt ein kleines bisschen heller.",
        "Schön, dass es dich gibt!",
        "Du kannst heute etwas Großartiges erreichen.",
        "Mit dir wird jeder Tag ein bisschen besser.",
        "Du bist einzigartig und wunderbar!",
    ]

    while True:
        name = input("Wie heißt du? ").strip()
        if name:
            break
        print("Bitte gib einen Namen ein.")

    print(f"Hallo, {name}! {random.choice(sprueche)}")


if __name__ == "__main__":
    main()
