"""Synthetic eligibility and annual premium rules (CM-UW-RULES)."""


def evaluate(applicant_age: int, coverage_cents: int) -> dict:
    if type(applicant_age) is not int or not 0 <= applicant_age <= 120:
        raise ValueError("applicant_age must be an integer between 0 and 120")
    if type(coverage_cents) is not int or coverage_cents <= 0:
        raise ValueError("coverage_cents must be a positive integer")
    eligible = 18 <= applicant_age <= 85
    premium_cents = max(1, coverage_cents // 20) if eligible else 0
    return {"eligible": eligible, "premium_cents": premium_cents}
