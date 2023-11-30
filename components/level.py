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
                y = int(row['y'].strip())
                width = int(row['width'].strip())
                height = int(row['height'].strip())
                image_path = row.get('image_path', '')  # Add a new column 'image_path' to your CSV file
                scale = float(row.get('scale', '1.0'))  # Add a new column 'scale' to your CSV file, default is 1.0
                self.platforms.append(Platform(x, y, width, height, image_path, scale))

    def get_platforms(self):
        return self.platforms
