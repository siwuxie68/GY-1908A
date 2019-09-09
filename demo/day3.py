#字典数据里新增新的数据

dd={'nmsl':'wsngg','wsnd':'whndsnmdhez'}
dd['nslmm'],dd['nslm']  = 'wsd','oouu'

print(dd)
#删除数据
print(dd.pop('nslm'))
print(dd)

del dd['nmsl']
print(dd)


#清空数据
ins={'name':'json','sex':'♂','stu':'25'}
print(ins)
ins.clear()
ins=a=''

print(ins)
#   生产一个新的字典
ins={'name':'json','sex':'♂','stu':'25'}
sin={'key':'values'}

z=dict(ins,**sin)
print(z)

class Nmsl():
    def nn(self):
        print('我是你哥哥')


    def mm(self):
        print('我们都是你吗的儿子')





