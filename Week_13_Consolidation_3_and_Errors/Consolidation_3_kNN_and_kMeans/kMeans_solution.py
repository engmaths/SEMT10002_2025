import matplotlib.pyplot as plt 
import random
import numpy as np 

file = "heart_data.csv"



#Your code for reading and visualising the data goes here.

def initialise_means(k, data):

    #means should be a list of k points, where each point is an tuple (feature1, feature2).
    random_indexes = [random.randint(0, len(data[0])) for val in range(k)]
    initial_means = [(data[0][index], data[1][index]) for index in random_indexes]

    print(initial_means)

    return initial_means

def assign_data_to_clusters(centroids, data):
    #Your code goes here

    #Clusters should be a list of tuples. Each list should contain all data points assigned to a cluster
    clusters = [[] for val in range(len(centroids))]

    for data_index in range(len(data[0])):
        data_point = (data[0][data_index], data[1][data_index])
        min_dist = None
        cluster = -1 

        for (cluster_index, mean) in enumerate(centroids):
            distance = (data_point[0] - mean[0])**2 + (data_point[1] - mean[1])**2
            if min_dist == None or distance < min_dist:
                min_dist = distance
                cluster = cluster_index
        
        clusters[cluster].append(data_point)

    print(clusters)

    return clusters

def calculate_cluster_means(clusters):

    #Centroids should be a list of points (x, y, ... ), with each point representing the mean position of all data in a cluster
    #means = [0 for val in range(len(clusters))]
    means = []

    for cluster in clusters:
        feature1 = [value[0] for value in cluster]
        feature2 = [value[1] for value in cluster]

        mean_1 = np.mean(feature1)
        mean_2 = np.mean(feature2)

        cluster_mean = (mean_1, mean_2)
        means.append(cluster_mean)

    return means

def plot_clusters(clusters):

    fig = plt.figure()
    ax = fig.add_subplot(111)
    colors = ['r', 'g', 'b']
    color_index = 0

    for cluster in clusters:
        x_data = [value[0] for value in cluster]
        y_data = [value[1] for value in cluster]

        ax.scatter(x_data, y_data, color=colors[color_index])
        color_index = color_index + 1
    
    plt.show()

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

with open(file, 'r') as f:
    data = f.readlines()
    data = [line.split(',') for line in data[1:]]

ages = []
creatanines = []

for values in data:
    ages.append(float(values[0]))
    creatanines.append(float(values[2]))

#plt.scatter(ages, creatanines)
#plt.show()

data = [ages, creatanines]

kMeans(2, [ages, creatanines])