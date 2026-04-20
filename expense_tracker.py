from datetime import datetime
'''
A Simple Expense Tracker Python Project That Keeps Track Of Our Daily Expenses!
'''
expense_record = []

def Add_Expense(Category,Date,Amount):
    '''
    Function Add_Expense that adds multiple
    Expenses
    '''
    expense_record.append((Category,Amount,Date))
    print(f"{'Category':<10} {'Amount':<12} {'Date':<10}")
    return '-'*32