def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
def is_twisted_prime(n):
    string_convertion=str(n)
    reversed_n = int(string_convertion[::-1])
    return is_prime(n) and is_prime(reversed_n)

num = int(input("Enter a number: "))
if is_twisted_prime(num):
    print(f"{num} is a Twisted Prime.")
else:
    print(f"{num} is NOT a Twisted Prime.")
