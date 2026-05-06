"""
Utility functions for the finance tracker.
"""

from datetime import datetime
from typing import Union
import re


def validate_amount(amount: Union[str, float]) -> float:
    """
    Validate and convert amount to float.
    
    Args:
        amount: The amount to validate
        
    Returns:
        float: The validated amount
        
    Raises:
        ValueError: If amount is invalid
    """
    try:
        amount = float(amount)
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        return round(amount, 2)
    except ValueError:
        raise ValueError(f"Invalid amount: {amount}. Please enter a valid number.")


def validate_date(date_str: str) -> str:
    """
    Validate date format (YYYY-MM-DD).
    
    Args:
        date_str: Date string to validate
        
    Returns:
        str: The validated date string
        
    Raises:
        ValueError: If date format is invalid
    """
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return date_str
    except ValueError:
        raise ValueError(f"Invalid date format: {date_str}. Use YYYY-MM-DD")


def format_currency(amount: float) -> str:
    """
    Format amount as currency string.
    
    Args:
        amount: The amount to format
        
    Returns:
        str: Formatted currency string
    """
    return f"${amount:,.2f}"


def validate_category(category: str) -> str:
    """
    Validate and clean category string.
    
    Args:
        category: Category to validate
        
    Returns:
        str: Cleaned category string
        
    Raises:
        ValueError: If category is empty
    """
    category = category.strip()
    if not category:
        raise ValueError("Category cannot be empty")
    if len(category) > 50:
        raise ValueError("Category name too long (max 50 characters)")
    return category


def validate_description(description: str) -> str:
    """
    Validate and clean description string.
    
    Args:
        description: Description to validate
        
    Returns:
        str: Cleaned description string
    """
    description = description.strip()
    if len(description) > 200:
        raise ValueError("Description too long (max 200 characters)")
    return description or "No description"


def get_current_date() -> str:
    """Get current date in YYYY-MM-DD format."""
    return datetime.now().strftime('%Y-%m-%d')


def get_month_year(date_str: str) -> str:
    """Get month-year from date string."""
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    return date_obj.strftime('%Y-%m')
