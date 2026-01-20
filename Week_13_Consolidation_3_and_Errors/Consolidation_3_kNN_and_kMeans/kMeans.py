import matplotlib.pyplot as plt 

file = "heart_data.csv"

#Your code for reading and visualising the data goes here.

def initialise_means(k, data):

    #means should be a list of k points, where each point is an tuple (feature1, feature2).
    initial_means = []

    return initial_means

def assign_data_to_clusters(centroids, data):
    #Your code goes here

    #Clusters should be a list of tuples. Each list should contain all data points assigned to a cluster
    clusters = [[] for val in range(len(centroids))]

    return clusters

def calculate_cluster_means(clusters):

    #Centroids should be a list of points (x, y, ... ), with each point representing the mean position of all data in a cluster
    means = [0 for val in range(len(clusters))]

    return means

def plot_clusters(clusters):

    #Your code goes here. You should plot all data, using a different color to represent each cluster. 
    pass

def kMeans(k, data, max_iterations = 100):

    #We need to randomly initialise the means (or centroids) before we can start
    means = initialise_means(k, data)

    #kMeans doesn't always converge, so we set a maximum number of iterations to stop our code from running forever. 
    for iteration in range(max_iterations):
        #We start by assigning data to clusters
        clusters = assign_data_to_clusters(means, data)
        #Next we update our centroids
        means = calculate_cluster_means(clusters)
        #Sometime it's helpful to visualise each step of the algorithm- uncomment the line below to see that.
        #plot_clusters(clusters)

    #Once finished, let's plot the clusters
    plot_clusters(clusters)

