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

with open('expenses.txt', 'a') as f:
    f.write(f"{'Category':<10} {'Amount':<12} {'Date':<10}\n")
    f.write(f"{'-'*32}\n")

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


def Total_Spending(): 
    total_amount = 0
    for c,d,a in expense_record:
        total_amount+=a
    return f"Total Spending -----> {total_amount}"

def Exit():
    if not expense_record:
        return 'No records found! please try to add expenses!'
    print('Your final expense record!')
    print(f"{'Category':<10} {'Amount':<12} {'Date':<10}")
    print('-'*32)

    final_expense = '\n'.join([f"{category:<10} {amount:<12} {date:<10}" for category,amount,date in expense_record])
    return final_expense

class CategoryNameError(Exception):
    pass

while True:
    print('Choose your options from following:\n 1.Add Expense\n','2.View Expense\n','3.Category Wise Total\n','4.Total Spending\n','5.Exit\n') 
    user_opt = input('Enter option described above: ').strip()

    if user_opt == '1':
        while True:
            try:
                Category = input('Enter a valid Category Name: ').strip()
                if any(ch.isdigit() for ch in Category):
                    raise CategoryNameError('Category name must not contains digits! Try Again!')  #Handles Category Name
                break
            except CategoryNameError as e:
                print(e)

        while True:
            try:
                Date = datetime.strftime(datetime.strptime(input('Enter date format like (YY-MM-DD):'),'%Y-%m-%d'),'%Y-%m-%d')  #Handles Datetime Format
                Amount = int(input('Enter amount you spend:')) #Handles Amount
                break
            except ValueError as e:
                print('Invalid datetime | amount!',e)

        print(Add_Expense(Category,Amount,Date))
            
        for category,date,amount in expense_record:
            print(f"{category:<10} {amount:<12} {date}")

        with open('expenses.txt', 'a') as af:
            af.write(f"{Category:<10} {Amount:<12} {Date}\n")

    elif user_opt == '2':
        user_category = input('Enter Category to view your expenses: ')
        print(View_Expense(user_category))

    elif user_opt == '3':
        print(Category_Wise_Total())

    elif user_opt == '4':
        print(Total_Spending())

    elif user_opt == '5':
        print(Exit())
        print('Thanks for visiting! Have a great day')
        break
    else:
        print('Invalid Option! Please try again')

                
