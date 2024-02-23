# Write your code here
def is_prime(n):
    if n == 1 or n == 0:
        return False
    else:
        for i in range (2, n):
            if n % i == 0:
                return False
        return True
        
def main():
    n = int(input("nummer aub: "))
    print(is_prime(n))

#main()