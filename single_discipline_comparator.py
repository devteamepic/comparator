import csv
import os, glob
import numpy as np
import misc_functions as mf


def compare():
    arr = []
    fileArr = []
    trigger = False
    
    while not trigger:
        trigger, arr, fileArr = convert(arr, fileArr, trigger)

   # TODO delete old data.csv and make a new one
    print(arr[:, 3].size)
    print(fileArr.size)


def match_and_delete(subjectArray, counterpartArray, isCsv):
    counter = 0
    subjectHolder = subjectArray
    counterpartHolder = counterpartArray

    if isCsv:
        subjectHolder = subjectArray[:, 3]
    else:
        counterpartHolder = counterpartArray[:, 3]

#    if asdf:
#        print(subjectHolder)
#        print('----------')
#        print(counterpartHolder)
    for item in subjectHolder:
        dummy = './singleDisciplineDirectory/files/' + item
        if dummy not in counterpartHolder:
            subjectArray = np.delete(subjectArray, counter, 0)
            if isCsv:
                mf.remove_from_csv(item, './singleDisciplineDirectory')
            else:
                print('here')
                mf.remove_from_directory(item, './singleDisciplineDirectory')
            return False, subjectArray
        counter = counter + 1

    print('what')
    return True, subjectArray


def convert(arr, fileArr, trigger):

    if (type(arr).__module__ != np.__name__):
        arr, fileArr = mf.read_data_and_reshape(arr, fileArr, './singleDisciplineDirectory') 

    # TODO under construction
    if trigger:
        trigger, fileArr = match_and_delete(fileArr, arr, False)
        return trigger, arr, fileArr

    trigger, arr = match_and_delete(arr, fileArr, True)

    if not trigger:
        return trigger, arr, fileArr
    

    return None, [], []
