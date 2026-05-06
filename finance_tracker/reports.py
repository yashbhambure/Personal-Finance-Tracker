"""
Reports module for generating expense reports and statistics.
"""

from typing import List, Dict
from collections import defaultdict
from .expense import Expense
from .utils import format_currency, get_month_year


class Reports:
    """Generates various reports and statistics from expenses."""
    
    def __init__(self, expenses: List[Expense] = None):
        """
        Initialize Reports.
        
        Args:
            expenses (List[Expense]): List of expenses to analyze
        """
        self.expenses = expenses or []
    
    def update_expenses(self, expenses: List[Expense]):
        """Update the expense list."""
        self.expenses = expenses
    
    def summary_report(self) -> Dict:
        """
        Generate a summary report of all expenses.
        
        Returns:
            Dict: Summary statistics
        """
        if not self.expenses:
            return {
                'total_expenses': 0,
                'expense_count': 0,
                'average_expense': 0,
                'highest_expense': 0,
                'lowest_expense': 0
            }
        
        amounts = [e.amount for e in self.expenses]
        return {
            'total_expenses': sum(amounts),
            'expense_count': len(amounts),
            'average_expense': sum(amounts) / len(amounts),
            'highest_expense': max(amounts),
            'lowest_expense': min(amounts)
        }
    
    def category_summary(self) -> Dict[str, Dict]:
        """
        Generate category-wise expense summary.
        
        Returns:
            Dict: Category breakdown with totals and counts
        """
        category_data = defaultdict(lambda: {'total': 0, 'count': 0})
        
        for expense in self.expenses:
            category_data[expense.category]['total'] += expense.amount
            category_data[expense.category]['count'] += 1
        
        # Sort by total amount descending
        return dict(sorted(category_data.items(), 
                          key=lambda x: x[1]['total'], reverse=True))
    
    def monthly_summary(self) -> Dict[str, Dict]:
        """
        Generate monthly expense summary.
        
        Returns:
            Dict: Monthly breakdown with totals and counts
        """
        monthly_data = defaultdict(lambda: {'total': 0, 'count': 0})
        
        for expense in self.expenses:
            month = get_month_year(expense.date)
            monthly_data[month]['total'] += expense.amount
            monthly_data[month]['count'] += 1
        
        # Sort by month
        return dict(sorted(monthly_data.items()))
    
    def top_expenses(self, n: int = 10) -> List[Expense]:
        """
        Get top N highest expenses.
        
        Args:
            n (int): Number of top expenses to return
            
        Returns:
            List[Expense]: Top N expenses sorted by amount descending
        """
        return sorted(self.expenses, key=lambda x: x.amount, reverse=True)[:n]
    
    def print_summary_report(self):
        """Print a formatted summary report."""
        summary = self.summary_report()
        
        print("\n" + "="*50)
        print("EXPENSE SUMMARY REPORT")
        print("="*50)
        print(f"Total Expenses:    {format_currency(summary['total_expenses'])}")
        print(f"Number of Entries: {summary['expense_count']}")
        print(f"Average Expense:   {format_currency(summary['average_expense'])}")
        print(f"Highest Expense:   {format_currency(summary['highest_expense'])}")
        print(f"Lowest Expense:    {format_currency(summary['lowest_expense'])}")
        print("="*50 + "\n")
    
    def print_category_summary(self):
        """Print category-wise breakdown."""
        category_data = self.category_summary()
        
        if not category_data:
            print("No expenses found.")
            return
        
        print("\n" + "="*60)
        print("CATEGORY BREAKDOWN")
        print("="*60)
        print(f"{'Category':<20} {'Total':<15} {'Count':<10}")
        print("-"*60)
        
        for category, data in category_data.items():
            print(f"{category:<20} {format_currency(data['total']):<15} {data['count']:<10}")
        
        print("="*60 + "\n")
    
    def print_monthly_summary(self):
        """Print monthly breakdown."""
        monthly_data = self.monthly_summary()
        
        if not monthly_data:
            print("No expenses found.")
            return
        
        print("\n" + "="*50)
        print("MONTHLY BREAKDOWN")
        print("="*50)
        print(f"{'Month':<15} {'Total':<20} {'Count':<10}")
        print("-"*50)
        
        for month, data in monthly_data.items():
            print(f"{month:<15} {format_currency(data['total']):<20} {data['count']:<10}")
        
        print("="*50 + "\n")
    
    def print_top_expenses(self, n: int = 5):
        """
        Print top N expenses.
        
        Args:
            n (int): Number of top expenses to show
        """
        top = self.top_expenses(n)
        
        if not top:
            print("No expenses found.")
            return
        
        print("\n" + "="*70)
        print(f"TOP {min(n, len(top))} EXPENSES")
        print("="*70)
        
        for i, expense in enumerate(top, 1):
            print(f"{i}. {expense}")
        
        print("="*70 + "\n")
    
    def print_all_expenses(self):
        """Print all expenses."""
        if not self.expenses:
            print("No expenses found.")
            return
        
        print("\n" + "="*70)
        print("ALL EXPENSES")
        print("="*70)
        
        for i, expense in enumerate(self.expenses, 1):
            print(f"{i}. {expense}")
        
        print("="*70 + "\n")
