import numpy as np
from scipy.optimize import linear_sum_assignment

from user.models import User as UserModel

def earth_movers_distance(p, q):
    if len(p) != len(q):
        raise ValueError("Input sets must have the same length.")

    # Normalize the input sets to ensure they sum to 1
    p = np.array(p) / np.sum(p)
    q = np.array(q) / np.sum(q)

    # Calculate the cost matrix
    cost_matrix = np.abs(np.subtract.outer(p, q))

    # Solve the linear sum assignment problem to find optimal transport plan
    row_indices, col_indices = linear_sum_assignment(cost_matrix)
 
    # Calculate the Earth Mover's Distance
    emd = cost_matrix[row_indices, col_indices].sum()

    return int((1-emd)*100)

b = UserModel.objects.filter()
for i in b:
    s1 = []
    for j in i.tweets_sentiments.split("#"):
        s1.append(float(j))
    s2 = []
    for j in i.images_sentiments.split("#"):
        s2.append(float(j))
    dist = earth_movers_distance(s1, s2)
    # print(dist)
    UserModel.objects.filter(id=i.id).update(images_tweets_distance=dist)

##
b = UserModel.objects.filter()
for i in b:
    s1 = []
    for j in i.tweets_sentiments.split("#"):
        s1.append(float(j))
    s2 = []
    for j in i.friends_sentiments.split("#"):
        s2.append(float(j))
    dist = earth_movers_distance(s1, s2)
    # print(dist)
    UserModel.objects.filter(id=i.id).update(tweets_distance=dist)

##
b = UserModel.objects.filter()
for i in b:
    s1 = []
    for j in i.friends_sentiments.split("#"):
        s1.append(float(j))
    s2 = []
    for j in i.images_sentiments.split("#"):
        s2.append(float(j))
    dist = earth_movers_distance(s1, s2)
    # print(dist)
    UserModel.objects.filter(id=i.id).update(images_distance=dist)
# # Example usage:
# set1 = [0.1, 0.1, 0.1, 0.1, 0.6]
# set2 = [0.15, 0.25, 0.25, 0.2, 0.15]

# distance = earth_movers_distance(set1, set2)
# print("Similarity", 1-distance)
