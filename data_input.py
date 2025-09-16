def input_product():
    products = {}
    while True:
        name = input("Введіть назву товару або 'stop' щоб закінчити: ")
        if name.lower() == 'stop':
            break
        try:
            price = float(input(f"Введіть ціну для {name}: "))
            stock = int(input(f"Введіть кількість {name}: "))
            products[name] = {'Ціна': price, 'Залишок': stock}
        except ValueError:
            print("Помилка вводу! Спробуйте ще раз.")
    return products
