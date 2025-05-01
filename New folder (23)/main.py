def check_bit():
    print("welcome to the bit checker game!")
    print("You will be given a number, and i'll tell you if it's a 0-bit or a 1-bit.\n")

    while True:
        bit = input("enter a bit (0 or 1) or 'exit' to quit: ")

        if bit.lower() == 'exit':
            print("Thanks for playing!")
            break
        elif bit == '0':
            print("You entered a 0 that's called a **zero bit**!\n")
        elif bit == '1':
            print("You entered a 1 that's called a **one bit**!\n")
        else:
            print("Invalid input! Please enter a 0 or a 1.\n")

# run the program
check_bit()

