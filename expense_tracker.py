import readline
from expense import Expense
import calendar
import datetime

def main():
    print(f'running expense tracker')
    expense_file_path='expenses.csv'
    budget=2000

 # Get user input for expense.
    expense=get_user_expense()

  # Write their expense to a file.  
    write_user_expense_tofile(expense,expense_file_path)

 # Read file and summarize expenses. 
    summarize_expenses(expense_file_path, budget)


def get_user_expense():
    print(f'enter the user expense')
    expense_name=input('enter the expense name:')
    expense_amount=float(input('enter the expense amount:'))
    expense_category=['food','home','work','fun','misc']

    while True:
        print('select a category:')
        for i,category_name in enumerate(expense_category):
            print(f' {i+1}.{category_name}')

        value_range=f'[1-{len(expense_category)}]'#for the range selection of category number
        selected_index=int(input(f'enter your category number{value_range}:'))-1

        if i in range(len(expense_category)):
            selected_category=expense_category[selected_index]
            new_expense=Expense(name=expense_name,category=selected_category,amount=expense_amount)
            return new_expense
        else:
            print(f'entered number is not in range of category')
        



def write_user_expense_tofile(expense,expense_file_path):
    print(f'write_user_expense_tofile:{expense}to {expense_file_path}')
    with open(expense_file_path,'a')as f:
        f.write(f'{expense.name},{expense.category},{expense.amount}\n')

def summarize_expenses(expense_file_path, budget):
    print(f"🎯 Summarizing User Expense")
    expenses: list[Expense] = []
    with open(expense_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            expense_name, expense_category, expense_amount = line.strip().split(",")
            line_expense = Expense(
                name=expense_name,
                amount=float(expense_amount),
                category=expense_category,
            )
            expenses.append(line_expense)

    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount

    print("Expenses By Category 📈:")
    for key, amount in amount_by_category.items():
        print(f"  {key}: ${amount:.2f}")

    total_spent = sum([x.amount for x in expenses])
    print(f"💵 Total Spent: ${total_spent:.2f}")

    remaining_budget = budget - total_spent
    print(f"✅ Budget Remaining: ${remaining_budget:.2f}")

    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = days_in_month - now.day

    daily_budget = remaining_budget / remaining_days
    print(green(f"👉 Budget Per Day: ${daily_budget:.2f}"))


def green(text):
    return f"\033[92m{text}\033[0m"




if __name__=='__main__':
    main()