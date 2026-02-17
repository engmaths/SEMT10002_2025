import matplotlib.pyplot as plt 
import random
import math
import statistics

file = "heart_data.csv"

#Your code for reading and visualising the data goes here.

def initialise_means(k, data_pts):

    initial_means = []

    #means should be a list of k points, where each point is an tuple (feature1, feature2).
    for _ in range(k):
        num = random.randint(0,len(data_pts)-1)
        initial_means.append(data_pts[num])

    return initial_means

def assign_data_to_clusters(centroids, data_pts):
    
    #Clusters should be a list of tuples. Each list should contain all data points assigned to a cluster
    clusters = [[] for val in range(len(centroids))]

    #Your code goes here
    for point in data_pts:
        distances = [distBetween(point, c) for c in centroids]

        closest_index = distances.index(min(distances))

        clusters[closest_index].append(point)

    return clusters

def calculate_cluster_means(clusters):

    #Centroids should be a list of points (x, y, ... ), with each point representing the mean position of all data in a cluster
    means = [0 for val in range(len(clusters))]

    for i in range (len(clusters)):
        x = [p[0] for p in clusters[i]]
        y = [p[1] for p in clusters[i]]

        means[i] = (statistics.mean(x),statistics.mean(y))

    return means

def plot_clusters(clusters):

    colours = ['blue', 'red', 'green']

    for i in range(len(clusters)):

        
        x = [p[0] for p in clusters[i]]
        y = [p[1] for p in clusters[i]]

        plt.scatter(x, y, marker='o', color = colours[i])

    plt.xlabel("Age")
    plt.ylabel("Creatinine Phosphokinase")

    plt.grid(False)
    plt.show()


def kMeans(k, data_pts, max_iterations = 100):

    #We need to randomly initialise the means (or centroids) before we can start
    means = initialise_means(k, data_pts)

    #kMeans doesn't always converge, so we set a maximum number of iterations to stop our code from running forever. 
    for iteration in range(max_iterations):
        #We start by assigning data to clusters
        clusters = assign_data_to_clusters(means, data_pts)
        #Next we update our centroids
        means = calculate_cluster_means(clusters)
        #Sometime it's helpful to visualise each step of the algorithm- uncomment the line below to see that.
        #plot_clusters(clusters)

    #Once finished, let's plot the clusters
    plot_clusters(clusters)

def distBetween(a,b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

if __name__ == "__main__":

    
    age = []
    creatinine_phosphokinase = []

    with open('heart_data.csv') as file:
        data = list(file)[1:]

        for value in data:
        
            parts = value.strip().split(",")

            age.append(float(parts[0]))
            creatinine_phosphokinase.append(float(parts[2]))

    data_pts = list(zip(age,creatinine_phosphokinase))

    kMeans(3, data_pts)


