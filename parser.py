import numpy as np
import os

filename = "benzene.smol";
def read(filename, directory = None):
    if directory:
        filename = os.path.join(directory, filename);
        
    with open(filename, "r") as f:
        atoms = []
        coordinates = []
        bonds = []
        orders = []
        for l in f.readlines():
            l = l.split()
            if filename.endswith(".mol"):
               condition_coordinates = len(l) > 14;
               condition_bond = len(l) > 5 and len(l) < 9;
            elif filename.endswith(".smol"):
                condition_coordinates = len(l) == 4;
                condition_bond = len(l) == 3;
            if condition_coordinates:
                coordinates.append([float(i) for i in l[:3]]);
                atoms.append(l[3]);
            elif condition_bond:
                bonds.append([int(i) for i in l[:2]])
                orders.append(int(l[2]))
    return atoms, coordinates, bonds;

print(read(filename))
