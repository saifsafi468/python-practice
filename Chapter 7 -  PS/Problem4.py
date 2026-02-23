num = int(input("Enter number: "))
is_prime = True

for i in range(2, num):
    if num % i == 0:
        is_prime = False
        break

if is_prime and num > 1:
    print("Prime number.")
else:
    print("Not prime")