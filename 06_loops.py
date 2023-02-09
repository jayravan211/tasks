#FOR LOOP

n = int(input("Enter n :"))
for i in range ( 0, n):
        for j in range (i):
            print (i,end='')
        print()    


count=0
n = int(input("Enter n :"))
while (n<10):
        for a in range ( 0, n):
            print (a)
        break
else  :  
    print("PLEASE ENTER NUMBER BELOW 10")    
