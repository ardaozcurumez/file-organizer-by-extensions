import os 

def organize():
    
    folder = input("Enter your folder path: ")
    files = list()
    exts = list()
    
    def list_dir():

        for file in os.listdir(folder):

            if os.path.isdir(os.path.join(folder,file)):
                continue
            elif file.startswith("."):
                continue
            else:
                files.append(file)
    
    list_dir()

    for file in files:                   

        ext = file.split(".")[-1]

        if ext in exts:
            continue
        else:
            exts.append(ext)

    for ext in exts:

        if os.path.isdir(os.path.join(folder,ext)):
            continue

        else:
            os.mkdir(os.path.join(folder,ext))    

    for file in files:

        ext = file.split(".")[-1]

        os.rename(os.path.join(folder,file),os.path.join(folder,ext,file))

if __name__ == "__main__":
    organize()


               
