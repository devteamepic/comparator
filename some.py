# -*- coding: utf-8 -*-
import csv
import glob, os
import numpy as np


def remove_from_csv(item):
    with open('../data.csv', 'rb', ) as inpt, open('../data_converted.csv', 'wb') as out:
        writer = csv.writer(out, delimiter=';')
        for row in csv.reader(inpt, delimiter=';'):
            if row[3] != item:
                writer.writerow(row)
            else:
                print('asdf')



def remove_from_directory(item):
    for x in os.listdir('./'):
        if x == item:
            try:
                os.remove(item)
                print('Removed from files: ' + item)
            except OSError:
                print('Remove manualy: ' + item)



def match_and_delete(subjectArray, counterpartArray, isCsv):
    counter = 0
    subjectHolder = subjectArray
    counterpartHolder = counterpartArray

    if isCsv:
        subjectHolder = subjectArray[:, 3]
    else:
        counterpartHolder = counterpartArray[:, 3]

    for item in subjectHolder:
        if item not in counterpartHolder:
            subjectArray = np.delete(subjectArray, counter, 0)
            if isCsv:
                remove_from_csv(item)
            else:
                remove_from_directory(item)
            return False, subjectArray
        counter = counter + 1

    return True, subjectArray


def read_data_and_reshape(arr, fileArr):
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

        return arr, fileArr


def convert(arr, fileArr):
    trigger = False

    if (type(arr).__module__ != np.__name__):
       arr, fileArr = read_data_and_reshape(arr, fileArr) 

    trigger, arr = match_and_delete(arr, fileArr, True)

    if not trigger:
        return trigger, arr, fileArr

    trigger, fileArr = match_and_delete(fileArr, arr, False)

    return trigger, arr, fileArr


def main():
    arr = []
    fileArr = []
    trigger = False
    
    while not trigger:
        trigger, arr, fileArr = convert(arr, fileArr)
    
    print(arr[:, 3].size)
    print(fileArr.size)


if __name__ == "__main__":
    main()