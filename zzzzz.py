import json


def read_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def read_info_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file if line.strip()]


def extract_needed_data(info_data, params):
    extracted_data = {}
    param_keys = {key: (category, count)
                  for category, keys in params.items()
                  for key, count in keys.items()}

    current_key, current_values = None, []

    for line in info_data:
        if line in param_keys:
            if current_key:
                category, count = param_keys[current_key]
                extracted_data.setdefault(category, {})[current_key] = current_values[:count]
            current_key, current_values = line, []
        elif current_key:
            current_values.append(line)

    if current_key:
        category, count = param_keys[current_key]
        extracted_data.setdefault(category, {})[current_key] = current_values[:count]

    for category, keys in params.items():
        for key in keys:
            if key not in extracted_data.get(category, {}):
                extracted_data.setdefault(category, {})[key] = []

    return extracted_data

def main():
    try:
        params = read_json_file('Type_param.json')
        info_data = read_info_file('param1.info')
        return extract_needed_data(info_data, params)
    except FileNotFoundError:
        return {'Файл не найден.'}
    except json.JSONDecodeError:
        return {'Некорректные данные в json-файле.'}


if __name__ == "__main__":
    result = main()
    print(result)

