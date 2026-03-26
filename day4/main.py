products = ["rice", "sugar", "milk", "oil", "salt", "wheat", "eggs", "bread", "Tea powder", "coffee powder"]
prices =[60, 45, 25, 120, 20, 50, 6, 35, 150, 180]
print("Index  product     price")
for i,(product, price) in enumerate(zip(products, prices),start=1):
    print(i,  "  ", product,  "       ₹",    price)
