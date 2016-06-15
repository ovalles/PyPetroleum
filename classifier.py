# CHEAPOIL GAME :)

# By AJ Ovalles
# Made in Venezuela, 2016
# ovallesa@me.com


import numpy as np
import scipy.cluster.hierarchy as hac
import matplotlib.pyplot as plt
import pdb


def MeanCenter(cluster):
    xCenter = np.mean(cluster[0,:])
    yCenter = np.mean(cluster[1,:])
    meanCenter = np.array([xCenter,yCenter])
    
    return meanCenter



def DistCenter(point,cluster):
    
    meanCenter = MeanCenter(cluster)
    Dist = (((point[0]-meanCenter[0])**2)+((point[1]-meanCenter[1])**2))**(1/2)

    return Dist

def hiercluscounter(a,numOfClust):
    t = np.array(a)

    if len(t) <=1:
       numElinClus = 1
    else:

        z = hac.linkage(t, 'single')
        
        # Autocalculando the number of cluster 
        #knee = np.diff(z[::-1, 2], 2)
        #num_clust1 = knee.argmax() + 2
        #print 'Number of Cluster', num_clust1
        #knee[knee.argmax()] = 0
        #num_clust2 = knee.argmax() + 2
        #clusLabel = hac.fcluster(z, num_clust1, 'maxclust')

        # Determining the cluster label of each point
        clusLabel = hac.fcluster(z, numOfClust, 'maxclust') #4 is the number of cluster
        numElinClus = len(clusLabel[(clusLabel[len(clusLabel)-1] == clusLabel)])

    return numElinClus
