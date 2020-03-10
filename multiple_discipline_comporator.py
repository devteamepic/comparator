import csv
import os, glob
import numpy as np
import misc_functions as mf

def compare():
    arrPrime = []
    arrSub = []
    fileArrPrime = []
    fileArrSub = []

    trigger = False

    while not trigger:
        trigger, arrPrime, fileArrPrime, arrSub, fileArrSub = convert(arrPrime, fileArrPrime, arrSub, fileArrSub)


def match_and_delete(arrPrime, arrSub, fileArrPrime, fileArrSub):
    counter = 0

    for item in arrPrime:
        if item in arrSub:
            arrSub = np.delete(arrSub, counter, 0)
            remove_from_csv(item, './multipleDisciplineDirectory/subFiles')
            remove_from_directory(item, )
    return 


def convert(arrPrime, fileArrPrime, arrSub, fileArrSub):
    trigger = False

    if (type(arrPrime).__module__ != np.__name__):
        arrPrime, fileArrPrime = mf.read_data_and_reshape(arrPrime, fileArrPrime)
        arrSub, fileArrSub = mf.read_data_and_reshape(arrSub, fileArrSub)

    trigger, arrPrime = match_and_delete(arrPrime, arrSub, fileArrPrime, fileArrSub)

    if not trigger:
        return trigger, arrPrime, fileArrPrime, arrSub, fileArrSub
