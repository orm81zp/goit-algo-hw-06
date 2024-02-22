import sys
import random

from algorithms import binary_upper_limit_search


def parse_arguments():
    """Парсить аргументи командного рядка"""

    x = [3.5, 4, 6.0]
    arr = [1.1, 1.3, 2.5, 3.8, 4.6, 5.9]

    if len(sys.argv) > 2:
        try:
            arr = [float(x) for x in sys.argv[1].split(",")]
            x = [float(x) for x in sys.argv[2].split(",")]
        except Exception as _:
            print("Сталася біда, під час парсінгу аргументів командного рядка")
            print("Дані мають розділятися комою, наприклад: 1.1,1.3,2.5 3.5,4,6.0")

    return arr, x


def run_test():
    arr, x = parse_arguments()

    # Вивід статистичних даних
    print(f"Набір даних: {arr}")
    print(f"Набір пошукових значень: {x}")
    print()

    print("{: <17} | {: <10}".format("Пошукове значення", "Результат"))
    for xi in x:
        result = binary_upper_limit_search(arr, xi)
        print("{: <17} | {: <10}".format(xi, str(result)))


def main():
    run_test()


if __name__ == "__main__":
    main()
