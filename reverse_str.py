#reverse the given string

s = input("Enter the String : ")

def task(x):
    if len(x) == 0:
        return
    print(x[-1],end = "")
    m = ""
    for i in range(len(x)-1):
        m = m + x[i]
    task(m)

task(s)
