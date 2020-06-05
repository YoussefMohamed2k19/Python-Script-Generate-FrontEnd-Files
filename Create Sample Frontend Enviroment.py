import os

# Create target Directory if don't exist
dirName = ['css','js', 'img']

for string in dirName:
    if not os.path.exists(string):
        os.mkdir(string)
        print (string + " Created")
    else:
        print (string +" Exist")

# Create target files if don't exist
filename = ['index.html', 'style.css', 'script.js']
open(filename[0], 'w').close()

os.chdir("./css")
open(filename[1], 'w').close()

os.chdir("../js")
open(filename[2], 'w').close()