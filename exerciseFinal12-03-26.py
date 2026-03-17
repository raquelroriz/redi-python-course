# 6_FinalExercise 12/03/2026

while True:
    text = input("Enter a string: ")

    if text == "":
        print("Thanks for playing!")
        break

    print("1)", text.capitalize())
    print("2)", text.lower())
    print("3)", text.title())
    print("4)", text.upper())