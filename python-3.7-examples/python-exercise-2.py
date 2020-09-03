print '*** Registration Form *** testing...'

username = raw_input('Enter your username here [4-20 characters]: ')
password = raw_input('Register password [4-10 characters]: ')

username_len = len(username)
password_len = len(password)

if username_len < 4 or username_len > 20:
    print 'Incorrect username size! Try again.'

if password_len < 4 or password_len > 10:
    print 'Incorrect password size! Try again.'

username_first_char = username[0]
username_last_char = username[username_len -1]

if username_first_char != username_last_char:
    print 'Username should start with same letter and it should end with same letter'

while True:

    role = int(raw_input('Choose a role (1 - ADMIN, 2 - USER, 3 - SEMI): '))

    if role == 1:
        print('Welcome %s. You choose ADMIN' % username)
        break
    elif role == 2:
        print('Welcome %s. You choose USER' % username)
        break
    elif role == 3:
        print('Welcome %s. You choose SEMI' % username)
        break
    else:
        print 'Incorrect roll selected'

    # exit = int(raw_input('Press 0 if you wish to exit now: '))
    # if exit == 0:
    #     quit()
