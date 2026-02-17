import matplotlib.pyplot as plt 
import random
import pandas as pd
import numpy as np

file = "heart_data.csv"

def initialise_means(k, data):
    minmaxage = [int(min(data["age"])), int(max(data["age"]))]
    minmaxcreatinine = [int(min(data["creatinine_phosphokinase"])), int(max(data["creatinine_phosphokinase"]))]
    
    initial_means = [[random.randint(*minmaxage), random.randint(*minmaxcreatinine)] for _ in range(k)]
    return initial_means

def get_euclidean_distances(value,data):
    distance_list = list(map(lambda index,p: [index,sum((a-b)**2 for a,b in zip(value,p))**0.5],range(len(data)),data))
    return sorted(distance_list,key=lambda x: x[1])


def assign_data_to_clusters(centroids, data):
    clusters = [[] for _ in range(len(centroids))]
    
    for age, creatinine in zip(data["age"], data["creatinine_phosphokinase"]):
        point = [age, creatinine]
        centroid_index = get_euclidean_distances(point,centroids)[0][0]
        clusters[centroid_index].append(point)

    return clusters

def calculate_cluster_means(clusters):
    means = []
    for cluster in clusters:
        if len(cluster) > 0:
            xs, ys = list(zip(*cluster))
            mean_x = sum(xs) / len(xs)
            mean_y = sum(ys) / len(ys)
            means.append([mean_x, mean_y])
        else:
            pass 

    return means

def plot_clusters(clusters):
    colors = ['r', 'b', 'g', 'c', 'm', 'y'] # simple color list
    for i, cluster in enumerate(clusters):
        if len(cluster) > 0:
            xs, ys = list(zip(*cluster))
            c = colors[i % len(colors)] 
            plt.scatter(xs, ys, color=c, label=f'Cluster {i+1}')
            
    plt.xlabel('Age')
    plt.ylabel('Creatinine Phosphokinase')
    plt.legend()
    plt.show()

def kMeans(k, data, max_iterations=100):
    means = initialise_means(k, data)

    for iteration in range(max_iterations):
        clusters = assign_data_to_clusters(means, data)
        
        new_means = calculate_cluster_means(clusters)
        
        
        if len(new_means) != k:
            means = new_means
        elif new_means == means:
            print(f"Converged at iteration {iteration}")
            break
        else:
            means = new_means

    plot_clusters(clusters)



def kNN(k,i,training_data :pd.DataFrame):
    neighbour_indexes,_ = zip(*get_euclidean_distances(i,training_data.values.tolist())[:k])
    neighbour_deaths = training_data.iloc[list(neighbour_indexes),3].tolist()

    return 0 if sum(neighbour_deaths)/len(neighbour_deaths) <0.5 else 1
        

def calculate_knn_mse_error(k,data : pd.DataFrame):
    training_data = data.iloc[0:250]
    test_data = data.iloc[250:].values.tolist()

    comparison_list = []
    for i in test_data:
        y_hat = kNN(k,i,training_data)
        comparison_list.append([y_hat,int(i[3])])
    
    return (1/len(comparison_list))*(sum((y_hat-y)**2 for y_hat,y in comparison_list))
    

if __name__ == "__main__":

    try:
        heartdata = pd.read_csv(file)
        plotdata = heartdata[["age", "creatinine_phosphokinase"]]
        knndata = heartdata[["age","creatinine_phosphokinase","ejection_fraction","DEATH_EVENT"]]

        kMeans(3, plotdata)
        errors = [[k,calculate_knn_mse_error(k,knndata)] for k in range(1,11)]


        ks = [k for k, _ in errors]
        mses = [mse for _, mse in errors]
        plt.figure()
        plt.plot(ks, mses, marker='o')
        plt.xlabel('k (number of neighbours)')
        plt.ylabel('KNN MSE')
        plt.title('KNN MSE vs k')
        plt.grid(True, alpha=0.3)
        plt.show()
    except FileNotFoundError:
        print("Error: 'heart_data.csv' not found. Please ensure the file is in the directory.")