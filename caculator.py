class calculator:
    def add(self):
        self.a=int(input("enter first number"))
        self.b=int(input("enter second number"))
        self.c =self.a+self.b
        print("addition of number",self.c)

    def sub(self):
        self.a = int(input("enter first number"))
        self.b = int(input("enter second number"))
        self.c = self.a - self.b
        print("subtraction of number", self.c)

    def mul(self):
        self.a = int(input("enter first number"))
        self.b = int(input("enter second number"))
        self.c = self.a * self.b
        print("multiplication of number", self.c)
    def div(self):
        self.a = int(input("enter first number"))
        self.b = int(input("enter second number"))
        if self.b != 0:
            self.c = self.a / self.b
            print(f"The result of division is: {self.c}")
        else:
            print("Division by zero is not allowed.")
obj1=calculator()
while True:
    op =input("enter operation which you want to perform(+,-,*,/) or q for quit =")
    if op == 'q':
            print("program is exiting goodbye! :)")
            break
    match op :
            case '+':
                obj1.add()
            case '-' :
                obj1.sub()
            case '*':
                obj1.mul()
            case '/' :
                obj1.div()
            case '_':
                print("invalid operation")




