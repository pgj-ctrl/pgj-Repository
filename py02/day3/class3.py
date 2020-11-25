# class A:
#     def func1(self):
#         print('A func')
#
#     def func4(self):
#         print('aaaaa fn4')
#
# class B:
#     def func2(self):
#         print('B func')
#
#     def func4(self):
#         print('bbbbb fn4')
#
# class C(A,B):
#     def func3(self):
#         print('C func')
#
#     def func4(self):
#         print('cccc fn4')
#
# if __name__ == '__main__':
#     c1 = C()
#     c1.func1()
#     c1.func2()
#     c1.func3()
#     c1.func4()

class Book:
    def __init__(self,title,author):
        self.title =title
        self.author = author

    def __str__(self):
        return '<%s>' % self.title

    def __call__(self,):
        print('%s is %s write' % (self.title,self.author))

if __name__ == '__main__':
    xyj = Book("西游记",'吴承恩')
    print(xyj)
    xyj()