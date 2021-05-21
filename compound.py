p = float(input("Enter the principle amount : "))
r = float(input("Enter the rate of interest : "))
t = float(input("Enter the time: "))

ci =  p *(1 + r / 100)** t 

print("Principle amount: ", p)
print("Interest rate: ", r)
print("Time: ", t)
print("compound Interest: ", ci)
