import mysql.connector
conn = mysql.connector.connect(host="localhost", username="root", password="root", database="bankmanagement")

def closeAccount():
    accountNo = input('Enter your account number: ')

    sql1 = 'delete from account where accountNo=%s'
    sql2 = 'delete from amount where accountNo=%s'
    data = (accountNo,)

    my_cursor = conn.cursor()
    my_cursor.execute(sql1, data)
    my_cursor.execute(sql2, data)
    conn.commit()

    print('\nAccount Deleted Successfully')

    main()





def customerDetails():
    accountNo = input('Enter your account number: ')

    sql1 = 'select * from account where accountNo=%s'
    data1 = (accountNo,)

    my_cursor = conn.cursor()
    my_cursor.execute(sql1, data1)
    x = my_cursor.fetchone()

    info = ('Name: ', 'Account No: ', 'Date of Birth: ', 'Address: ', 'Mobile No: ',
            'Opening Balance: ')

    print('\n')

    for i in range(6):
        print(info[i],x[i])

    main()





def balEnquiry():
    accountNo = input('Enter your account number: ')

    sql1 = 'select balance from amount where accountNo=%s'
    data1 = (accountNo,)

    my_cursor = conn.cursor()
    my_cursor.execute(sql1, data1)
    x = my_cursor.fetchone()

    print('\n')
    print('Balance for account', accountNo, 'is', x[0])
    main()





def withdraw():
    bal = int(input('How much amount you want to withdraw: '))
    accountNo = input('Enter your account number: ')

    sql1 = 'select balance from amount where accountNo=%s'
    data1 = (accountNo,)

    my_cursor = conn.cursor()
    my_cursor.execute(sql1, data1)
    x = my_cursor.fetchone()

    y = x[0] - bal
    sql2 = 'update amount set balance=%s where accountNo=%s'
    data2 = (y, accountNo)
    my_cursor.execute(sql2, data2)
    conn.commit()

    print('\n')
    print(bal, 'Tk withdrawn successfully')
    main()





def deposit():
    bal = int(input('How much amount you want to deposit: '))
    accountNo = input('Enter your account number: ')

    sql1 = 'select balance from amount where accountNo=%s'
    data1 = (accountNo,)

    my_cursor = conn.cursor()
    my_cursor.execute(sql1, data1)
    x = my_cursor.fetchone()

    y = x[0] + bal
    sql2 = 'update amount set balance=%s where accountNo=%s'
    data2 = (y, accountNo)
    my_cursor.execute(sql2, data2)
    conn.commit()

    print('\n')
    print(bal, 'Tk deposited successfully')
    main()





def openAccount():
    name = input('Enter your name: ')
    accountNo = input('Enter the account number: ')
    dob = input('Enter your date of birth: ')
    address = input('Enter your address: ')
    contact = input('Enter your contact number: ')
    openingBal = input('How much you want to deposit (opening balance): ')

    sql1 = 'insert into account values(%s, %s, %s, %s, %s, %s)'
    data1 = (name, accountNo, dob, address, contact, openingBal)

    sql2 = 'insert into amount values(%s, %s, %s)'
    data2 = (name, accountNo, openingBal)

    x = conn.cursor()
    x.execute(sql1, data1)
    x.execute(sql2, data2)
    conn.commit()

    print('Data inserted successfully')
    main()





def main():
    print('''
                1/ Open New Account
                2/ Deposit Amount
                3/ Withdraw Amount
                4/ Balance Enquiry
                5/ Check Customer Details
                6/ Close an Account
                7/ Exit''')

    choice = input("\nEnter the task you want to perform: ")

    if choice == '1':
        openAccount()
    elif choice == '2':
        deposit()
    elif choice == '3':
        withdraw()
    elif choice == '4':
        balEnquiry()
    elif choice == '5':
        customerDetails()
    elif choice == '6':
        closeAccount()
    elif choice == '7':
        print('\nThanks for using our service')
        quit()
    else:
        print('\n\nInvalid Data ! Please Enter Again')
        main()

main()

