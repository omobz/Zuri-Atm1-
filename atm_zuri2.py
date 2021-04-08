print('Welcome to Zenith bank ATM')
import datetime
now = datetime.datetime.now()
print('current date and time : ')
print(now.strftime('%Y-%m-%d %H:%M:%S'))
Pin = input('Please enter your pin \n')
allowedPin = ['1111', '2222', '3333']
if(Pin in allowedPin):
    print("Available Options")
    print('1. Withdrawal')
    print('2. Deposit')
    print('3. Complaint')
    selectedOption = int(input('Pls select an option:'))
    if selectedOption==1:
        withdrawAmount=int(input('How much would you like to withdraw? \n'))
        if withdrawAmount>0 :
            print('pls take your cash')
        else:
            print('insufficient balance')
    elif selectedOption==2:
        depositAmount=int(input('How much would you like to deposit? \n'))
        if depositAmount>0:
            print('Deposit sucessful! Available balance is ()')
        else:
            print('input valid amount to proceed')
    elif selectedOption==3:
        Complaint= str(input('What issue will you like to report \n'))
        print('Thank you for contacting us!')
else: 
    print ('Wrong pin! Try again')