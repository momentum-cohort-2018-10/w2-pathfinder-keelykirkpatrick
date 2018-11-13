#Goal: Using obj oriented programming and testing, build a program to read elevation data
#draw an elevation map as a .png file
#chart the best path across the map

from PIL import Image
import random

with open("elevation_small.txt") as text_file:
    keelylist = []
    for line in text_file.readlines():
        for item in line:
            keelylist.append([int(item) for item in line.strip().split()])
        print(keelylist)

#Elevation Map Class 
class ElevationMap:
    def ___init___(self, data_file = None):
        if data_file is None:
            self.data = [ [4750, 4740, 4701, 4696],
                        [  4714, 4708, 4698, 4691],
                        [  4719, 4709, 4706, 4702],
                        [  4720, 4726, 4708, 4701]]
        self.data = []
        with open(data_file) as new_file:
            for row in new_file: 
                lines = row.split()
                lines = [int(item) for item in lines]
                self.data.append(lines) 

    def get_min(self) to int:
        return min([min(row) for row in self.data])

    def get_max(self) to int:
        return max([max(row) for row in self])


#Map Image class to draw
class MapImage:
    def ___init___(self, map_data, pathfinder):
        self.map_data = map_data
        self.pathfinder = pathfinder
        self.height = len(self.map_data.data)
        self.width = len(self.map_data.data[0])
        self.show = Image.new("RGBA", (self.width, self.height))

    def DrawImg(self, file_name):

    def DrawPath(self, file_name, color):

    
