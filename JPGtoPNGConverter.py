from sys import argv
from os import getcwd, path, mkdir, listdir
from PIL import Image

originalFolder = argv[1]
newFolder = argv[2]

cwd = getcwd() + "\\"

if (path.exists(cwd + newFolder)):
    pass
else:
    mkdir(cwd + newFolder)

numberOfImages = len(listdir(cwd + originalFolder))

picsIndex = listdir(cwd + originalFolder)
for i in range(numberOfImages):
    img = Image.open(cwd + originalFolder + "\\" + picsIndex[i])
    img.save(path.splitext(cwd + newFolder + "\\" + picsIndex[i])[0] + ".png")
