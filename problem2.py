def find_top_seller(products: dict, sales: dict) -> str:
    
    res = {name: price * sales[name] for name, price in products.items()}

    return max(res, key=res.get)

        



print(find_top_seller({"Olma": 5000, "Banan": 8000, "Uzum": 7000}, {"Olma": 10,   "Banan": 5,    "Uzum": 8}))