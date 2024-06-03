import time
wrong_password = 0
while True:
    password = input('Password : ')
    if password == '123654':
        print('Succesfully logged in')
        time.sleep(5)
        print('Dell : Satya : satya|Tejith : 1234||Scratch : abc1234|coder12342014 : abc1234 :)')
        time.sleep(20)
        break
    elif wrong_password > 5:
        print('Try again later.....')
        time.sleep(5)
        break
    else:
        print('Wrong Password.....')
        wrong_password = wrong_password + 1
