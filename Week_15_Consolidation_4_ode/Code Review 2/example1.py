import matplotlib.pyplot as plt 
import csv
import random
import math


heartfile = "heart_data.csv"

data = []
with open(heartfile, 'r') as file:
    csv_file = csv.DictReader(file)
    for row in csv_file:
        data.append(dict(row))

Creatinine = [float(x ['creatinine_phosphokinase']) for x in data]
Age = [float(x ['age']) for x in data]
points = list(zip(Age, Creatinine))

plt.plot(Age,Creatinine,'co')
plt.xlabel("Age")
plt.ylabel("Creatinine")
plt.show()

#Your code for reading and visualising the data goes here.

def initialise_means(k, data):

    #means should be a list of k points, where each point is an tuple (feature1, feature2).

    return random.sample(data, k)

def assign_data_to_clusters(centroids, data):
    #Your code goes here

    #Clusters should be a list of tuples. Each list should contain all data points assigned to a cluster
    clusters = [[] for val in range(len(centroids))]

    for point in data:
        distances = []
        for centroid in centroids:
            dist = math.dist(point, centroid)
            distances.append(dist)

        closest_index = distances.index(min(distances))
        clusters[closest_index].append(point)

    return clusters

def calculate_cluster_means(clusters):

    #Centroids should be a list of points (x, y, ... ), with each point representing the mean position of all data in a cluster
    means = [0 for val in range(len(clusters))]

    for cluster in clusters:
        if len(cluster) == 0:
            means.append((0, 0))
            continue

        x_mean = sum(point[0] for point in cluster) / len(cluster)
        y_mean = sum(point[1] for point in cluster) / len(cluster)
        means.append((x_mean, y_mean))

    return means

def plot_clusters(clusters):
    colors = ['r', 'g', 'b']

    for i, cluster in enumerate(clusters):
        if cluster:
            x = [point[0] for point in cluster]
            y = [point[1] for point in cluster]
            plt.scatter(x, y, c=colors[i % len(colors)], label=f"Cluster {i+1}")


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

kMeans(3, points)
