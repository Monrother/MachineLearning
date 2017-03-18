from numpy import *
import matplotlib.pyplot as plt


def dist_cal(x, y):
    # x and y must be np vector
    return sqrt(sum(power(x-y, 2)))


def sel_n_k(n, k):
    # return k exclusive numbers of numbers from 1 to n
    sel = range(n)
    random.shuffle(sel)
    return sel[:k]


def k_means(dataset, k):
    num_points, dim = dataset.shape
    indices = sel_n_k(num_points, k)
    centroids = dataset[indices, :]
    # initialize all the distances to infitine maximum
    assign_changed = True
    assign = mat(zeros([num_points, 1]))

    while(assign_changed):
        assign_changed = False
        min_dist = mat(inf * ones([num_points, 1]))
        # step1: assign the points to the closest centroid
        for i in range(num_points):
            min_dist = inf
            for j in range(k):
                dist = dist_cal(dataset[i, :], centroids[j, :])
                if dist < min_dist:
                    min_dist = dist
                    temp_assign = j
            if temp_assign != assign[i]:
                assign_changed = True
                assign[i] = temp_assign

        #step2: update the centroids to the mean of the cluster
        for j in range(k):
            sum = mat(zeros([1, dim]))
            npoints = 0
            for i in range(num_points):
                if assign[i] == j:
                    sum += dataset[i, :]
                    npoints += 1
            centroids[j] = sum / npoints;

    return centroids, assign

def show_cluster(dataset, k, centroids, assign):
    num_points, dim = dataset.shape
    mark = ['sr', 'Dr', '1g', 'pr']

    for i in xrange(num_points):
        markIndex = int(assign[i, 0])
        plt.plot(dataset[i, 0], dataset[i, 1], mark[markIndex])

    mark = ['sb', 'Db', '1k', 'pb']
    for i in range(k):
        plt.plot(centroids[i, 0], centroids[i, 1], mark[i], markersize = 12)

    plt.show()




