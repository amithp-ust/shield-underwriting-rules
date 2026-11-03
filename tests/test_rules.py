import unittest

from src.underwriting.rules import evaluate


class RulesTests(unittest.TestCase):
    def test_eligible_premium(self):
        self.assertEqual(evaluate(35, 100000), {
            "eligible": True, "premium_cents": 5000,
        })

    def test_age_boundaries(self):
        for age in (18, 85):
            self.assertTrue(evaluate(age, 100000)["eligible"])
        for age in (17, 86):
            self.assertFalse(evaluate(age, 100000)["eligible"])

    def test_invalid_inputs(self):
        for age, coverage in ((-1, 100), (121, 100), (True, 100),
                              (35, 0), (35, 1.5), (35, True)):
            with self.subTest(age=age, coverage=coverage):
                with self.assertRaises(ValueError):
                    evaluate(age, coverage)
