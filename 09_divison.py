number1 = int(input("Enter the Number :"))
number2 = int(input("Enter the Number :"))

if number2 % number1 == 0:
    print("WAAH LODA")
else:
    r = number1%number2
    x = number2-r
    y = x+number1
    print(x,y)

C = input("Enter Your Choice between up and low:")

if  C == 'up':
    print(y)
else:
    print(x)    
