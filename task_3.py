"""Модуль порівняння алгоритмів пошуку"""

import sys
import timeit

from algorithms import boyer_moore_search, kmp_search, rabin_karp_search

algorithms = [
    {"name": "Алгоритм Боєра-Мура", "func": boyer_moore_search},
    {"name": "Алгоритм Рабіна-Карпа", "func": rabin_karp_search},
    {"name": "Алгоритм Кнута-Морріса-Пратта", "func": kmp_search},
]

def parse_arguments():
    """Парсить аргументи командного рядка"""

    search_pattern = "структури даних вже давно реалізовані"

    if len(sys.argv) > 1:
        search_pattern = " ".join(sys.argv[1:])

    return search_pattern


def run_tests():
    """Запускає тестування алгоритмів"""

    search_pattern = parse_arguments()
    # набір статей для пошуку
    articles = ["article1.txt", "article2.txt"]
    # підготовка масиву для заповнення результатами
    algorithms_result = [0.0] * len(algorithms)
    # кількість тестів
    attempts = 10

    for _ in range(attempts):
        for index, algorithm in enumerate(algorithms):
            for article in articles:
                with open(f"./assets/{article}", "r", encoding="utf-8") as hf:
                    # зчитати зміст файлу
                    text = hf.read()
                    # виконання певного алгоритму із збереженням часу його виконання
                    algorithms_result[index] += timeit.timeit(
                        lambda: algorithm["func"](text, search_pattern), number=1
                    )

    # Вивід статистичних даних
    print(f"Кількість спроб: {attempts}")
    print(f"Набори даних: {articles}")
    print(f'Пошуковий підрядок: "{search_pattern}"')

    print("\n✓ Середній час:")
    for index, algorithm in enumerate(algorithms):
        print(f"{algorithm["name"]}: {algorithms_result[index]/attempts:.6f}")

    # знаходимо алгоритм з найменшим часов виконання (найшвидший)
    index_evaluation_result = algorithms_result.index(min(algorithms_result))
    evaluation_algorithm = algorithms[index_evaluation_result]
    evaluation_result = algorithms_result[index_evaluation_result]

    print(f"\n✓ Найшвидший алгоритм: {evaluation_algorithm["name"]}")

    for index, algorithm in enumerate(algorithms):
        # опрацьовуємо лише алгоритми для порівняння
        if algorithm["name"] != evaluation_algorithm["name"]:
            if evaluation_result < algorithms_result[index]:
                ratio = algorithms_result[index] / evaluation_result
                print(
                    f"{evaluation_algorithm["name"]} працює у {ratio:.1f} разів швидше ніж {algorithm["name"]}."
                )
            elif evaluation_result > algorithms_result[index]:
                ratio = evaluation_result / algorithms_result[index]
                print(
                    f"{evaluation_algorithm["name"]} працює у {ratio:.1f} разів повільніше ніж {algorithm["name"]}."
                )
            else:
                print(
                    f"{evaluation_algorithm["name"]} працює однаково з {algorithm["name"]}."
                )


def main():
    run_tests()


if __name__ == "__main__":
    main()
