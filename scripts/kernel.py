import scipy as sp
from metrics import metrics
from batcher import batcher
from parser import parser

class kernel:

    def __init__(self, file_name, camp_dist): #maybe folder name instead of file_name
        self.camp_dist_array = camp_dist
        self.parser = parser('../data/xlsx/start.xlsx', '../data/csv/out.csv')
        self.pars()
        self.data = sp.genfromtxt(file_name, delimiter=',', dtype='|S10')
        self.metrics = metrics()
        self.batcher = batcher(self.data)
        self.tth = self.batcher.tth_create()

    def pars(self):
        self.parser.load_translit()
        self.parser.expand()
        self.parser.split()

    def comput_first(self):
        self.dist = self.metrics.first_metrics(self.camp_dist_array, self.tth)
        return self.dist



if __name__ == "__main__":
    camp_dist = sp.genfromtxt('../data/camp_dist.tsv', delimiter= '\t')
    krn = kernel('../data/data.tsv', camp_dist)
    krn.comput_first()
    print(krn.batcher.name_list)
    print(krn.metrics.distance)


