import os, glob
import csv
import numpy as np


def read_data_and_reshape(arr, fileArr, directory):
    with open(directory + '/data.csv') as dataFile:
        csvReader = csv.reader(dataFile, delimiter = ";")
        for row in csvReader:
            arr.append(row)
    
        del arr[0]
        for file in glob.glob(directory + "/files/*"):
            holder = list(file)
            holder[33] = '/'
            fileArr.append("".join(holder))
        
        arr = np.array(arr)
        fileArr = np.array(fileArr)
        
        fileArr = fileArr[fileArr.argsort(kind="heapsort")]
        arr = arr[arr[:,3].argsort(kind="heapsort")]

        return arr, fileArr


def remove_from_csv(item, directory = ''):
    with open(directory + '/data.csv', 'rt', ) as inpt, open(directory + '/data_converted.csv', 'wt') as out:
        writer = csv.writer(out, delimiter=';')
        for row in csv.reader(inpt, delimiter=';'):
            if row[3] != item:
                writer.writerow(row)


def remove_from_directory(item, directory = ''):
    for x in os.listdir(directory + '/files/'):
        if x == item:
            print(x)
            print(item)
            try:
                os.remove(item)
                print('Removed from files: ' + item)
            except OSError:
                print('Remove manualy: ' + item)
