#Enter a year, check if a year is a leaf year or not. Leaf year: dividable for 4 and undividable for 100, or dividable for 400
year = int(input("Enter a year: "))
if (year%4==0 and year%100 != 0) or year % 400==0:
    print("Leaf year")
else:
    print("Not leaf year")