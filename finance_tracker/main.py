"""
Main module providing CLI interface for the Finance Tracker.
"""

from .expense_manager import ExpenseManager
from .file_handler import FileHandler
from .reports import Reports
from .utils import get_current_date


class FinanceTracker:
    """Main Finance Tracker application."""
    
    def __init__(self):
        """Initialize the Finance Tracker."""
        self.file_handler = FileHandler()
        self.manager = ExpenseManager(self.file_handler)
        self.reports = Reports(self.manager.get_all_expenses())
    
    def run(self):
        """Run the main application loop."""
        self._print_welcome()
        
        while True:
            self._print_menu()
            choice = input("\nEnter your choice (1-11): ").strip()
            
            if choice == '1':
                self._add_expense()
            elif choice == '2':
                self._view_all_expenses()
            elif choice == '3':
                self._view_expenses_by_category()
            elif choice == '4':
                self._view_expenses_by_date()
            elif choice == '5':
                self._delete_expense()
            elif choice == '6':
                self._update_expense()
            elif choice == '7':
                self._search_expenses()
            elif choice == '8':
                self._view_reports()
            elif choice == '9':
                self._backup_expenses()
            elif choice == '10':
                self._export_expenses()
            elif choice == '11':
                self._exit_application()
            else:
                print("\nInvalid choice. Please try again.")
    
    def _print_welcome(self):
        """Print welcome message."""
        print("\n" + "="*60)
        print("WELCOME TO PERSONAL FINANCE TRACKER")
        print("="*60)
        print("Track your expenses and manage your finances efficiently!")
        print("="*60 + "\n")
    
    def _print_menu(self):
        """Print main menu."""
        print("\n" + "-"*60)
        print("MAIN MENU")
        print("-"*60)
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Expenses by Category")
        print("4. View Expenses by Date")
        print("5. Delete Expense")
        print("6. Update Expense")
        print("7. Search Expenses")
        print("8. View Reports")
        print("9. Backup Expenses")
        print("10. Export Expenses")
        print("11. Exit")
        print("-"*60)
    
    def _add_expense(self):
        """Add a new expense."""
        print("\n--- ADD EXPENSE ---")
        try:
            amount = float(input("Enter amount: $"))
            category = input("Enter category: ")
            description = input("Enter description: ")
            date = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
            
            if self.manager.add_expense(amount, category, description, date if date else None):
                print("✓ Expense added successfully!")
                self.reports.update_expenses(self.manager.get_all_expenses())
            else:
                print("✗ Failed to add expense.")
        except ValueError:
            print("✗ Invalid input. Please check your entries.")
    
    def _view_all_expenses(self):
        """View all expenses."""
        expenses = self.manager.get_all_expenses()
        self.reports.update_expenses(expenses)
        self.reports.print_all_expenses()
    
    def _view_expenses_by_category(self):
        """View expenses filtered by category."""
        print("\n--- VIEW BY CATEGORY ---")
        category = input("Enter category: ").strip()
        
        expenses = self.manager.get_expenses_by_category(category)
        self.reports.update_expenses(expenses)
        
        if expenses:
            self.reports.print_all_expenses()
        else:
            print(f"No expenses found for category: {category}")
    
    def _view_expenses_by_date(self):
        """View expenses by date."""
        print("\n--- VIEW BY DATE ---")
        print("1. View expenses on a specific date")
        print("2. View expenses within a date range")
        choice = input("Choose option (1 or 2): ").strip()
        
        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ").strip()
            expenses = self.manager.get_expenses_by_date(date)
            if expenses:
                self.reports.update_expenses(expenses)
                self.reports.print_all_expenses()
            else:
                print(f"No expenses found for date: {date}")
        elif choice == '2':
            start_date = input("Enter start date (YYYY-MM-DD): ").strip()
            end_date = input("Enter end date (YYYY-MM-DD): ").strip()
            expenses = self.manager.get_expenses_by_date_range(start_date, end_date)
            if expenses:
                self.reports.update_expenses(expenses)
                self.reports.print_all_expenses()
            else:
                print(f"No expenses found between {start_date} and {end_date}")
    
    def _delete_expense(self):
        """Delete an expense."""
        print("\n--- DELETE EXPENSE ---")
        self._view_all_expenses()
        
        try:
            index = int(input("Enter expense number to delete: ")) - 1
            if self.manager.delete_expense(index):
                print("✓ Expense deleted successfully!")
                self.reports.update_expenses(self.manager.get_all_expenses())
            else:
                print("✗ Failed to delete expense.")
        except ValueError:
            print("✗ Invalid input. Please enter a valid number.")
    
    def _update_expense(self):
        """Update an existing expense."""
        print("\n--- UPDATE EXPENSE ---")
        self._view_all_expenses()
        
        try:
            index = int(input("Enter expense number to update: ")) - 1
            
            print("\nLeave blank to keep current value:")
            amount = input("New amount: ").strip()
            category = input("New category: ").strip()
            description = input("New description: ").strip()
            date = input("New date (YYYY-MM-DD): ").strip()
            
            amount = float(amount) if amount else None
            category = category if category else None
            description = description if description else None
            date = date if date else None
            
            if self.manager.update_expense(index, amount, category, description, date):
                print("✓ Expense updated successfully!")
                self.reports.update_expenses(self.manager.get_all_expenses())
            else:
                print("✗ Failed to update expense.")
        except ValueError:
            print("✗ Invalid input. Please check your entries.")
    
    def _search_expenses(self):
        """Search expenses by keyword."""
        print("\n--- SEARCH EXPENSES ---")
        keyword = input("Enter search keyword: ").strip()
        
        expenses = self.manager.search_expenses(keyword)
        self.reports.update_expenses(expenses)
        
        if expenses:
            self.reports.print_all_expenses()
        else:
            print(f"No expenses found matching: {keyword}")
    
    def _view_reports(self):
        """View various reports."""
        print("\n--- REPORTS ---")
        print("1. Summary Report")
        print("2. Category Breakdown")
        print("3. Monthly Breakdown")
        print("4. Top Expenses")
        choice = input("Choose report (1-4): ").strip()
        
        self.reports.update_expenses(self.manager.get_all_expenses())
        
        if choice == '1':
            self.reports.print_summary_report()
        elif choice == '2':
            self.reports.print_category_summary()
        elif choice == '3':
            self.reports.print_monthly_summary()
        elif choice == '4':
            try:
                n = int(input("How many top expenses? "))
                self.reports.print_top_expenses(n)
            except ValueError:
                print("✗ Invalid input.")
        else:
            print("✗ Invalid choice.")
    
    def _backup_expenses(self):
        """Create a backup of expenses."""
        print("\n--- BACKUP ---")
        if self.file_handler.backup_expenses():
            print("✓ Backup created successfully!")
        else:
            print("✗ Failed to create backup.")
    
    def _export_expenses(self):
        """Export expenses."""
        print("\n--- EXPORT ---")
        print("1. Export as CSV")
        print("2. Export as JSON")
        choice = input("Choose format (1 or 2): ").strip()
        
        expenses = self.manager.get_all_expenses()
        
        if choice == '1':
            if self.file_handler.export_to_csv(expenses):
                print("✓ Exported to CSV successfully!")
            else:
                print("✗ Failed to export.")
        elif choice == '2':
            if self.file_handler.export_to_json(expenses):
                print("✓ Exported to JSON successfully!")
            else:
                print("✗ Failed to export.")
        else:
            print("✗ Invalid choice.")
    
    def _exit_application(self):
        """Exit the application."""
        print("\nThank you for using Personal Finance Tracker!")
        print("Your data has been saved. Goodbye!")
        exit()
