# example.py
#
# Example of calculating with dictionaries

prices = {
   'ACME': 45.23,
   'AAPL': 612.78,
   'IBM': 205.55,
   'HPQ': 37.20,
   'FB': 10.75
}

# Find min and max price
# Comparision is done based on the first value
# Combine three values and return the list of tupele.
# Example: >>> zip([1,2,3],[4,5,6],[7,8,9])
#  [(1, 4, 7), (2, 5, 8), (3, 6, 9)]


min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))

print('min price:', min_price)
print('max price:', max_price)

print('sorted prices:')
# Sort based on the first tuple value
# Nature of sorted function is sort the value based on first index value in case of iterable of iterable.
prices_sorted = sorted(zip(prices.values(), prices.keys()))
for price, name in prices_sorted:
    print('    ', name, price)


