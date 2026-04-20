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


def View_Expense(user_category):
    if not expense_record:
        return 'Empty Record'
    else:
        print(f"{'Category':<10} {'Amount':<12} {'Date':<10}")
        print('-'*32)
        expense_list = '\n'.join([f'{c:<12} {a:<12} {d}' for c,d,a in expense_record if user_category == c])
        return expense_list