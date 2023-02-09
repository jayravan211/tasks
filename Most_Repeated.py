n = 0
data = [1,2,3,4,5,6,7,8,9,0,1,1,2,3,4,5,6,6,7,8,8,9,0,1,1,1]
number = data[0]
for element in data:
    b = (data.count(element))
    if b > n:
        n = b
        number = element  
print(f"{number} is most repeated number {b} Times...")  



