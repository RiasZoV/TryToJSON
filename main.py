import json


def read_json(json_file):
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def read_info(info_file, key, num_lines):
    result = []
    with open(info_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    i = 0
    while i < len(lines):
        current_key = lines[i].strip()
        if current_key == key:
            for j in range(1, num_lines + 1):
                if i + j < len(lines):
                    result.append(lines[i + j].strip())
            break
        i += 1

    return result


def main():
    json_file = 'Type_param.json'
    info_file = 'param1.info'

    params = read_json(json_file)

    results = {}

    category_list = list(params.keys())

    while True:
        print("\nДоступные категории:")
        for i, category in enumerate(category_list, 1):
            print(f"{i} - {category}")

        try:
            selected_category_num = input("\nВведите номер выбранной категории (или 'стоп' для завершения): ").strip()
            if selected_category_num.lower() == 'стоп':
                break

            if not selected_category_num.isdigit() or not (1 <= int(selected_category_num) <= len(category_list)):
                print("Ошибка: выбранный номер категории отсутствует в списке.")
                continue

            selected_category = category_list[int(selected_category_num) - 1]
        except KeyboardInterrupt:
            print("\nПрограмма завершена пользователем.")
            return

        print(f"\nДоступные ключи в категории '{selected_category}':")
        for key, max_lines in params[selected_category].items():
            print(f"{key} (максимум {max_lines} строк)")

        while True:
            try:
                selected_key = input("\nВведите выбранный ключ (или 'назад' для выбора другой категории): ").strip()
                if selected_key.lower() == 'назад':
                    break

                if selected_key not in params[selected_category]:
                    print("Ошибка: выбранный ключ отсутствует в категории.")
                    continue

                max_lines = params[selected_category][selected_key]

                while True:
                    try:
                        num_lines = int(
                            input(f"Введите количество строк для ключа '{selected_key}' (максимум {max_lines}): "))
                        if 0 <= num_lines <= max_lines:
                            break
                        else:
                            print(f"Пожалуйста, введите число от 0 до {max_lines}.")
                    except ValueError:
                        print("Пожалуйста, введите корректное число.")

                if selected_key in results:
                    results[selected_key].extend(read_info(info_file, selected_key, num_lines))
                else:
                    results[selected_key] = read_info(info_file, selected_key, num_lines)
            except KeyboardInterrupt:
                print("\nПрограмма завершена пользователем.")
                return

    for k, v in results.items():
        print(f"{k}:")
        for line in v:
            print(line)
        print()  # Добавляем пустую строку для разделения ключей


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nПрограмма завершена пользователем.")
