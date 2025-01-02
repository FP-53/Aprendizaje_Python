def enter_products():
    products = {}
    buying = True
    while buying == True: 
        more_products= input('Quiere seguir comprando? A para seguir Q para parar: ')
        if more_products == 'A':
            buying= True
            item = input('Introduzca el producto: ')
            quantity = int(input('Introduzca la cantidad: '))
            products.update({item:quantity})
        elif more_products == 'Q':
            buying = False
        elif more_products != 'True' or more_products != 'False':
            print('Por favor elija una funcion valida, recuerde usar las mayusculas')
            buying = True
    return products

def get_price(product, quantity):
    price_data = {
        'Leche' : 3, 
        'Queso' : 4, 
        'Mantequilla' : 5,
        'Pollo': 7,
        'Cerdo' : 9,
        'Pescado' : 12,
        'Pan' : 5,
    }

    total = price_data[product]*quantity
    print(product+':$'+str(price_data[product])+'x'+str(quantity)+'='+str(total))
    return total

def get_discount(total, member_type): 
    discount = 0
    if total >= 25: 
        if member_type == 'Gold': 
            total = total * 0.80 
            discount = 20
        elif member_type == 'Silver':
            total = total * 0.90
            discount = 10
        elif member_type == 'Bronze':
            total = total * 0.95
            discount = 5
        print(str(discount)+'% por'+member_type+''+'membresia por un total de: $'+str(total))
    else: 
        print('No tiene descuento ya que es una compra igual o menor a $25')
    return total

def crear_factura(products,member_type): 
    total= 0
    for key,value in products.items():
        total += get_price(key, value)
    total = get_discount(total,member_type)
    print('El descuento es $' + str(total))

products = enter_products()
member_type = input('Elija una membresia. Gold , Siler o Bronze: ')
crear_factura(products, member_type)

