product = {
    "ноутбук msi": {
        "цена": 120000,
        "количество": 66,
        "категория": "техника"
    },

    "клавиатура dell": {
        "цена": 1500,
        "количество": 100,
        "категория": "техника"
    },
    
    "apple watch": {
        "цена": 35000,
        "количество": 27,
        "категория": "часы"
    },

    "наушники razer": {
        "цена": 2500,
        "количество": 156,
        "категория": "наушники"
    },
    "колонка JBL":{
        "цена": 10000,
        "количество": 120,
        "категория": "гарнитура"
    }
}  


money = int(0)
def wealth(product_dict: dict):
    for kind, box in product_dict.items():
        print("-"*70)
        print(f"Товар {kind!r}")
        print("-"*70)
        for asset, pages in box.items():
            print(f" {asset} - {pages} ")

def purchases(product_dict : dict):
    products = input("Введите название товара: ")
    global money
    for znac in product_dict.values():
        if products in product:
            money = money + product_dict[products]['цена']
            product_dict[products]['количество'] = product_dict[products]['количество'] - 1
            print(product_dict[products]['количество'])
            return product_dict[products]['количество']
def spisok():
    name =''
    koli = ''
    www= {:}
    while True:
        name = input("Введите название товара: ")
        if name == " ":
            break
        koli = input("Введите количество товара: ")
        www[name] = koli
    
    dict_to_buy = {''

    
if __name__ == '__main__':
    #wealth(product)
    #purchases (product)
    #spisok()
   
   
