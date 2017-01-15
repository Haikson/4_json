import json


def load_data(filepath):
    with open(filepath) as infile:
        data = json.load(infile)
    return data


def pretty_print_json(data):
    print(json.dumps(data, indent=4))


if __name__ == '__main__':
    pretty_print_json(load_data("data.json"))
