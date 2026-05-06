"""
Unit tests for Expense module.
"""

import unittest
from datetime import datetime
from finance_tracker.expense import Expense


class TestExpense(unittest.TestCase):
    """Test cases for Expense class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.expense = Expense(50.00, "Food", "Lunch at restaurant", "2024-01-15")
    
    def test_expense_creation(self):
        """Test creating an expense."""
        self.assertEqual(self.expense.amount, 50.00)
        self.assertEqual(self.expense.category, "Food")
        self.assertEqual(self.expense.description, "Lunch at restaurant")
        self.assertEqual(self.expense.date, "2024-01-15")
    
    def test_expense_to_dict(self):
        """Test converting expense to dictionary."""
        expense_dict = self.expense.to_dict()
        self.assertEqual(expense_dict['amount'], 50.00)
        self.assertEqual(expense_dict['category'], "Food")
        self.assertEqual(expense_dict['description'], "Lunch at restaurant")
        self.assertEqual(expense_dict['date'], "2024-01-15")
    
    def test_expense_from_dict(self):
        """Test creating expense from dictionary."""
        data = {
            'amount': 100.00,
            'category': 'Transport',
            'description': 'Gas',
            'date': '2024-01-16'
        }
        expense = Expense.from_dict(data)
        self.assertEqual(expense.amount, 100.00)
        self.assertEqual(expense.category, 'Transport')
    
    def test_expense_string_representation(self):
        """Test string representation."""
        expected = "2024-01-15 | Food         |    50.00 | Lunch at restaurant"
        self.assertEqual(str(self.expense), expected)
    
    def test_expense_default_date(self):
        """Test default date is today."""
        expense = Expense(25.00, "Coffee", "Morning coffee")
        today = datetime.now().strftime('%Y-%m-%d')
        self.assertEqual(expense.date, today)
    
    def test_expense_with_zero_amount(self):
        """Test expense with zero amount."""
        expense = Expense(0.00, "Test", "Test")
        self.assertEqual(expense.amount, 0.00)


if __name__ == '__main__':
    unittest.main()
