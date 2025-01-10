class employee:
    def putdata(self):
        self.name=input("enter employee name:")
        self.id=int(input("enter employee id :"))
        self.sallery=int(input("enter employee sallery:"))
    def show(self):
        print("employee name=",self.name)
        print("employee id=",self.id)
        print("employee sellary=",self.sallery)

obj1=employee()
obj1.putdata()
obj1.show()
obj2=employee()
obj2.putdata()
obj2.show()