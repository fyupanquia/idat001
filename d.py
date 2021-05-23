number=int(input("Enter a four digits number: "))

thousand = int(number/1000)
number = number%1000
hundreds= int(number/100)
number = number%100
tens= int(number/10)
number = number % 10
units= int(number)

min = min(thousand,hundreds,tens,units)
max = max(thousand, hundreds, tens, units)

print(f"Digits: {thousand}, {hundreds}, {tens} and {units}")
print(f"Min: {min}")
print(f"Max: {max}")
