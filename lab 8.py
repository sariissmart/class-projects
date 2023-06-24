prices = {"product" : "apple",
    "price":10,
}
print(prices["price"])
print(prices["product"])
print(prices.keys())
print(prices.values())
prices["amount"] = 1
prices["seller"] = "mary"
prices["buyer"] = "safwan"
prices["price"] = 20
print(prices)
del prices["seller"] 
print(prices)

