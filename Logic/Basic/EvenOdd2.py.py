''' Given a number n, check whether it is even or odd. Return true for even and false for odd. '''

# We use Bitwise AND operator - The last bit of all odd numbers is always 1, for even numbers it is always 0
# So we perform Bitwise AND operation with 1

def isEven(n):
    return (n & 1) == 0

while True:
    user_ip = input("Enter a number (or type 'exit to stop): ").strip().lower()
    if user_ip == 'exit':
        break
    if user_ip.isdigit():
        n = int(user_ip)
        if isEven(n):
            print(f"{n} is an even number")
        else:
            print(f"{n} is an odd number")