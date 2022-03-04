
def findPrice(name,price=10):
    print('product is: ', name)
    print('price is: ', price)

# valid findPrice('car')
# valid findPrice('car',200)
# valid findPrice(name="car", price=200)
# valid findPrice('car', price=200)
# valid  findPrice(price=200,name="car")
# invalid findPrice(price=200,'car')
# invalid findPrice(200, name="car")

findPrice("car")
