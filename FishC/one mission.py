def write_file(boy, girl, count):
    file_name_boy= 'boy_' + str(count) + '.txt '#���ļ����б���
    file_name_girl= 'girl_' + str(count) + '.txt '
    boy_file = open(file_name_boy, 'x')
    girl_file = open(girl_name_boy, 'x')
    boy_file.writelines(boy)
    girl_file.writelines(girl)
    boy_file.close()
    girl_file.close()

def slipt_file(file_name):
    f= open('record.txt')
    boy = []
    girl= []
    count = 1
    for each_line in f:
        if each_line != '======':
            (role, line_spoken)= each_line.split(':', 1)
            if role == 'С����':
            boy.append(line_spoken)
            if role = 'С�ͷ�':
                girl.append(line_spoken)
    #������������ַ����ָ�
        else:
            write_file(boy, girl, count)
            boy = []
            girl = []
            count += 1
    write_file(boy, girl, count)
    f.close()
split_file(record.txt)
