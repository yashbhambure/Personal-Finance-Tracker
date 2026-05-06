"""
Unit tests for FileHandler module.
"""

import unittest
import os
import json
import tempfile
import shutil
from finance_tracker.expense import Expense
from finance_tracker.file_handler import FileHandler


class TestFileHandler(unittest.TestCase):
    """Test cases for FileHandler class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.test_dir = tempfile.mkdtemp()
        self.test_data_path = os.path.join(self.test_dir, 'test_expenses.json')
        self.file_handler = FileHandler(self.test_data_path)
        self.file_handler.backup_path = os.path.join(self.test_dir, 'backup/')
        self.file_handler.exports_path = os.path.join(self.test_dir, 'exports/')
    
    def tearDown(self):
        """Clean up after tests."""
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
    
    def test_save_and_load_expenses(self):
        """Test saving and loading expenses."""
        expenses = [
            Expense(50.00, "Food", "Lunch"),
            Expense(100.00, "Transport", "Gas")
        ]
        
        self.assertTrue(self.file_handler.save_expenses(expenses))
        loaded = self.file_handler.load_expenses()
        
        self.assertEqual(len(loaded), 2)
        self.assertEqual(loaded[0].amount, 50.00)
        self.assertEqual(loaded[1].category, "Transport")
    
    def test_load_empty_file(self):
        """Test loading when file doesn't exist."""
        loaded = self.file_handler.load_expenses()
        self.assertEqual(loaded, [])
    
    def test_backup_expenses(self):
        """Test creating backup."""
        expenses = [Expense(50.00, "Food", "Lunch")]
        self.file_handler.save_expenses(expenses)
        
        self.assertTrue(self.file_handler.backup_expenses())
        backup_files = os.listdir(self.file_handler.backup_path)
        self.assertGreater(len(backup_files), 0)
    
    def test_export_to_csv(self):
        """Test exporting to CSV."""
        expenses = [
            Expense(50.00, "Food", "Lunch", "2024-01-15"),
            Expense(100.00, "Transport", "Gas", "2024-01-16")
        ]
        
        self.assertTrue(self.file_handler.export_to_csv(expenses, 'test_export.csv'))
        
        export_path = os.path.join(self.file_handler.exports_path, 'test_export.csv')
        self.assertTrue(os.path.exists(export_path))
        
        with open(export_path, 'r') as f:
            content = f.read()
            self.assertIn('Food', content)
            self.assertIn('50.00', content)
    
    def test_export_to_json(self):
        """Test exporting to JSON."""
        expenses = [Expense(50.00, "Food", "Lunch", "2024-01-15")]
        
        self.assertTrue(self.file_handler.export_to_json(expenses, 'test_export.json'))
        
        export_path = os.path.join(self.file_handler.exports_path, 'test_export.json')
        self.assertTrue(os.path.exists(export_path))
        
        with open(export_path, 'r') as f:
            data = json.load(f)
            self.assertEqual(len(data), 1)
            self.assertEqual(data[0]['amount'], 50.00)


if __name__ == '__main__':
    unittest.main()
