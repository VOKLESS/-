# TODO импортировать необходимые молули
import csv
import json
from textwrap import indent

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    # TODO считать содержимое csv файла

    with open(INPUT_FILENAME,"r", encoding="utf-8") as csv_file:
        input_data = csv.DictReader(csv_file)
        new_data = [item for item in input_data]

    # TODO Сериализовать в файл с отступами равными 4

    with open(OUTPUT_FILENAME,"w", encoding="utf-8") as json_file:
        json.dump(new_data, json_file, indent=4, ensure_ascii=False)

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
