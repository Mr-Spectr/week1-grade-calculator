# Week 1 CLI Grade Calculator

A simple Python command-line program to store student marks and calculate averages, grades, and pass/fail results.

## Features

- Add student marks for multiple subjects
- View all student results
- Search or remove a student
- Export the report to a CSV file

## Run

```bash
python grade_calculator.py
```

## Example output

```text
==========================================
       WEEK 1 - GRADE CALCULATOR
==========================================
1. Add or update a student
2. View class report
3. Find a student
4. Remove a student
5. Export report to CSV
6. Exit

Choose an option (1-6): 2

========================================================================
Student             Subjects                       Average   Grade  Result
------------------------------------------------------------------------
Ravi                Python: 95, Math: 82            88.50%       A    PASS
========================================================================
```

## Concepts used

- Variables, data types, and operators
- Dictionaries and loops
- Functions and return values
- `if` conditions
- File handling with CSV
- Basic exception handling

## Test

```bash
python -m unittest discover -s tests -v
```
