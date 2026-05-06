"""
Entry point for running the Personal Finance Tracker application.
"""

from finance_tracker.main import FinanceTracker


def main():
    """Run the Finance Tracker application."""
    tracker = FinanceTracker()
    tracker.run()


if __name__ == '__main__':
    main()
