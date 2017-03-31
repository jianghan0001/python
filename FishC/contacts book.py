print('|---欢迎进入通讯录程序---|')
print('|---1：查询联系人资料---|')
print('|---2：插入新的联系人---|')
print('|---3：删除已有联系人---|')
print('|---4：推出通讯录程序---|')

contacts=dict()
while 1:
    instr=int(input('\n请输入相关指令代码：'))
    if instr == 1:
        name=input('请输入联系人姓名')
        if name in contacts:
            print (name + ':' +contacts[name])
        else:
            print ('%s 不在通讯录中' %name)
    if instr == 2:
        name = ('请输入联系人姓名')
        if name in contacts:
            print('Already there!')
            print(name + ':' + contacts[name])
            if input('Do you want to change it? Yes/No') == 'Yes':
                contacts[name]=input('please enter you new num')
        else:
            contacts[name]=input('请输入联系方式')
    if instr == 3:
        name = input('请输入联系人姓名')
        if name in contacts:
            del(contacts[name])
        else:
            print('There is no %s in the book' %name)
    if instr == 4:
        break
print('Thank you for using our product!')