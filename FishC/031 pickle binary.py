#031 将啥啥啥转换成二进制文件
import pickle
my_list= [1, 3, 4, 3.14]
pickle_file = open('my_list.pkl', 'wb')#wb 以二进制写 必须
pickle.dump.(my_list,pickle_file) #把my_list的内容写到my_list.pkl里面
pickle_file.close()


pickle_file= open('my_list.pkl', 'rb')#以二进制读 必须
my_list2= pickle.load(pickle_file) #把my_list.pkl的内容load到my_list2里
print(my_list2)

#在实际编程中 把大的list，dict先弄成pickle会让代码变漂亮

import pickle
f= open('data.pkl', 'wb')
pickle.dump(data, f)#dump what to where
f.close()
#存

import pickle
f= open('data.pkl', 'rb')
data = pickle.load(f)
f.close()
取