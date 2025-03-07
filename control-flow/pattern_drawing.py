number = int(input("Enter the size of the pattern: "))

count = 1

while count <= number:
    for x in range(number):
        print("*", end="")
    count += 1
    print()
