def calculate_stock_value(product_info):
    for product, details in product_info.items():
        stock_value = details['Ціна'] * details['Залишок']
        print(f"Вартість залишку для {product}: {stock_value:.2f} грн")


def calculate_discount(product_info):
    for product, details in product_info.items():
        if details['Залишок'] < 10:
            discount = details['Ціна'] * 0.05
            print(f"Знижка для {product}: {discount:.2f} грн (5%)")
        else:
            print(f"Для {product} знижка не застосовується (залишок: {details['Залишок']})")
