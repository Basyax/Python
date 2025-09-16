from data_input import input_product
from calculations import calculate_stock_value, calculate_discount
from general import print_product_names, find_product_by_name


def main():
    products = input_product()
    print("\n--- Усі товари ---")
    print(products)

    print("\n--- Розрахунок вартості залишків ---")
    calculate_stock_value(products)

    print("\n--- Розрахунок знижок ---")
    calculate_discount(products)

    print("\n--- Список товарів ---")
    product_names = list(products.keys())
    print_product_names(product_names)

    print("\n--- Пошук товару ---")
    search_name = input("Введіть назву товару для пошуку: ")
    find_product_by_name(products, search_name)


if __name__ == "__main__":
    main()
