import csv

ui_path = 'widgets/info.ui'
picture_dir_path = 'widgets/pictures_of_elements'
csv_path = 'widgets/info.csv'

island_style = "background-color: rgb(100, 100, 100); border-radius: 20px;"


def open_csv_file(index: int):
    with open(csv_path, encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        return list(reader)[index]


def window_name_convert(name: str):
    return f"{name}_info"


def weight_convert(weight: str):
    return f"{float(weight)} гр/моль"


def group_convert(pos_y: int):
    if pos_y == 9:
        return 6
    if pos_y == 10:
        return 7
    return pos_y


def oxidation_convert(text: str):
    if text == "unexpected":
        return "-"
    return text


def date_covert(date: str):
    date = int(date)
    if date < 0:
        return f"{abs(date)} г. до н.э."
    return f"{date} г."


def temperature_convert(ch: str):
    if ch == "unexpected":
        return "-"
    return f"{float(ch)}°K"


def density_convert(ch: str):
    if ch == "unexpected":
        return "-"
    return f"{float(ch)} гр/м3"
