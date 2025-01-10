class sample:
    a=int(input("enter the value of a ="))
    b=int(input("enter the value of b="))
    def show(self,):
        print("value of a =",self.a)
        print("value of b =",self.b)
class add(sample):
    c=0
    def addition(self):
        self.c=self.a + self.b
        print("addition of number",self.c)
class sub(sample):
    d=0
    def subtraction(self):
        self.d=self.a - self.b
        print("subtraction of number",self.d)

obj1=add()
obj1.show()
obj1.addition()
print("perform multiple inheritance")
obj2=sub()
obj2.show()
obj2.subtraction()
