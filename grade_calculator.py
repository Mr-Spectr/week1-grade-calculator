"""A menu-driven grade calculator for the Week 1 Python mini-project."""

import csv
from pathlib import Path


GRADE_SCALE = {
    "A+": (90, 100),
    "A": (80, 89),
    "B+": (70, 79),
    "B": (60, 69),
    "C": (50, 59),
    "D": (40, 49),
    "F": (0, 39),
}
PASS_MARK = 40


def score_to_grade(score):
    """Return the letter grade for a score from 0 to 100."""
    for grade, (minimum, maximum) in GRADE_SCALE.items():
        if minimum <= score <= maximum:
            return grade
    raise ValueError("Score must be between 0 and 100.")


def get_score(subject):
    """Ask for one valid numeric score."""
    while True:
        try:
            score = float(input(f"  Score in {subject} (0-100): ").strip())
            if 0 <= score <= 100:
                return score
            print("  Please enter a score from 0 to 100.")
        except ValueError:
            print("  Please enter a number, such as 78 or 84.5.")


def add_student(students):
    """Add or replace a student's subject scores."""
    name = input("Student name: ").strip().title()
    if not name:
        print("A name cannot be empty.")
        return

    subjects = {}
    print("Enter subjects one at a time. Press Enter with no subject to finish.")
    while True:
        subject = input("Subject: ").strip().title()
        if not subject:
            break
        subjects[subject] = get_score(subject)

    if subjects:
        students[name] = subjects
        print(f"Saved {name}'s {len(subjects)} subject(s).")
    else:
        print("No subjects entered; nothing was saved.")


def student_summary(name, subjects):
    """Build a dictionary containing calculated results for one student."""
    average = sum(subjects.values()) / len(subjects)
    return {
        "name": name,
        "average": average,
        "grade": score_to_grade(average),
        "result": "PASS" if average >= PASS_MARK else "FAIL",
    }


def display_report(students):
    """Show scores and calculated results in a tidy table."""
    if not students:
        print("No students have been added yet.")
        return

    print("\n" + "=" * 72)
    print(f"{'Student':<20}{'Subjects':<28}{'Average':>10}{'Grade':>8}{'Result':>8}")
    print("-" * 72)
    for name, subjects in students.items():
        summary = student_summary(name, subjects)
        subject_text = ", ".join(f"{subject}: {score:g}" for subject, score in subjects.items())
        print(
            f"{name:<20}{subject_text:<28}{summary['average']:>9.2f}%"
            f"{summary['grade']:>8}{summary['result']:>8}"
        )
    print("=" * 72)


def find_student(students):
    """Show an individual student's detailed report."""
    name = input("Student name to find: ").strip().title()
    subjects = students.get(name)
    if not subjects:
        print("Student not found.")
        return

    summary = student_summary(name, subjects)
    print(f"\n{name}'s report")
    print("-" * (len(name) + 9))
    for subject, score in subjects.items():
        print(f"{subject:<20} {score:>6.2f}  ({score_to_grade(score)})")
    print(f"Average: {summary['average']:.2f}% | Grade: {summary['grade']} | {summary['result']}")


def remove_student(students):
    """Remove a student after confirmation."""
    name = input("Student name to remove: ").strip().title()
    if name not in students:
        print("Student not found.")
        return
    if input(f"Remove {name}? (y/n): ").strip().lower() == "y":
        del students[name]
        print(f"Removed {name}.")
    else:
        print("Removal cancelled.")


def export_csv(students, filename="grade_report.csv"):
    """Export each student summary to a CSV file."""
    if not students:
        print("There is no data to export.")
        return
    path = Path(filename)
    try:
        with path.open("w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Student", "Subjects", "Average", "Grade", "Result"])
            for name, subjects in students.items():
                summary = student_summary(name, subjects)
                subject_text = "; ".join(f"{subject}: {score:g}" for subject, score in subjects.items())
                writer.writerow([name, subject_text, f"{summary['average']:.2f}", summary["grade"], summary["result"]])
        print(f"Report exported to {path.resolve()}")
    except OSError as error:
        print(f"Could not write the CSV file: {error}")


def show_menu():
    # Use ASCII here so the app works in the default Windows console encoding.
    print("\n" + "=" * 42)
    print("       WEEK 1 - GRADE CALCULATOR")
    print("=" * 42)
    print("1. Add or update a student")
    print("2. View class report")
    print("3. Find a student")
    print("4. Remove a student")
    print("5. Export report to CSV")
    print("6. Exit")


def main():
    """Run the interactive command-line application."""
    students = {}
    actions = {
        "1": lambda: add_student(students),
        "2": lambda: display_report(students),
        "3": lambda: find_student(students),
        "4": lambda: remove_student(students),
        "5": lambda: export_csv(students),
    }
    print("Welcome! Track marks, grades, and pass/fail results in one place.")

    while True:
        show_menu()
        choice = input("Choose an option (1-6): ").strip()
        if choice == "6":
            print("Goodbye - keep learning Python!")
            break
        action = actions.get(choice)
        if action:
            action()
        else:
            print("Invalid choice. Please select a number from 1 to 6.")


if __name__ == "__main__":
    main()
