"""
Entry point for the pensionescol application MVP.

This script simply delegates to the pension_calculator module's
main function.  Run this script to test the MVP pension calculator.
"""

from pension_calculator import main as pension_main


if __name__ == "__main__":
    pension_main()
