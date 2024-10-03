# Функция для пользовательского интерфейса
from string_module import is_palindrome
from string_module import count_vowels
from string_module import reverse_string
from string_module import count_words
from string_module import corrected_function

def main():
    print("Добро пожаловать в программу для работы со строками!")
    print("Вы можете выбрать одну из следующих функций:")
    print("1. Проверить, является ли строка палиндромом.")
    print("2. Подсчитать количество гласных букв в строке.")
    print("3. Перевернуть строку.")
    print("4. Подсчитать количество слов в строке.")
    print("5. Получить индекс последнего символа строки.")
    print("Введите 'exit' для выхода из программы.")

    while True:
        user_input = input("\nВведите текст: ")
        if user_input.lower() == 'exit':
            print("Выход из программы. До свидания!")
            break

        try:
            print("\nВыберите номер функции, которую хотите выполнить:")
            option = int(input("Введите номер функции (1-5): "))

            if option == 1:
                print(f"Проверка палиндрома: {'Да' if is_palindrome(user_input) else 'Нет'}")
            elif option == 2:
                print(f"Количество гласных в строке: {count_vowels(user_input)}")
            elif option == 3:
                print(f"Перевернутая строка: {reverse_string(user_input)}")
            elif option == 4:
                print(f"Количество слов в строке: {count_words(user_input)}")
            elif option == 5:
                index = corrected_function(user_input)
                print(f"Индекс последнего символа: {index}" if index >= 0 else "Строка пуста.")
            else:
                print("Неверный номер функции. Пожалуйста, выберите номер от 1 до 5.")
        except ValueError:
            print("Пожалуйста, введите корректный номер функции.")
            
if __name__ == "__main__":
    main()