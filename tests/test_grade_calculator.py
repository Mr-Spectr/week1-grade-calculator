import unittest

from grade_calculator import score_to_grade, student_summary


class GradeCalculatorTests(unittest.TestCase):
    def test_grade_boundaries(self):
        self.assertEqual(score_to_grade(90), "A+")
        self.assertEqual(score_to_grade(80), "A")
        self.assertEqual(score_to_grade(40), "D")
        self.assertEqual(score_to_grade(39), "F")

    def test_summary_calculates_average_and_result(self):
        summary = student_summary("Asha", {"Math": 91, "Python": 79, "English": 80})
        self.assertEqual(summary["name"], "Asha")
        self.assertAlmostEqual(summary["average"], 250 / 3)
        self.assertEqual(summary["grade"], "A")
        self.assertEqual(summary["result"], "PASS")


if __name__ == "__main__":
    unittest.main()
