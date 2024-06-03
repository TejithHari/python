que = ''
while que != 'n':
    que = input('Enter the year:[yyyy], press n to exit. ')
    if que == 'n':
        break
    if que.isnumeric():
        year = int(que)
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
    else:
        print('Please enter the year as numbers with format [yyyy]')
print('Bye Bye...')
    
