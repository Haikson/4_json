import json


def load_data(filepath):
    with open(filepath) as infile:
        json_data = json.load(infile)
    return json_data


def pretty_print_json(json_data):
    print(json.dumps(json_data, indent=4))


if __name__ == '__main__':
    pretty_print_json(load_data("data.json"))
