# class CustomList:
#     def __init__(self,L):
#         self.L = L
#         self.i = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         while self.i < len(self.L):
#             if self.L[self.i] > 15:
#                 temp = self.L[self.i]
#                 self.i = self.i + 1
#                 return temp
#             else:
#                 self.i = self.i + 1
#         else:
#            raise StopIteration()
#
#
# if __name__=="__main__":
#     L = [10,20,5,6,7,45]
#     obj = CustomList(L)
#     for i in obj:
#         print(i)

# class A:
#     def __init__(self,a = 300):
#         self.a = a
#
# class B(A):
#     def __init__(self,a,b):
#         self.b = b
#         super(B,self).__init__()
#
#
# if __name__=="__main__":
#     b_obj = B(100,200)
#     print(b_obj.a + b_obj.b)


class A:
    def __init__(self):
        self.a = 100


class B:
    def __init__(self):
        self.a = 200


class C(B, A):
    def __init__(self):
        super(C, self).__init__()
        A.__init__(self)


if __name__ == "__main__":
    c_obj = C()
    print(c_obj.a)
