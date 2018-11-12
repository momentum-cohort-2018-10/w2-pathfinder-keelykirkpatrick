# from PIL import Image
# im = Image.open("samples/map_with_path.png")
# im.rotate(45).show()

with open("elevation_small.txt") as text_file:
    keelylist = []
    for line in text_file.readlines():
        for item in line:
            keelylist.append([int(item) for item in line.strip().split()])
            print(keelylist)


