import os
import time
import psutil

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
for name in sourcesNames:
    os.popen("g++ -c " + name + " -o " + name.replace(".cpp",".o",1))

#пока работает компилятор ждем
Working = True
processNames = set()
while Working:
    for proc in psutil.process_iter():
        processNames.add(str(proc.name()))
    if(len(processNames.intersection(compilersNames))== 0):
        Working = False
    else:
        time.sleep(2)
        processNames.clear()
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
os.popen(command) #линковка

#пока работает компилятор - ждем
Working = True
processNames = set()
while Working:
    for proc in psutil.process_iter():
        processNames.add(str(proc.name()))
    if(len(processNames.intersection(compilersNames))== 0):
        Working = False
    else:
        time.sleep(2)
        processNames.clear()
#time.sleep(5)

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