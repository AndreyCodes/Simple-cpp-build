import os
import time
import psutil
import subprocess

path = os.getcwd()
compilerPath = "C:\Program Files\mingw-w64\mingw64\\bin" #захардкожено под мой пк
compilersNames = set()
sourcesNames = []

with os.scandir(compilerPath) as listOfEntries:  
    for entry in listOfEntries:
        #сбор имен компиляторов
        if entry.is_file():
            compilersNames.add(str(entry.name))

with os.scandir(path) as listOfEntries:  
    for entry in listOfEntries:
        #Сбор имен исходных файлов cpp
        if entry.is_file():
            if(entry.name.endswith(".cpp")):
                sourcesNames.append(str(entry.name))

#билдим объектники
commandToMakeObjFiles = "g++ -c "
for name in sourcesNames:
    commandToMakeObjFiles+=name+" "
CompilatorProcess_1 = subprocess.Popen(commandToMakeObjFiles)
#

#пока работает компилятор ждем
CompilatorProcess_1.wait()
#time.sleep(10)

#составление списка объектных файлов
objNames = []
with os.scandir(path) as listOfEntries:  
    for entry in listOfEntries:
        if entry.is_file():
            if(entry.name.endswith(".o")):
                objNames.append(str(entry.name))

#/составление списка объектных файлов
print(objNames)
if(len(objNames) != len(sourcesNames)):
    print("compiling failed")
    os.system("pause")
    exit()

#Составление команды
print("enter the name of program")
nameOfRes = input()
command = "g++ "
for name in objNames:
    command+=(name+" ")
command+="-o " + nameOfRes+".exe"
#/составление команды


isHavingRes = False #Есть ли результат компиляции

CompilatorProcess_1 = subprocess.Popen(command) #линковка
#пока работает компилятор - ждем
CompilatorProcess_1.wait()

#проверка наличия результата
with os.scandir(path) as listOfEntries:
    for entry in listOfEntries:
        if entry.is_file():
            if(entry.name == (nameOfRes+".exe")):
                isHavingRes = True

if(not isHavingRes):
    print("linking unsucced!")
    os.system("pause")
    exit()

print("RESULT IS OK")
os.system("pause")