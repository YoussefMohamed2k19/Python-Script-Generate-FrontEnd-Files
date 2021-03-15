import os
import emoji

while True:             # Loop continuously
  projectName=str(input("Enter The Project Name: "))
  # Get the input
  if not os.path.exists(projectName):
    os.mkdir(projectName)
    print ("\n" + "Your Project Folder Was Creating..." + "\n")
    break
  else:
    print ("\n" + "This Project Name Already Used, Try Again!"+ "\n")
    pass   

# Navigate to Project Folder to Make new files
os.chdir("./"+ projectName )

# Create target Directory if don't exist
dirName = ['Css','Js', 'Img']
for string in dirName:
    if not os.path.exists(string):
        os.mkdir(string)
        print (string + " Folder Created...")
    else:
        print ("Sorry" + string +" Exist!")

# Create target files if don't exist
filename = ['index.html', 'style.css', 'script.js']

open(filename[0], 'w').close()

# Bootstrap start template
str= """<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">
    <link rel="stylesheet" href="Css/style.css">
    <title>Hello, world!</title>
  </head>
  <body>
    <h1>Hello, world!</h1>

    <!-- Optional JavaScript; choose one of the two! -->

    <!-- Option 1: Bootstrap Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/js/bootstrap.bundle.min.js" integrity="sha384-b5kHyXgcpbZJO/tY9Ul7kGkf1S0CWuKcCD38l8YkeH8z8QjE0GmW1gYU5S9FOnJ0" crossorigin="anonymous"></script>
    <script src="Js/script.js" type="text/javascript"></script>
    <!-- Option 2: Separate Popper and Bootstrap JS -->
    <!--
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.6.0/dist/umd/popper.min.js" integrity="sha384-KsvD1yqQ1/1+IA7gi3P0tyJcT3vR+NdBTt13hSJ2lnve8agRGXTTyNaBYmCR/Nwi" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/js/bootstrap.min.js" integrity="sha384-nsg8ua9HAw1y0W1btsyWgBklPnCUAFLuTMS2G72MMONqmOymq585AcH49TLBQObG" crossorigin="anonymous"></script>
    -->
  </body>
</html>"""

open(filename[0],"w").write(str)

os.chdir("./Css")
open(filename[1], 'w').close()

os.chdir("../Js")
open(filename[2], 'w').close()

# 🎉 Finished msg 🎉
# -*- coding: UTF-8 -*- 
print("\n" + emoji.emojize('Done!🎉🎉', use_aliases=True))
os.system("pause")
