# components/level.py
import csv
from components.platform import Platform

class Level:
    def __init__(self, level_file):
        self.platforms = []
        self.load_level(level_file)

    def load_level(self, level_file):
        with open(level_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                x = int(row['x'])
                y = int(row[' y'].strip())  # Remove leading/trailing spaces
                width = int(row[' width'].strip())
                height = int(row[' height'].strip())
                color_values = [int(val.strip()) for val in row.get('color', '0,255,0').split(',')]
                color = tuple(color_values[:3])  # Take the first three values (RGB)

                print(color)  # Add this line to inspect the color
                self.platforms.append(Platform(x, y, width, height, color))

    def get_platforms(self):
        return self.platforms
