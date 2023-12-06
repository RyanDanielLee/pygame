# components/level.py
import csv
from components.platform import Platform, EndPlatform

class Level:
    def __init__(self, level_file):
        # List of platforms
        self.platforms = []
        self.load_level(level_file)

    def load_level(self, level_file):
        # Load level from csv file
        # In the format of x, y, width, height, image_path, type
        with open(level_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                x = int(row['x'])
                y = int(row['y'].strip())
                width = int(row['width'].strip())
                height = int(row['height'].strip())
                image_path = row.get('image_path', '')
                # Check if platform is an "end" platform or a regular platform
                if row.get('type') == 'end':
                    # Add platform to EndPlatforms if it is type of end
                    self.platforms.append(EndPlatform(x, y, width, height, image_path)) 
                else:
                    # Add platform to Platforms (regular platforms) if it is a regular platform
                    self.platforms.append(Platform(x, y, width, height, image_path)) 

    def get_platforms(self):
        return self.platforms