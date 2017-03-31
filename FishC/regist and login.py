#用dict建立账号及登录系统


user_data={}
def new_user():
    promp = 'Please enter username'
    while True:
        username=input(promp)
        if username in user_data:
            print ('username has already been used.')
            continue
        else:
            break
    psw= input('Please set you password')
    user_data[username]=psw
    print ('Registration complete, give it a try!')
def sign_in():
    promp = 'Please enter username'
    while True:
        username = input(promp)
        if username not in user_data:
            print('username not available, please reenter')
            continue
        else:
            break

    psw = input('Please enter you password')
    if psw != user_data[username]:
        print('Your password is wrong!')
    else:
        print('Wellcome to xxoo system!')
def showMenu():
     prompt = '''
    |--- 新建用户：N/n ---|
    |--- 登录账号：E/e ---|
    |--- 推出程序：Q/q ---|
    |--- 请输入指令代码：'''
     while True:
         pa= False
         while not pa:
            code = input(prompt)
            if code not in 'NnEeQq':
                print('代码错误 重新输入')
            else:
                pa = True
         if code == 'Q' or code == 'q':
             break
         if code == 'N' or code == 'n':
             new_user()
         if code == 'E' or code == 'e'
             sign_in()


showMenu()


