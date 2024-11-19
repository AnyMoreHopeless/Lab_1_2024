import json


def calculate_weighted_score(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    total_sum = sum(item['score'] * item['weight'] for item in data)
    return round(total_sum, 3)


if __name__ == "__main__":
    result = calculate_weighted_score("input.json")
    print(result)
