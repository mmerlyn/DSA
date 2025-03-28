'''
An IP address is a unique identifier for devices on a network, enabling internet communication.'
IPv6: IPv6 addresses use hexadecimal colon notation, with eight groups of four hex digits 
(0-9, A-F) separated by colons, e.g., 2001:db8:85a3::8a2e:370:7334
1. Each section split by : contains only hexadecimal digits (0-9, a-f, A-F) and is within the valid length of 1 to 4 characters.
'''

def valid_part(part):
    n = len(part)
    if n < 1 or n > 4:
        return False
    for char in part:
        if not (char.isdigit() or 'a' <= char.lower() <= 'f'):
            return False
    return True

def isValid(ip):
    parts = ip.split(':')
    if len(parts) != 8:
        return False
    for part in parts:
        if not valid_part(part):
            return False
    return True

ip1 = "2001:0db8:85a3:0000:0000:8a2e:0370:7334"
ip2 = "fe80::1"
ip3 = "2001:db8:85a3::8a2e:370:7334"
ip4 = "2001:0db8:85a3:xyz:0000:8a2e:0370:7334"

print(isValid(ip1))
print(isValid(ip2))
print(isValid(ip3))
print(isValid(ip4))