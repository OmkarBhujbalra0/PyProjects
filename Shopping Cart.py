items = []
prices = []
total = 0

while True:
    e = input("Enter item you want to add in cart or (Press q to quit):")
    if e.lower() == "q":
        break
    else:
        price = int(input(f'Enter the price of {e}: Rs.'))
        items.append(e)
        prices.append(price)

print("<-------------------  YOUR SHOPPING CART  ------------------->")

for e in items:
    print(e,end=" ")

for i in prices:
    total += i

print(f"\nYour total bill is Rs.{total}")