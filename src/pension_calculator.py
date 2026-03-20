"""Simple pension savings calculator for the pensionescol MVP.

This module provides a function to estimate pension savings based on a
contribution rate, an annual salary and the number of years of
contributions.  It deliberately keeps the calculation very simple and does
not account for investment returns, taxes, inflation or other factors.  It
is intended purely as a starting point for further development.
"""

from __future__ import annotations


def calculate_pension(contribution_rate: float, salary: float, years: int) -> float:
    """Estimate pension savings at retirement.

    The calculation multiplies the annual salary by the contribution rate and
    the number of years.  For example, a contribution rate of 0.10 (10 %),
    a salary of 50 000 and 30 years of contributions would yield:
    ``50_000 * 0.10 * 30 = 150_000``.

    Parameters
    ----------
    contribution_rate : float
        The fraction of the salary that is contributed to the pension each year
        (e.g. 0.10 for 10 %).
    salary : float
        The annual salary in the same currency as the desired output.
    years : int
        The number of years contributions are made.

    Returns
    -------
    float
        The estimated total contributions at retirement.
    """
    if not 0 <= contribution_rate <= 1:
        raise ValueError("Contribution rate must be between 0 and 1 (inclusive)")
    if salary < 0:
        raise ValueError("Salary must be non-negative")
    if years < 0:
        raise ValueError("Years must be non-negative")
    return salary * contribution_rate * years


def main() -> None:
    """Run a demonstration of the pension calculator."""
    print("This is a simple pension calculator")
    contribution_rate = 0.10  # 10 %
    salary = 50_000.0         # annual salary
    years = 30                # number of years contributing
    estimated = calculate_pension(contribution_rate, salary, years)
    print(f"Estimated pension savings: ${estimated:,.2f}")


if __name__ == "__main__":
    main()
