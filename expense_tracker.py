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
    

def Category_Wise_Total():
    if not expense_record:
        return 'No Expenses!' 
    category_total = {}

    for category,date,amount in expense_record:
        category_total[category] = category_total.get(category,0)+amount

    print('--------CATEGORY WISE TOTAL--------')
    print(f"{'Category':<10} {'Amount':<12}")
    print('-'*22)
    expenses = '\n'.join([f'{category:<10} {amount:<12}' for category,amount in category_total.items()])
    return expenses