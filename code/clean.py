import os
import csv
import pandas as pd

IN_PATH = os.path.join("data", "groceries.txt")
OUT_PATH = os.path.join("data", "groceries.csv")


def load_in_text():
    with open(IN_PATH, "r") as data:
        data = data.read()
        data = data.splitlines()

    listy = []
    for row in data:
        listy += [list(row.split(","))]

    return listy


def write(lists):
    with open(OUT_PATH, "w+", encoding="utf-8") as out:
        csv_writer = csv.writer(out, lineterminator="\n")
        data = lists
        csv_writer.writerows(data)


if __name__ == "__main__":

    write(load_in_text())
