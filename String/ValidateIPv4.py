'''
An IP address is a unique identifier for devices on a network, enabling internet communication.
IPv4: IPv4 addresses use dot-decimal notation, consisting of four numbers (0-255) separated by dots, e.g., 172.16.254.1
1. Each section split by ‘.’ contains only digits, has no leading zeros, and lies within the range 0-255.
'''

def valid_part(part):
    n = len(part)
    if n == 0 or n > 3:
        return False
    if not part.isdigit():
        return False
    if part[0] == 0 and n > 1:
        return False
    num = int(part)
    return 0 <= num <= 255

def isValid(ip):
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        if not valid_part(part):
            return False
    return True

ip1 = "128.0.0.1"
ip2 = "125.16.100.1"
ip3 = "125.512.100.1"
ip4 = "125.512.100.abc"

print(isValid(ip1))
print(isValid(ip2))
print(isValid(ip3))
print(isValid(ip4))