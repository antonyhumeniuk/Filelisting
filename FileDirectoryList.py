import os

path=("C:\\Users\\Antony\\Documents")
ListOfDirs=[]
os.chdir(path)
print(path)

def DirectoryList():
    for root, dirs, files in os.walk("."):
        for name in files:
            print(" "*10,os.path.join(root, name))
        #for name in dirs:
            #print(os.path.join(root, name))
            #print(os.path.join(str(root),str(files)))

        #for name in dirs:
         #   docs=(os.path.join(root, name))
          #  print(docs)
           # ListOfDirs.append(docs)

DirectoryList()








            
            #FilesInDirectory(docs)
            #print (ListOfDirs)
            #for name in files:
            #print(os.path.join(dirs,name))
            #for dirs in root:
            #temppath=os.path.join(root, dirs)
            #os.chdir(os.path.join(root, dirs ))
            #print("**********",temppath,"*****'*******")
            #usingdirlist(path)
            #for name in dirs:
            #print(os.path.join(temppath,name))
            #print(" "*10,name)
              




#for i in range(len(ListOfDirs)):
    #print(ListOfDirs[i])
    #os.chdir(ListOfDirs[i]))
    #onlyfiles = [f for f in ListOfDirs(os.path(i)) if isfile(join(i, f))]

    #onlyfiles
    
    


