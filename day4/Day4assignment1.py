def is_valid_ipv4(ip):
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit():
            return False
        num = int(part)
        if num < 0 or num > 255:
            return False
        if part != str(num):  
            return False
    return True

print(is_valid_ipv4("222.111.111.111"))  
print(is_valid_ipv4("5555..555"))        
print(is_valid_ipv4("0.0.0.255"))        
print(is_valid_ipv4("0.0.0.0255"))       
