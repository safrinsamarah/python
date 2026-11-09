import array as arr

stock = arr.array('i', [65,23,32,43,100, 167, 122])

print("stock: ", stock)
print("total stock: ",len(stock))
print("first product: ", stock[0])
print("last product: ",stock[-1])

stock[0] = 150
print(stock)
stock.append(170)
stock.insert(2, 300)
print(stock)
stock.remove(100)
print(stock)

print("first three products: ",stock[:3])
print("Low stock products: ")

for product in stock:
    if product < 100:
        print(product)