#Goal: Using obj oriented programming and testing, build a program to read elevation data
#draw an elevation map as a .png file
#chart the best path across the map

from PIL import Image
img = Image.open("samples/map_alone.png")
img.rotate(45).show()


with open("elevation_small.txt") as text_file:
    keelylist = []
    for line in text_file.readlines():
        for item in line:
            keelylist.append([int(item) for item in line.strip().split()])
        print(keelylist)
        