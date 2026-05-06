"""
Expense module containing the Expense class.
"""

from datetime import datetime
from typing import Dict, Any


class Expense:
    """Represents a single expense entry."""
    
    def __init__(self, amount: float, category: str, description: str, date: str = None):
        """
        Initialize an Expense object.
        
        Args:
            amount (float): The amount spent
            category (str): Category of the expense
            description (str): Brief description of the expense
            date (str): Date of the expense in format 'YYYY-MM-DD'
        """
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date or datetime.now().strftime('%Y-%m-%d')
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert expense to dictionary."""
        return {
            'amount': self.amount,
            'category': self.category,
            'description': self.description,
            'date': self.date
        }
    
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'Expense':
        """Create an Expense object from dictionary."""
        return Expense(
            amount=data['amount'],
            category=data['category'],
            description=data['description'],
            date=data.get('date', datetime.now().strftime('%Y-%m-%d'))
        )
    
    def __str__(self) -> str:
        """String representation of the expense."""
        return f"{self.date} | {self.category:<12} | ${self.amount:>8.2f} | {self.description}"
    
    def __repr__(self) -> str:
        """Developer-friendly representation."""
        return f"Expense(amount={self.amount}, category='{self.category}', description='{self.description}', date='{self.date}')"
