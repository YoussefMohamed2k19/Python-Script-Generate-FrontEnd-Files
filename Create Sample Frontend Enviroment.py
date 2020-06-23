import os
import emoji

while True:             # Loop continuously
  projectName=str(input("Enter The Project Name: "))
  # Get the input
  if not os.path.exists(projectName):
    os.mkdir(projectName)
    print ("\n" + "Your Project Folder Was Created..." + "\n")
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
str = """<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <link rel="stylesheet" href="Css/style.css">
    <title>Hello, world!</title>
  </head>
  <body>
    <h1>Hello, world!</h1>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
    <script src="Js/script.js" type="text/javascript"></script>
  </body>
</html>"""
open(filename[0],"w").write(str)

os.chdir("./Css")
open(filename[1], 'w').close()

os.chdir("../Js")
open(filename[2], 'w').close()

# 🎉 Finished msg 🎉 
print("\n" + emoji.emojize('Done:tada:!', use_aliases=True))

os.system("pause")
