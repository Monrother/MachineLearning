from numpy import *
import time
import matplotlib.pyplot as plt

# calculate the Euclidean distance
def euclDistance(vector1, vector2):
    return sqrt(sum(power(vector2 - vector1, 2)))

# init centroids with random samples
def initCentroids(dataSet, k):
    numSamples, dim = dataSet.shape
    centroids = zeros((k, dim))
    for i in range(k):
        index = int(random.uniform(0, numSamples))
        centroids[i, :] = dataSet[index, :]
    return centroids

# k-means cluster
def kmeans(dataSet, k):
    numSamples = dataSet.shape[0]

    clusterAssment = mat(zeros((numSamples, 2)))
    clusterChanged = True

    ## step1: init centroids
    centroids = initCentroids(dataSet, k)

    epoch = 0
    while clusterChanged:
        epoch += 1

        clusterChanged = False
        ## for each sample
        for i in xrange(numSamples):
            minDist = 10000.0
            minIndex = 0

            ## step2: assign every sample to corresponding centroid
            for j in range(k):
                dist = euclDistance(dataSet[i, :], centroids[j, :])
                if dist < minDist:
                    minDist = dist
                    minIndex = j

                ## step3: update the cluster of every sample
            if clusterAssment[i, 0] != minIndex:
                clusterChanged = True
                print("epoch: %g, # of changed points: %g, from %g to %g" %(epoch, i, clusterAssment[i, 0], minIndex))

                clusterAssment[i, :] = minIndex, minDist ** 2

        ## step4: update the centroids
        for j in range(k):
            pointsInCluster = dataSet[nonzero(clusterAssment[:, 0].A == j)[0]]
            centroids[j, :] = mean(pointsInCluster, axis = 0)


    print('Congratulations, cluster complete!')
    return centroids, clusterAssment

# show your cluster, only available with 2-D data
def showCluster(dataSet, k, centroids, clusterAssment):
    numSamples, dim = dataSet.shape
    if dim != 2:
        print("Sorry, the pic that you want to plot is unavailable.")
        return 1

    mark = ['or', 'ob', 'og', 'ok', '^r', '+r', 'sr', 'dr', '<r', 'pr']
    if k > len(mark):
        print("You don't have so many bicycles.")
        return 1

    # draw all samples
    for i in xrange(numSamples):
        markIndex = int(clusterAssment[i, 0])
        plt.plot(dataSet[i, 0], dataSet[i, 1], mark[markIndex])

    mark = ['Dr', 'Db', 'Dg', 'Dk', '^b', '+b', 'sb', 'db', '<b', 'pb']

    # draw the centroids
    for i in range(k):
        plt.plot(centroids[i, 0], centroids[i, 1], mark[i], markersize=12)

    plt.show()

