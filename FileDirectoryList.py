#now cloned to GIT


# now copied back from the master

import os
listing_path: str=input("which path do you want...,\n")
#print(""\n"")


path = (listing_path)
ListOfDirs=[]
os.chdir (path)
print(path)

def DirectoryList():
    for root, dirs, files in os.walk("."):
        for name in files:
            #print(" "*10,os.path.join(root, name))
            print(name)
        for name in dirs:
            print(os.path.join(root, dirs))
            #print(os.path.join(str(root),str(files)))

        #for name in dirs:
         #   docs=(os.path.join(root, name))
          #  print(docs)
           # ListOfDirs.append(docs)

DirectoryList()
