''' Given Principal p, Rate r and Time t, the task is to calculate Simple Interest. '''

# Formula: SI = (p * t * r)/100
# p = 10000 r = 5 t = 5 
# -> we need to find simple interest on 10000/- at the rate of 5% for 5 units of time 
# SI = 2500

def simple_interest(p, t, r):
    return (p * t * r)/100

p = int(input("Enter principle amount: "))
t = int(input("Enter time period: "))
r = int(input("Enter the rate of interest: "))

print(simple_interest(p, t, r))
