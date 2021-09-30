# Stock one
stock1_name = input("Enter the first stock's name: ")
stock1_price = float(input("Enter the first stock's value: "))

# Stock two
stock2_name = input("Enter the first stock's name: ")
stock2_price = float(input("Enter the second stock's value: "))

# Stock three
stock3_name = input("Enter the first stock's name: ")
stock3_price = float(input("Enter the third stock's value: "))

print(stock1_name + "\t" + stock2_name + "\t" + stock3_name)
print(str(stock1_price) + "\t" + str(stock2_price) + "\t" + str(stock3_price))
total = stock1_price + stock2_price + stock3_price
print(str(stock1_price / total) + "\t" + str(stock2_price / total) + "\t" + str(stock3_price / total))


if stock1_price > stock2_price:
    print(stock1_name + " is worth more than " + stock2_name)
else: 
    print(stock2_name + " is worth more than " + stock1_name)


