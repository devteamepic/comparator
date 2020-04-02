import csv
import os, glob
import numpy as np
import misc_functions as mf


def compare():
    arr = []
    fileArr = []
    trigger = False
    stateEnum = ['CSV', 'FILES']
    stateNumber = 0

    while not trigger:
        if stateNumber > 1:
            trigger = True
            continue

        trigger, stateNumber, arr, fileArr = convert(arr, fileArr, trigger, stateEnum[stateNumber], stateNumber)


   # TODO delete old data.csv and make a new one
    print('done')


def match_and_delete(subjectArray, counterpartArray, isCsv, stateNumber):
    counter = 0
    subjectHolder = subjectArray
    counterpartHolder = counterpartArray

    if isCsv:
        subjectHolder = subjectArray[:, 3]
    else:
        counterpartHolder = counterpartArray[:, 3]

    for item in subjectHolder:
        if isCsv:
            dummy = './singleDisciplineDirectory/files/' + item
        else:
            dummy = item.replace('./singleDisciplineDirectory/files/', '')

        if dummy not in counterpartHolder:
            print('now here')
            subjectArray = np.delete(subjectArray, counter, 0)
            if isCsv:
                mf.remove_from_csv(item, './singleDisciplineDirectory')
                return stateNumber, subjectArray
            else:
                print('asdf')
                mf.remove_from_directory(item, './singleDisciplineDirectory')
                return stateNumber, subjectArray
        counter = counter + 1

    stateNumber = stateNumber + 1
    return stateNumber, subjectArray


def convert(arr, fileArr, trigger, state, stateNumber):
    if (type(arr).__module__ != np.__name__):
        arr, fileArr = mf.read_data_and_reshape(arr, fileArr, './singleDisciplineDirectory') 

    # TODO under construction
    if state == 'FILES':
        print('in files')
        stateNumber, fileArr = match_and_delete(fileArr, arr, False, stateNumber)
        return trigger, stateNumber, arr, fileArr

    if state == 'CSV':
        stateNumber, arr = match_and_delete(arr, fileArr, True, stateNumber)
        return trigger, stateNumber, arr, fileArr,

    return True, [], []
