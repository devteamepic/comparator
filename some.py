import csv
import glob, os
import numpy as np

arr = []
fileArr = []
counter = 0

with open('./data.csv') as dataFile:
    csvReader = csv.reader(dataFile, delimiter = ";")
    for row in csvReader:
        arr.append(row)

del arr[0]
os.chdir("./files")
for file in glob.glob("*.pdf"):
    fileArr.append(file)

arr = np.array(arr)
fileArr = np.array(fileArr)

fileArr = fileArr[fileArr.argsort(kind="heapsort")]
arr = arr[arr[:,3].argsort(kind="heapsort")]
for a in arr:
    print(counter)
    print("1" + fileArr[counter])
    print("2" + a[3])
#    if (fileArr[counter] == a[3]):
#        print("number: " + str(counter) + " exists")
#    else:
#        print("WARNING, number: " + str(counter) + " DOES NOT EXIST, Name is: " + a[3])
    counter = counter + 1