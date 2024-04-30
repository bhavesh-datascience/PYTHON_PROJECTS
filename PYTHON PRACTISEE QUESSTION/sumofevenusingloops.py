total = 0
even = int(input("Enter an even number: "))

if even % 2 == 0:
    for number in range(0, even+1, 2):
        total = total + number
    print(total)
else:
    print("Entered number is not even.")
