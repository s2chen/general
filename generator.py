# -*- coding: utf-8 -*-
"""
Created on Sun Feb 22 13:55:27 2015

@author: Shuang
"""

'''
Generator
'''
#Looping over directory names under certain folder
import os

#list files
def getallfiles(folder):
    for path, dirlist, filelist in os.walk(folder):
        for fn in filelist:
            yield os.path.join(path,fn)

#given a generator that yields open file objects (open('filename')),
#   yield the lines from those files
def catallfiles(openfile_gen):
    for openfile in openfile_gen:
        for line in openfile:
            yield line

#get all files
files = getallfiles('/Users/Shuang/Documents')
#filter files (*.txt)
files = (fn for fn in files if fn.endswith('.txt'))

#open files
openfiles = (open(fn) for fn in files)

#get all lines
lines = catallfiles(openfiles)
#filter lines (line starts with 'date:' only)
lines = (line for line in lines if line[:5] == 'date:')

#split lines
data = (line.split(',') for line in lines)
#get 2nd col ('1th') and convert to int
data = (int(split[1]) for split in data) 

#hey look, 'sum' consumes any iterable (not just a list)! 
print sum(data)


