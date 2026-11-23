import readline
from expense import Expense
def main():
    print(f'running expense tracker')
    expense_file_path='expenses.csv'

    expense=get_user_expense()
   
    write_user_expense_tofile(expense,expense_file_path)
    sumarize_expenses(expense_file_path)

def get_user_expense():
    print(f'enter the user expense')
    expense_name=input('enter the expense name:')
    expense_amount=float(input('enter the expense amount:'))
    print(f'you enter the {expense_amount} as a expense amount')
    print(f'you enter the {expense_name} as a expense name')

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

def sumarize_expenses(expense_file_path):
    print(f'suumarize expenses-')
    expenses=[]
    with open(expense_file_path,'r') as f:
        lines=f.readlines()
        for line in lines:
            stripped_line=line.strip()
            expense_name,expense_category,expense_amount=line.strip().split(',')
            line_expense=Expense(name=expense_name,amount=float(expense_amount),category=expense_category,)
            print(line_expense)
            expenses.append(line_expense)
        print(expenses)

if __name__=='__main__':
    main()