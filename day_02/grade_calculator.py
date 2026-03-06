while True:
    # Ask for student name
    name = input("Enter the student's name (or type 'exit' to quit): ")

    # Check if user wants to exit
    if name.lower() == "exit":
        print("Program ended.")
        break

    # Ask for marks
    maths = float(input("Enter Maths marks: "))
    science = float(input("Enter Science marks: "))
    english = float(input("Enter English marks: "))

    # Calculate average
    average = (maths + science + english) / 3

    # Determine grade
    if average >= 75:
        grade = "A"
    elif average >= 60:
        grade = "B"
    elif average >= 40:
        grade = "C"
    else:
        grade = "Fail"

    # Print result with formatting
    print("------------------------------")
    print(f"Name    : {name}")
    print(f"Average : {average:.2f}")
    print(f"Grade   : {grade}")
    print("------------------------------\n")