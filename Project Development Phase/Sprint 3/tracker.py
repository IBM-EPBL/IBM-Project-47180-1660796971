def add_expense(good_or_service, price, date, expense_type):
     GOODS_OR_SERVICES.append(good_or_service)
     PRICES.append(price) 
     DATES.append(date)
     EXPENSE_TYPES.append(expense_type)
      option = -1
while(option != 0):
    #options
    print('welcome to the simple expense tracker:')
    print('1. add food expense')
    print('2. add household expenses')
    print('3. add transportation expenses')
    print('4. show and save the expense report')
    print('0. exit')
    option = int(input('choose an option:\n'))
    
    print()
    #check
    if option == 0:
        print('exiting the  program')
        break
    elif option == 1:
        print('adding food')
        expense_type = 'FOOD' 
    elif option== 2:
        print('adding household')
        expense_type = 'HOUSEHOLD'
    elif option == 3:
        print('adding transportation')
        expense_type = 'TRANSPORTATION'
    elif option == 4: 
        expense_report = pd.DataFrame()
        expense_report['GOODS_OR_SERVICES'] = GOODS_OR_SERVICES 
        expense_report['PRICES'] = PRICES 
        expense_report['DATES'] = DATES 
        expense_report['EXPENSE_TYPES'] = EXPENSE_TYPES
        
        expense_report.to_csv('expenses.csv') 
        
        print(expense_report)
    else:
        print('you choose an incorrect option')
    
    if option == 1 or option == 2 or option == 3:
        good_or_service = input('enter the good for the expense type' +expense_type+':\n' )
        price = float(input('enter the price of good or services:\n'))
        today = date.today()
        add_expense(good_or_service, price, today, expense_type)
        
    print()
