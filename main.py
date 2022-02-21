import csv
import operator


def read_csv(file_name):
    """Reads a csv file and returns a list of lists."""
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        return list(reader)


def get_candidates_raw(data):
    """Returns a list of candidates."""
    return [str(datum[4]).lower() for datum in data[1:]]


def remove_accents(data: list):
    """Removes accents."""
    data_list = [
        normalize(datum).upper().strip()
        for datum in data
    ]
    return data_list


def normalize(text: str):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        text = text.replace(a, b).replace(a.upper(), b.upper())
    return text


def create_candidates_dict(candidates):
    """Returns a dictionary with candidates as keys and a\
        list of votes as values."""
    candidates_dict = {}
    for candidate in candidates:
        candidates_dict[candidate] = candidates_dict.get(candidate, 0) + 1

    list_name = [
        ["GUSTAVO PETRO", "PETRO", "GUSTABO PETRO", "GUSTAVO"],
        ["RODOLFO HERNANDEZ", "RODOLFO", "RODOLFO HERNANDES", "HERNANDES"],
        ["FRANCIA MARQUEZ", "FRANCIA", "FRANCIA MARQUES", "MARQUES"],
        ["ALEX CHAR", "ALEX", "CHAR", "ALE CHAR"],
        ["SERGIO FAJARDO", "SERGIO", "SERGIO FAGARDO", "SERJIO"],
        ["FEDERICO GUTIERREZ", "FEDERICO", "FEDERICO GUTIERRES",
         "GUTIERRES", "GUTIERREZ"]
    ]
    for names in list_name:
        for name in names[1:]:
            candidates_dict[names[0]] += candidates_dict.get(name, 0)
            candidates_dict.pop(name, None)

    return candidates_dict


def clean_candidates(candidates: list):
    """Removes bad candidates from the list.
    """
    candidates = candidates[8:]
    return candidates


def sort_dict(data: dict):
    sorted_dict = sorted(
        data.items(),
        key=operator.itemgetter(1),
        reverse=True
    )
    return sorted_dict


if __name__ == "__main__":
    data = read_csv("data.csv")
    candidates = get_candidates_raw(data)
    candidates = remove_accents(candidates)
    candidates.sort()
    candidates = clean_candidates(candidates)
    candidates_dict = create_candidates_dict(candidates)
    print(sort_dict(candidates_dict)[:10])
