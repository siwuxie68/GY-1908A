class Nmsl():
    def aaa(self):
        print('wsnd')
    def ins(self):
        print('wsngg')

    def s(self,*args, **kwargs):
        print(args)
        print(kwargs)



    def jia_f(self,a, b=60):
        return a + b
c = Nmsl()
c.ins()
c.aaa()
print(c.jia_f(8))
c.s(1, 2, 3, 5, 6, {'nmsl': 'wsnd'}, awsl=1234)
#dergakio   要求生成两个新的字符串  drai  和egko

oo='dergakio'
print(oo[::2])
print(oo[1::2])


#fjdshfsdhjhj789

insk='fjdshfsdhjhj789'
print(insk[::-5])

#字符串切片


ncn='剑气长城,浩然天下,清明天下'

print(ncn.split(","))

lll='       nmsl                 '
print(lll.rstrip())

po='fjkdsjfkdsjgkllkfdsjlkjlkfsdjfldjklF"      jKLjkl"sdJFlk'
print(po.replace('"',"'"))
print(po.replace(' ',''))
print(po.replace('"',''))

g='niuchaonan'
print(g.find("na"))
print(len(g))

ip='GET, https://,www.fiddler2.com,/UpdateCheck.aspx?,isBeta=False, HTTP/1.1'
print(ip.split(','))










y=[1,9,8,6,5,3,2,1]
y.append(1212)

from demo.day3 import Nmsl

wsnd=Nmsl


wsnd.mm()