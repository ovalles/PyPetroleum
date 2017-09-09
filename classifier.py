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

def hiercluscounter(a,max_numOfClust):
    t = np.array(a)

    if len(t) <=1:
       numElinClus = 1
    else:

        z = hac.linkage(t, 'single')
        if len(t) <=3:
            numOfClust = 2
        else:

            # Autocalculando the number of cluster
            knee = np.diff(z[::-1, 2], 2)
            
            # This method perform better number of cluster calc            
            numOfClust = knee.argmax() + 2
            print 'Number of Cluster 1st method', numOfClust
            
            # This method overestimate the number of cluster
            # I use the if a a threshold
            knee[knee.argmax()] = 0
            numOfClust = knee.argmax() + 2
            print 'Number of Cluster 2nd method', numOfClust
            if numOfClust > max_numOfClust:
                numOfClust = max_numOfClust
            

        # Determining the cluster label of each point
        clusLabel = hac.fcluster(z, numOfClust, 'maxclust') #4 is the number of cluster
        numElinClus = len(clusLabel[(clusLabel[len(clusLabel)-1] == clusLabel)])

    return numElinClus
