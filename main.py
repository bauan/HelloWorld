def main():
    """Ask for a name and print a friendly personalized message."""
    while True:
        name = input("Wie heißt du? ").strip()
        if name:
            break
        print("Bitte gib einen Namen ein.")

    print(f"Hallo, {name}! Du machst die Welt ein kleines bisschen heller.")


if __name__ == "__main__":
    main()
