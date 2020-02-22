import numpy as np
import pandas as pd


class knn(object):
    def __init__(self, data):
        self.data = data
        dataset = pd.read_csv("file.csv", names=[
            'energy1','homogeneity1','contrast1','correlation1',
            'energy2','homogeneity2','contrast2','correlation2',
            'energy3','homogeneity3','contrast3','correlation3',
            'energy4','homogeneity4','contrast4','correlation4',
            'label'
        ])
        x = dataset.drop(["label"], axis = 1)
        x.head()
        samples = np.array(x)
        from sklearn.neighbors import NearestNeighbors
        neigh = NearestNeighbors(radius=200)
        neigh.fit(samples)
        # print(self.data)
        rng = neigh.radius_neighbors(self.data)
        dist = np.asarray(rng[0][0])
        num = np.asarray(rng[1][0])
        dict = {}
        for i in range(len(dist)):
            dict.update({num[i]:dist[i]})
        dict = sorted(dict.items(), key=lambda x:x[1])
        self.list = []
        for rows in dataset.itertuples():
            my_list = [
                rows.energy1,rows.homogeneity1,rows.contrast1,rows.correlation1,
                rows.energy2,rows.homogeneity2,rows.contrast2,rows.correlation2,
                rows.energy3,rows.homogeneity3,rows.contrast3,rows.correlation3,
                rows.energy4,rows.homogeneity4,rows.contrast4,rows.correlation4, rows.label
                    ]
            self.list.append(my_list)
        for i in range(len(dict)):
            self.list[dict[i][0]].append(dict[i][1])
        self.list.sort(key=lambda x: float(x[17]))
