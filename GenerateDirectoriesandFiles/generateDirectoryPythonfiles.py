import os
path = "C:/Users/swath/PycharmProjects/NamasthePythonPractice"
dirName = input("enter the name of the directory to be created: ")
path += f"/{dirName}"
def createDirectory():
    try:
        os.mkdir(path)
        print(f"{dirName} folder was created")
    except:
        print(f"{dirName} folder already exists")
def createPythonFilesInDirectory():
    try:
        for i in range(1,11):
            fileName= path+f"/{dirName}q{i}.py"
            print(fileName)
            #os.mkdir(fileName)
            with open(fileName,'w') as f:
                pass
        print("Python files generated for questions")
    except:
        print("there has been some error")

createDirectory()
createPythonFilesInDirectory()