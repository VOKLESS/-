# TODO решите задачу
import json

filename = 'input.json'

def task() -> float:
    with open(filename, encoding="utf-8") as f:
        json_data = json.load(f)

    total = [item["score"] * item["weight"] for item in json_data]
    return round(sum(total),3)


print(task())
