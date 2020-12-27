from __future__ import absolute_import
import json
import demjson
from colorama import Fore, Back, Style
from prettytable import PrettyTable
import os


class Sequence:
    def __init__(self):
        self.list_path = "./datasets/list.json"

    def get_sequence(self, name):
        with open(self.list_path, encoding="utf-8") as f:
            sequences = json.load(f)
            return sequences[name]

    def get_sequences(self):
        with open(self.list_path, encoding="utf-8") as f:
            return json.load(f)

    def check_sequences(self):
        sequences = self.get_sequences()
        tb = PrettyTable()
        tb.field_names = ["Exist", "Name", "Path"]
        for (key, value) in sequences.items():
            if os.path.exists(value['path']):
                tb.add_row(["Found", key, value['path']])
            else:
                tb.add_row([Fore.RED + "Not Found" + Fore.RESET, key, value['path']])
        print(tb)
