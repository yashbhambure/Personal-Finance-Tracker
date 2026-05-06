# Personal Finance Tracker

A simple yet powerful command-line application to track and manage your personal expenses efficiently.

## Features

- **Add Expenses**: Quickly add new expenses with category, amount, and description
- **View Expenses**: Display all expenses or filter by category, date, or date range
- **Search Functionality**: Search expenses by keywords in descriptions
- **Update & Delete**: Modify or remove existing expense entries
- **Comprehensive Reports**:
  - Summary reports with total, average, highest, and lowest expenses
  - Category-wise breakdown
  - Monthly expense summaries
  - Top expenses analysis
- **Data Management**:
  - Persistent data storage in JSON format
  - Automatic backup functionality
  - Export to CSV and JSON formats
- **User-Friendly CLI**: Intuitive menu-driven interface

## Project Structure

```
week4-finance-tracker/
├── finance_tracker/
│   ├── __init__.py              # Package initialization
│   ├── main.py                  # Main CLI application
│   ├── expense.py               # Expense class definition
│   ├── expense_manager.py       # Expense management logic
│   ├── file_handler.py          # File I/O operations
│   ├── reports.py               # Report generation
│   └── utils.py                 # Utility functions
├── data/
│   ├── expenses.json            # Expense data storage
│   ├── backup/                  # Backup directory
│   └── exports/                 # Export directory
├── tests/
│   ├── test_expense.py          # Expense class tests
│   ├── test_file_handler.py     # FileHandler tests
│   └── test_reports.py          # Reports tests
├── requirements.txt             # Project dependencies
├── README.md                    # This file
├── .gitignore                   # Git ignore rules
└── run.py                       # Application entry point
```

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd week4-finance-tracker
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Running the Application

```bash
python run.py
```

The application will start an interactive CLI menu with the following options:

1. **Add Expense**: Add a new expense entry
2. **View All Expenses**: Display all recorded expenses
3. **View Expenses by Category**: Filter expenses by category
4. **View Expenses by Date**: View expenses on specific dates or date ranges
5. **Delete Expense**: Remove an expense entry
6. **Update Expense**: Modify an existing expense
7. **Search Expenses**: Search for expenses by keywords
8. **View Reports**: Generate various reports and statistics
9. **Backup Expenses**: Create a backup of current data
10. **Export Expenses**: Export data to CSV or JSON format
11. **Exit**: Close the application

### Example Commands

Adding an expense:
```
Enter amount: $50.00
Enter category: Food
Enter description: Lunch at restaurant
Enter date (YYYY-MM-DD) or press Enter for today: 2024-01-15
```

### Running Tests

```bash
python -m pytest tests/
```

Or using unittest:
```bash
python -m unittest discover -s tests -p "test_*.py"
```

## Data Management

### Expense Storage
Expenses are stored in `data/expenses.json` with the following structure:
```json
[
  {
    "date": "2024-01-15",
    "category": "Food",
    "amount": 50.00,
    "description": "Lunch at restaurant"
  }
]
```

### Backups
Automatic backups are created in `data/backup/` with timestamp-based filenames.

### Exports
Exported files are saved in `data/exports/` in your chosen format (CSV or JSON).

## Categories

Suggested expense categories:
- Food
- Transport
- Entertainment
- Utilities
- Health
- Shopping
- Education
- Other

## Features in Detail

### Summary Report
Shows:
- Total expenses
- Number of entries
- Average expense
- Highest expense
- Lowest expense

### Category Breakdown
Displays total spending and transaction count for each category.

### Monthly Summary
Shows monthly expense totals and transaction counts.

### Top Expenses
Lists the highest expense transactions.

## Data Validation

The application includes validation for:
- **Amount**: Must be a positive number
- **Date**: Must be in YYYY-MM-DD format
- **Category**: Cannot be empty, maximum 50 characters
- **Description**: Maximum 200 characters

## Requirements

- Python 3.7+
- No external dependencies required for core functionality

## Future Enhancements

- Budget setting and tracking
- Recurring expense management
- Multi-user support
- Data visualization with charts
- Cloud synchronization
- Mobile app integration
- Advanced filtering options
- Receipt/attachment support

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Support

For issues or questions, please create an issue in the repository.

## Author

Developed as part of the Developer's Arena Week 4 Project.

---

**Last Updated**: 2024
**Version**: 1.0.0
