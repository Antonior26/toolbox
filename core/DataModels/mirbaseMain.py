__author__ = 'antonior'

import os




class MirBaseMain():
    def __init__(self, name, UR, RC, RC_adj, RPM_lib, RPM_total, coordinates, RPM_adj_lib, RPM_adj_total):
        self.Name = name
        self.RPM_lib=RPM_lib
        self.RPM_total=RPM_total
        self.RPM_adj_lib= RPM_adj_lib
        self.RPM_adj_total = RPM_adj_total
        self.coordinates = coordinates
        self.RC_adj = round(float(RC_adj), 2)
        self.RC = RC
        self.UR = UR
        self.align = name + "_" + "_".join(coordinates.split("#")[:2])

    def get_sorted_attr(self):
        return ["Name", "UR", "RC", "RC_adj", "coordinates","align"]

