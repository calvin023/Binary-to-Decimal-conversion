binnumber = input("Enter your binary number: ")
# Checking that the input is a binary number
if not all(c.isdigit() and int(c) < 2 for c in binnumber):
    raise ValueError("Invalid binary number")
else:
    # Setting up variables
    binlist = list(binnumber)
    decimal = 0
    # Converting to decimal
    for i in range(len(binlist)):
        decimal += int(binlist[i]) * 2**(len(binlist)-i-1)
    print(decimal)
