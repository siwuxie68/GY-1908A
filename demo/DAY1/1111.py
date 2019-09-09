#在最后增加单条数据
y=[1,9,8,6,5,3,2,1]
y.append(12)
print(y)





#在列表任意位置添加数据
y.insert(3,50)
print(y)

#在列表里增加多个数据
s=[1,5,9,8,]
y.extend(s)
print(y)
print(s)


#在列表中删除数据 y.pop()为空时默认删除是最后一位数据 填写位标时就删除位标数据


print(y.pop())
print(y)

print(y.pop(2))
print(y)

#删除指定数据使用的是remove

y.remove(1)
print(y)

#修改列表中的数据 中括号里放的是要修改数据的位标=后面的指是修改的数据
y[9]=1
print(y)


#查看列表，字符，元组里数据的长度
print(len(y))
