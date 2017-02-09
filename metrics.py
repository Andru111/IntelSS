import scipy as sp
import sys

class metrics:

    def __init__(self):
        print("metrics initialize")


    def first_metrics(self, camp_dist, tth):
        dist = sp.zeros((tth.__len__()))
        for i in range(tth.__len__()): #for all teachers
            for j in range(tth[i].__len__() - 1): #for all class
                dist[i] += camp_dist[int(tth[i][j][3]) - 1, int(tth[i][j+1][3]) - 1]


        self.distance = dist
        return dist