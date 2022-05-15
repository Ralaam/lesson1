from pprint import pprint


product = {
    "name": "iPhone 12",
    "stock": 24,
    "price": 65432.1
}
phones = ['iPhone 12 PRO', 'Samsung', 'Xiaomi']

product['recomended'] = phones
pprint(product)

product['recomended'].append('Iphone 9')
pprint(product)

