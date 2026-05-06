"""
Unit tests for Reports module.
"""

import unittest
from finance_tracker.expense import Expense
from finance_tracker.reports import Reports


class TestReports(unittest.TestCase):
    """Test cases for Reports class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.expenses = [
            Expense(50.00, "Food", "Lunch", "2024-01-15"),
            Expense(100.00, "Transport", "Gas", "2024-01-15"),
            Expense(30.00, "Food", "Dinner", "2024-01-16"),
            Expense(200.00, "Entertainment", "Movie", "2024-02-10"),
        ]
        self.reports = Reports(self.expenses)
    
    def test_summary_report(self):
        """Test summary report generation."""
        summary = self.reports.summary_report()
        
        self.assertEqual(summary['total_expenses'], 380.00)
        self.assertEqual(summary['expense_count'], 4)
        self.assertEqual(summary['highest_expense'], 200.00)
        self.assertEqual(summary['lowest_expense'], 30.00)
    
    def test_category_summary(self):
        """Test category summary."""
        category_data = self.reports.category_summary()
        
        self.assertIn('Food', category_data)
        self.assertIn('Transport', category_data)
        self.assertEqual(category_data['Food']['total'], 80.00)
        self.assertEqual(category_data['Food']['count'], 2)
    
    def test_monthly_summary(self):
        """Test monthly summary."""
        monthly_data = self.reports.monthly_summary()
        
        self.assertIn('2024-01', monthly_data)
        self.assertIn('2024-02', monthly_data)
        self.assertEqual(monthly_data['2024-01']['total'], 180.00)
        self.assertEqual(monthly_data['2024-02']['total'], 200.00)
    
    def test_top_expenses(self):
        """Test getting top expenses."""
        top = self.reports.top_expenses(2)
        
        self.assertEqual(len(top), 2)
        self.assertEqual(top[0].amount, 200.00)
        self.assertEqual(top[1].amount, 100.00)
    
    def test_empty_expenses(self):
        """Test reports with empty expenses."""
        reports = Reports([])
        summary = reports.summary_report()
        
        self.assertEqual(summary['total_expenses'], 0)
        self.assertEqual(summary['expense_count'], 0)
    
    def test_category_summary_sorting(self):
        """Test category summary is sorted by total descending."""
        category_data = self.reports.category_summary()
        categories = list(category_data.keys())
        
        # First category should have highest total
        self.assertEqual(categories[0], 'Transport')
        self.assertEqual(category_data['Transport']['total'], 100.00)


if __name__ == '__main__':
    unittest.main()
