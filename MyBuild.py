import os
import time
import psutil
import subprocess

path = os.getcwd()
sourcesNames = []


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