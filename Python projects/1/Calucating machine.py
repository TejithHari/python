import time

while True:
    A = input('Enter first number : ')
    B = input('Enter second number : ')

    if not A.isnumeric() and not B.isnumeric():
        print('Please enter digits only')    
    else:
        if '.' in A:
            A = float(A)
        else:
            A = int(A) 

        if '.' in B:
            B = float(B)
        else:
            B = int(B) 

        print('Addition : ', A + B)
        print('Subtraction : ', A - B)
        print('Multiplication : ', A * B)
        print('Division : ',A / B)

        res = input('Do you want to exit?(y/n)')
        if res == 'y':
            time.sleep(5)
            break    
