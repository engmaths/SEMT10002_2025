import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib.pyplot import cm
import random

def read_data_file(filename):

    with open(filename, 'r') as f:

        data = f.readlines()

        ages = []
        age_index = 0 
        creatine_tests = []
        creatine_index = 2

        #Loop through from data[1:] so we skip the header line
        for line in data[1:]:
            #csv file so we can split on a comma to get a list of values
            vals = line.split(',')
            #Then extract the correct values from the list
            ages.append(float(vals[age_index]))
            creatine_tests.append(float(vals[creatine_index]))

    return [ages, creatine_tests]

def initalise_centroids(k, data):
    '''
    Initialise centroids by randomly selecting k data points
    Centroids should be a list of k points, where each point is an 1x2 numpy array [feature1, feature2].
    '''

    ages = data[0]
    creatine_tests = data[1]

    #For each centroid, we need to generate a random number between 0 and the size of the data to be an index
    random_indices = [random.randint(0, len(ages)) for val in range(k)]

    #We then index into the array to choose our centroids
    centroids = [[ages[index], creatine_tests[index]]for index in random_indices]

    return centroids

def calculate_squared_distance(datum, centroid):

    squared_distance = 0
    for (datum_i, centroid_i) in zip(datum, centroid):
        squared_distance += (datum_i - centroid_i)**2

    return squared_distance

def assign_data_to_clusters(centroids, data):
    
    #Create an empty list for each cluster
    clusters = [[] for _ in range(len(centroids))]
    #Loop through the data points
    for index in range(len(data[0])):
        datum = (data[0][index], data[1][index])
        #Loop through the centroids, storing which is closest to the data point
        min_index = np.inf
        min_distance = np.inf
        for (index, centroid) in enumerate(centroids):
            distance_squared = calculate_squared_distance(datum, centroid)
            #If the distance squared is lower than any we've seen so far, store the index
            if distance_squared < min_distance:
                min_index = index
                min_distance = distance_squared
        #Add the data point to the cluster it is closest too
        clusters[min_index].append(datum)

    return clusters

def calculate_cluster_means(clusters):

    #Loop through the clusters
    centroids = []
    for cluster in clusters:
        #Loop through each feature
        centroid = []
        '''
        This is a bit of Python "magic" to turn a list of tuples into a list of lists.
        i.e we have clusters as [(data_0_feature1, data_0_feature2), (data_1_feature1, data_1feature2)] 
        but we need it as [[data_0_feature1, data_1_feature1], [data_0_feature2, data_1_feature2]]
        '''
        cluster_as_lists = list(zip(*cluster))
        #Loop over each feature
        for index in range(len(cluster_as_lists)):
            #Calculate the mean of each feature
            mean = np.mean(cluster_as_lists[index])
            centroid.append(mean)
        centroids.append(centroid)

    return centroids

def plot_clusters(clusters, centroids):

    fig = plt.figure(figsize=(9, 4))
    ax = fig.add_subplot(111)


    colors = cm.rainbow(np.linspace(0, 1, len(clusters)))
    for (i, cluster) in enumerate(clusters):
        ax.scatter([val[0] for val in cluster], [val[1] for val in cluster], color=colors[i])
        print("Centroids")
        print(centroids)
        ax.scatter(centroids[i][0], centroids[i][1], marker='+', color=colors[i])

    plt.show()

def kMeans(k, data, max_iterations = 100):

    #We need to randomly initialise the means (or centroids) before we can start
    centroids = initalise_centroids(k, data)

    #kMeans doesn't always converge, so we set a maximum number of iterations to stop our code from running forever. 
    for iteration in range(max_iterations):
        #We start by assigning data to clusters
        clusters = assign_data_to_clusters(centroids, data)

        #Next we update our centroids
        centroids = calculate_cluster_means(clusters)


    #Once finished, let's plot the clusters
    plot_clusters(clusters, centroids)

def test_calculate_cluster_means():

    cluster1 = [(1, 1), (1, 1), (1, 1)]
    cluster2 = [(10, 10), (10, 10), (10, 10)]
    clusters = [cluster1, cluster2]

    centroids = calculate_cluster_means(clusters)

    assert centroids[0] == [1., 1.], centroids[0]
    assert centroids[1] == [10., 10.], centroids[1]
    assert len(centroids) == 2
    assert len(centroids[0]) == 2

def test_assign_data_to_clusters():

    Xs = [25 * random.random() for val in range(60)] + [50 + (1 * random.random()) for val in range(40)] 
    Ys = [50 + (1 * random.random()) for val in range(100)] 

    data = [Xs, Ys]

    centroids = [[12.5, 50], [50.5, 50.5]]

    clusters = assign_data_to_clusters(centroids, data)

    print(clusters)

    assert len(clusters[0]) == 60
    assert len(clusters[1]) == 40

def test_kMeans():

    test_assign_data_to_clusters()
    test_calculate_cluster_means()

    Xs = [25 * random.random() for val in range(60)] + [50 + (25 * random.random()) for val in range(40)]
    Ys = [10 * random.random() for val in range(30)] + [60 + (20 * random.random()) for val in range(70)]

    data = [Xs, Ys]

    kMeans(3, data)


def main():

    test_kMeans()

    k = 3
    filename = "heart_data.csv"
    data = read_data_file(filename)
    kMeans(k, data)

main()

