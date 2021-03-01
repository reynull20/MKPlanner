# MADE BY : 16519045 / M. Reyhanullah Budiaman
#
# This is a simple program for solving topological sort 
# for making course schedule

from Dag import DAG
from topological import *

def readfile(file_name):
    cd_file = open(("../test/" + file_name), 'r')
    matkul = cd_file.readlines()
    arr_of_course = []

    for i in range(len(matkul)):
        arr_of_course.append(matkul[i].replace("\n", "").replace(".",""))

    return arr_of_course

def getPrecDict(course):
    '''Get all preRec from course and returning it with dictionary representation.'''
    prec = {}
    
    for i in range(len(course)):
        deskripsi = course[i].split(", ")
        key = deskripsi[0]
        deskripsi.remove(key)
        prec[key] = deskripsi
        
    return prec


#MAIN ALGORITHM
exit_loop = 1
while(exit_loop):
    fl = input("Enter filename : ")

    prerequirement = getPrecDict(readfile(fl))

    graf = DAG(prerequirement)
    prerec_dict = graf.getderajatmasuk()

    result, schedule = topological_sort(graf, prerec_dict)

    printSchedule(schedule)

    decision = input("Try another file? (Y/n) : ")
    if(decision == "Y" or decision == "y"):    
        exit_loop = 1
    else :
        exit_loop = 0
