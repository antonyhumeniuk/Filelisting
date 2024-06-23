#now cloned to GIT


# now copied back from the master

import os

path = ("C:\\Users\\anton\\Documents")
ListOfDirs=[]
os.chdir (path)
print(path)

def DirectoryList():
    for root, dirs, files in os.walk("."):
        for name in files:
            print(" "*10,os.path.join(root, name))
        for name in dirs:
            print(os.path.join(root, name))
            #print(os.path.join(str(root),str(files)))

        #for name in dirs:
         #   docs=(os.path.join(root, name))
          #  print(docs)
           # ListOfDirs.append(docs)

DirectoryList()
