total = 0
for i in range(5):
    price = float(input('Enter the product price:'))

    total = total + price

gst = total * 18 / 100
bill = total + gst

print(f'Total Bill is:{bill}')