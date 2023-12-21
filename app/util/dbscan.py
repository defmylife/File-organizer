import sys, os, pprint
from typing import List, Union, Dict
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import DBSCAN
from util.getFiles import *

'''def list_files(path):
    try:
        # Get all files in the directory
        files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
        return files
        
    except FileNotFoundError:
        print("The specified path was not found.")
'''

def dbscan(files :list) -> Union[Dict, List[str]]:

    # Convert file names into TF-IDF features
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(files)
    # print(vectorizer.get_feature_names_out())

    # Use DBSCAN for clustering and outlier detection
    dbscan = DBSCAN(eps=1.2, min_samples=2)
    labels = dbscan.fit_predict(X)

    # Organize files into clusters
    clusters = {}
    for i, label in enumerate(labels):
        if label not in clusters:
            clusters[label] = []
        clusters[label].append(files[i])

    # Get outlier file names
    outliers = [files[i] for i in range(len(files)) if labels[i] == -1]

    return clusters, outliers

if __name__=='__main__':
    # Replace 'Downloads' with the desired directory path
    directory_path = r'C:\Users\uSeR\Downloads'
    file_names, _ = getFiles(directory_path)

    if file_names:
        clusters, outliers = dbscan(file_names)
        
        print("Files in each cluster ({}):".format(len(clusters)))
        for i, files_in_cluster in clusters.items():
            if i != -1:
                print("Cluster {} ({}): {}".format(i, len(files_in_cluster), files_in_cluster))

        print("\nOutlier file names ({}):".format(len(outliers)))
        pprint.pprint(outliers)
    else:
        print("No files found in the specified path.")
