import sys
import os
path = os.path.dirname(os.path.abspath(__file__))

print(path)
file1 = open(path + '\\file1.txt', 'r')

dataFromFile1 = file1.readlines()

file2 = open(path + '\\file2.txt', 'w')
file2.writelines(dataFromFile1)