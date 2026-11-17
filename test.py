product = {'uzum' : 5000, 'anor' : 4000, 'olma' : 8000}
selles = {'uzum' : 4, 'anor' : 6, 'olma' : 3}

for name, product_price in product.items():
    for product_qty in selles.values():
        res = product_price * product_qty
    print(res)