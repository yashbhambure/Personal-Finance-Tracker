"""
Expense Manager module for managing expense operations.
"""

from typing import List, Optional
from .expense import Expense
from .file_handler import FileHandler
from .utils import validate_amount, validate_date, validate_category, validate_description


class ExpenseManager:
    """Manages all expense-related operations."""
    
    def __init__(self, file_handler: FileHandler = None):
        """
        Initialize ExpenseManager.
        
        Args:
            file_handler (FileHandler): File handler instance
        """
        self.file_handler = file_handler or FileHandler()
        self.expenses: List[Expense] = self.file_handler.load_expenses()
    
    def add_expense(self, amount: float, category: str, description: str, date: str = None) -> bool:
        """
        Add a new expense.
        
        Args:
            amount (float): Amount spent
            category (str): Category of expense
            description (str): Description of expense
            date (str): Date of expense (optional)
            
        Returns:
            bool: True if successful
        """
        try:
            amount = validate_amount(amount)
            category = validate_category(category)
            description = validate_description(description)
            
            if date:
                date = validate_date(date)
            
            expense = Expense(amount, category, description, date)
            self.expenses.append(expense)
            self.file_handler.save_expenses(self.expenses)
            return True
        except ValueError as e:
            print(f"Error adding expense: {e}")
            return False
    
    def delete_expense(self, index: int) -> bool:
        """
        Delete an expense by index.
        
        Args:
            index (int): Index of expense to delete
            
        Returns:
            bool: True if successful
        """
        try:
            if 0 <= index < len(self.expenses):
                del self.expenses[index]
                self.file_handler.save_expenses(self.expenses)
                return True
            else:
                print("Invalid expense index")
                return False
        except Exception as e:
            print(f"Error deleting expense: {e}")
            return False
    
    def update_expense(self, index: int, amount: float = None, category: str = None, 
                      description: str = None, date: str = None) -> bool:
        """
        Update an existing expense.
        
        Args:
            index (int): Index of expense to update
            amount (float): New amount (optional)
            category (str): New category (optional)
            description (str): New description (optional)
            date (str): New date (optional)
            
        Returns:
            bool: True if successful
        """
        try:
            if not (0 <= index < len(self.expenses)):
                print("Invalid expense index")
                return False
            
            expense = self.expenses[index]
            
            if amount is not None:
                expense.amount = validate_amount(amount)
            if category is not None:
                expense.category = validate_category(category)
            if description is not None:
                expense.description = validate_description(description)
            if date is not None:
                expense.date = validate_date(date)
            
            self.file_handler.save_expenses(self.expenses)
            return True
        except ValueError as e:
            print(f"Error updating expense: {e}")
            return False
    
    def get_all_expenses(self) -> List[Expense]:
        """Get all expenses."""
        return self.expenses.copy()
    
    def get_expenses_by_category(self, category: str) -> List[Expense]:
        """
        Get expenses filtered by category.
        
        Args:
            category (str): Category to filter by
            
        Returns:
            List[Expense]: Filtered expenses
        """
        return [e for e in self.expenses if e.category.lower() == category.lower()]
    
    def get_expenses_by_date(self, date: str) -> List[Expense]:
        """
        Get expenses for a specific date.
        
        Args:
            date (str): Date in format YYYY-MM-DD
            
        Returns:
            List[Expense]: Expenses on that date
        """
        return [e for e in self.expenses if e.date == date]
    
    def get_expenses_by_date_range(self, start_date: str, end_date: str) -> List[Expense]:
        """
        Get expenses within a date range.
        
        Args:
            start_date (str): Start date in format YYYY-MM-DD
            end_date (str): End date in format YYYY-MM-DD
            
        Returns:
            List[Expense]: Expenses within the range
        """
        return [e for e in self.expenses if start_date <= e.date <= end_date]
    
    def search_expenses(self, keyword: str) -> List[Expense]:
        """
        Search expenses by keyword in description.
        
        Args:
            keyword (str): Keyword to search for
            
        Returns:
            List[Expense]: Matching expenses
        """
        return [e for e in self.expenses if keyword.lower() in e.description.lower()]
    
    def clear_all_expenses(self) -> bool:
        """
        Clear all expenses (with confirmation).
        
        Returns:
            bool: True if cleared
        """
        self.expenses = []
        self.file_handler.save_expenses(self.expenses)
        return True
    
    def get_total_expenses(self, expenses: List[Expense] = None) -> float:
        """
        Get total of all expenses.
        
        Args:
            expenses (List[Expense]): List to sum (uses all if None)
            
        Returns:
            float: Total amount
        """
        if expenses is None:
            expenses = self.expenses
        return sum(e.amount for e in expenses)
    
    def get_expense_count(self) -> int:
        """Get count of all expenses."""
        return len(self.expenses)
