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

        #Loop through data[1:] so we skip the header line
        for line in data[1:]:
            #csv file so we can split on a comma to get a list of values
            vals = line.split(',')
            ages.append(float(vals[age_index]))
            creatine_tests.append(float(vals[creatine_index]))

    return np.array([ages, creatine_tests])

def initalise_centroids(k, data):
    '''
    Initialise centroids by randomly selecting k data points
    Centroids should be a list of k points, where each point is an 1x2 numpy array [feature1, feature2].
    '''

    ages = data[0, :]
    creatine_tests = data[1, :]

    #For each centroid, we need to generate a random number between 0 and the size of the data to be an index
    random_indices = [random.randint(0, len(ages)) for val in range(k)]
    #We then index into the array to choose our centroids
    centroids = [np.array([ages[index], creatine_tests[index]]) for index in random_indices]

    return centroids

def assign_data_to_clusters(centroids, data):
    
    #Create an zero array of size number of centroids * number of data points
    cluster_distances = np.zeros((len(centroids), data.shape[1]))

    #Loop through the centroids
    for (i, centroid) in enumerate(centroids):
        #Need to turn centroid from a shape (2, ) array into a shape (2, 1) array so the subtraction works
        reshaped_centroid = np.reshape(centroid, (2, 1))
        #Calculate the distance from each point in the dataset to the centroid
        distances = data - (np.ones((2, data.shape[1])) * reshaped_centroid)
        #Calculate the squared sum of the distances- we don't need to take the square root.
        squared_distances = np.sum(distances**2, axis=0)
        #Store the squared distances in our cluster_distances array
        cluster_distances[i, :] = squared_distances

    #Find which cluster each data point is closest too by selecting whichever centroid has the lowest distance
    cluster_indexes = np.argmin(cluster_distances, axis=0)
    #Use boolean indexing to assign each data point to the correct cluster
    clusters = [data[:, index == cluster_indexes] for index in range(len(centroids))]

    return clusters

def calculate_cluster_means(clusters):

    #Centroids should be a list of points (x, y, ... ), with each point representing the mean position of all data in a cluster
    centroids = [np.mean(cluster, axis=1) for cluster in clusters]

    return centroids

def plot_clusters(clusters, centroids):

    fig = plt.figure(figsize=(9, 4))
    ax = fig.add_subplot(111)

    colors = cm.rainbow(np.linspace(0, 1, len(clusters)))
    for (i, cluster) in enumerate(clusters):
        ax.scatter(cluster[0, :], cluster[1, :], color=colors[i])
        ax.scatter(centroids[i][0], centroids[i][1], marker='+', color=colors[i])

    plt.show()

def kMeans(k, data, max_iterations = 50):

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

    cluster1 = np.array([(1, 1, 1), (1, 1, 1)])
    cluster2 = np.array([(10, 10, 10), (10, 10, 10)])
    clusters = [cluster1, cluster2]

    centroids = calculate_cluster_means(clusters)

    assert np.array_equal(centroids[0], np.array([1., 1.])), centroids[0]
    assert np.array_equal(centroids[1], np.array([10, 10])), centroids[0]
    assert len(centroids) == 2
    assert centroids[0].shape == (2, )

def test_assign_data_to_clusters():

    Xs = np.array([25 * random.random() for val in range(60)] + [50 + (1 * random.random()) for val in range(40)] )
    Ys = np.array([50 + (1 * random.random()) for val in range(100)] )

    data = np.array([Xs, Ys])

    centroids = [np.array([12.5, 50]), np.array([50.5, 50.5])]

    clusters = assign_data_to_clusters(centroids, data)

    assert clusters[0].shape == (2, 60), clusters[0].shape
    assert clusters[1].shape == (2, 40), clusters[1].shape

    print(clusters)

def test_kMeans():

    test_assign_data_to_clusters()
    test_calculate_cluster_means()

    Xs = np.array([25 * random.random() for val in range(60)] + [50 + (25 * random.random()) for val in range(40)] )
    Ys = np.array([10 * random.random() for val in range(30)] + [60 + (20 * random.random()) for val in range(70)] )

    data = np.array([Xs, Ys])

    kMeans(3, data)


def main():

    test_kMeans()

    k = 3
    filename = "heart_data.csv"
    data = read_data_file(filename)
    kMeans(k, data)

main()

