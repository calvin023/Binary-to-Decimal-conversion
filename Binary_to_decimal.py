while True:
    binnumber = input("Enter your binary number: ")
    if not all(c.isdigit() and int(c) < 2 for c in binnumber):
        print("Invalid binary number.")
        continue
    else:
        binlist = list(binnumber)
        decimal = 0
        for i in range(len(binlist)):
            decimal += int(binlist[i]) * 2**(len(binlist)-i-1)
        print(decimal)
        break