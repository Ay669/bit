number = int(input("Enter a number: "))
binary = bin(number)[2:]
print("Binary is:", binary)

n = int(input("Which bit number do you want to see? (1= first from left): "))
if 1 <= n <= len(binary):
    bit = binary[n-1]
    print("that bit is:", bit)
else:
    print("oops! bit number too big.")
    