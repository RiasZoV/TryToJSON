import json


def read_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def read_info_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.readlines()
    return data


def extract_needed_data(info_data, params):
    extracted_data = {}
    param_keys = set()
    for category in params.values():
        param_keys.update(category.keys())

    current_key = None
    current_values = []

    for line in info_data:
        line = line.strip()
        if not line:
            continue

        if line in param_keys:
            if current_key and current_values:
                extracted_data[current_key] = current_values
            current_key = line
            current_values = []
        else:
            current_values.append(line)

    if current_key and current_values:
        extracted_data[current_key] = current_values

    return extracted_data

def main():
        params = read_json_file('Type_param.json')
        info_data = read_info_file('param1.info')
        needed_data = extract_needed_data(info_data, params)
        return needed_data


if __name__ == "__main__":
    result = main()
    print(json.dumps(result, indent=4, ensure_ascii=False))



