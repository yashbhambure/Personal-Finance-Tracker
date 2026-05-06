"""
File handling module for saving and loading expenses.
"""

import json
import os
from typing import List, Dict, Any
from datetime import datetime
from .expense import Expense


class FileHandler:
    """Handles file operations for expense data."""
    
    def __init__(self, data_path: str = 'data/expenses.json'):
        """
        Initialize FileHandler.
        
        Args:
            data_path (str): Path to store expense data
        """
        self.data_path = data_path
        self.backup_path = 'data/backup/'
        self.exports_path = 'data/exports/'
        self._ensure_directories()
    
    def _ensure_directories(self):
        """Create necessary directories if they don't exist."""
        for path in [self.data_path, self.backup_path, self.exports_path]:
            directory = os.path.dirname(path) if '.' in os.path.basename(path) else path
            if directory and not os.path.exists(directory):
                os.makedirs(directory, exist_ok=True)
    
    def save_expenses(self, expenses: List[Expense]) -> bool:
        """
        Save expenses to JSON file.
        
        Args:
            expenses (List[Expense]): List of expenses to save
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            self._ensure_directories()
            data = [expense.to_dict() for expense in expenses]
            with open(self.data_path, 'w') as f:
                json.dump(data, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving expenses: {e}")
            return False
    
    def load_expenses(self) -> List[Expense]:
        """
        Load expenses from JSON file.
        
        Returns:
            List[Expense]: List of loaded expenses
        """
        try:
            if not os.path.exists(self.data_path):
                return []
            
            with open(self.data_path, 'r') as f:
                data = json.load(f)
            
            return [Expense.from_dict(expense) for expense in data]
        except Exception as e:
            print(f"Error loading expenses: {e}")
            return []
    
    def backup_expenses(self) -> bool:
        """
        Create a backup of current expenses.
        
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            if not os.path.exists(self.data_path):
                return False
            
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            backup_file = os.path.join(self.backup_path, f'expenses_backup_{timestamp}.json')
            
            with open(self.data_path, 'r') as src:
                data = src.read()
            
            with open(backup_file, 'w') as dst:
                dst.write(data)
            
            print(f"Backup created: {backup_file}")
            return True
        except Exception as e:
            print(f"Error creating backup: {e}")
            return False
    
    def export_to_csv(self, expenses: List[Expense], filename: str = None) -> bool:
        """
        Export expenses to CSV file.
        
        Args:
            expenses (List[Expense]): List of expenses to export
            filename (str): Output filename (optional)
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            if not filename:
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                filename = f'expenses_export_{timestamp}.csv'
            
            filepath = os.path.join(self.exports_path, filename)
            
            with open(filepath, 'w', newline='') as f:
                f.write('Date,Category,Amount,Description\n')
                for expense in expenses:
                    f.write(f"{expense.date},{expense.category},{expense.amount},{expense.description}\n")
            
            print(f"Expenses exported to: {filepath}")
            return True
        except Exception as e:
            print(f"Error exporting to CSV: {e}")
            return False
    
    def export_to_json(self, expenses: List[Expense], filename: str = None) -> bool:
        """
        Export expenses to JSON file.
        
        Args:
            expenses (List[Expense]): List of expenses to export
            filename (str): Output filename (optional)
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            if not filename:
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                filename = f'expenses_export_{timestamp}.json'
            
            filepath = os.path.join(self.exports_path, filename)
            data = [expense.to_dict() for expense in expenses]
            
            with open(filepath, 'w') as f:
                json.dump(data, f, indent=2)
            
            print(f"Expenses exported to: {filepath}")
            return True
        except Exception as e:
            print(f"Error exporting to JSON: {e}")
            return False
