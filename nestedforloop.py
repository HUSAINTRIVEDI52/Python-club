rows=int(input("Enter number of rows:"))
columns=int(input("Enter number of columns:"))
symbol=input("Enter the symbol to be printed:")

for i in range(rows):
    for j in range(columns):
        print(symbol,end="")
    print()