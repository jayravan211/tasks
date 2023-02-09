
number1 = int(input("Enter the Number :"))
number2 = int(input("Enter the Number :"))

for i in range(1,11):
    for j in range(number1,number2+1):
        print(f"{j:} x {i:} = {j*i} " ,end="\t")

    print()    