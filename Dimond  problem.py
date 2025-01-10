class A:
    def display(self):
        print("hii i am class A")

class B(A):
    def display(self):
        print("hi i am class B")

class C(A):
    pass
    def show(self):
        print("hello i am class C")

class D(B,C):
    def show(self):
        print("hello i am class D")

d1=D()
d1.display()
d1.show()
