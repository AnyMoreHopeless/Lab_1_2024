import csv
import json


def csv_to_json(csv_file_path, json_file_path):

    with open(csv_file_path, mode='r', newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        data = [row for row in csv_reader]

    with open(json_file_path, mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)


csv_to_json('input.csv', 'output.json')
