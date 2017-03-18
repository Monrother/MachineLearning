from numpy import *
from k_means import *
import matplotlib.pyplot as plt

dataSet = []
fileIn = open("data.txt")
for line in fileIn.readlines():
    lineArr = line.strip().split('\t')
    dataSet.append([float(lineArr[0]), float(lineArr[1])])

dataSet = mat(dataSet)
k = 4
centroids, assign = k_means(dataSet, k)
show_cluster(dataSet, k, centroids, assign)