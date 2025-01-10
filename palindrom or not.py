num=int(input("enter a number "))
temp=num
rev=0
while(num>0):
    dig= num % 10
    rev= rev * 10 + dig
    num =  num

if temp == rev:
    print("number is palindrom")
else:
    print("number is not palindrom ")