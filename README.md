# 🎓 Week 1 CLI Grade Calculator

> A friendly, menu-driven Python program that records student marks, calculates averages and letter grades, and exports a class report to CSV.

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Interface](https://img.shields.io/badge/Interface-Command%20Line-6f42c1)
![Status](https://img.shields.io/badge/Status-Week%201%20Mini--Project-2ea44f)

## ✨ What it can do

| Feature | What happens |
| --- | --- |
| ➕ Add students | Store one or more subjects and marks for each student. |
| 🧮 Calculate results | Computes average, letter grade, and pass/fail status automatically. |
| 🔎 Find a student | Displays a detailed report for one student. |
| 🗑️ Remove students | Deletes a student after a confirmation prompt. |
| 📄 Export CSV | Saves a shareable `grade_report.csv` class report. |
| 🛡️ Validate input | Handles invalid menu entries, text marks, and out-of-range scores safely. |

## 🚀 Run it

**Prerequisite:** Python 3.10 or later.

```bash
git clone <your-repository-url>
cd week1-grade-calculator
python grade_calculator.py
```

No third-party packages are required.

## 🖥️ A quick tour

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
Choose an option (1-6):
```

### Grade scale

| Score | Grade | Result |
| ---: | :---: | :---: |
| 90–100 | A+ | PASS |
| 80–89 | A | PASS |
| 70–79 | B+ | PASS |
| 60–69 | B | PASS |
| 50–59 | C | PASS |
| 40–49 | D | PASS |
| 0–39 | F | FAIL |

## 🧠 Week 1 concepts demonstrated

- **Data types, variables, arithmetic, and type conversion:** numeric marks are converted from user input, totalled, and averaged.
- **Dictionaries:** student names map to their subject-and-score dictionaries; the grade scale is also a dictionary.
- **Control flow:** `if`/`elif` style decisions and `while`/`for` loops drive validation and the menu.
- **Functions:** focused functions use parameters, return values, and a default filename for CSV export.
- **String operations:** input is cleaned with `strip()` and formatted for readable reports.
- **File I/O:** the `csv` module writes the class report to a text-based CSV file.
- **Exception handling:** `try`/`except` handles non-numeric scores and file-writing errors.

## 🧪 Test the core logic

```bash
python -m unittest discover -s tests -v
```

## 📁 Project structure

```text
week1-grade-calculator/
├── grade_calculator.py        # Interactive application
├── tests/
│   └── test_grade_calculator.py
├── .gitignore
└── README.md
```

## 👤 Submission checklist

- [x] Mini-project code is ready to upload to GitHub.
- [x] A README explains setup, features, and course concepts.
- [ ] Add **Dr. Lakshmana** as a repository collaborator using `lakshmana.b@nmit.ac.in`.
- [ ] Confirm the invitation has been sent and the repository is accessible.

---

Made for the **Week 1 Beginner Python** mini-project.
