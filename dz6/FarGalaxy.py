from math import sqrt

def dist(coord1, coord2):
    x1, y1, z1 = coord1
    x2, y2, z2 = coord2

    return sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)

gals = []

line = input()
while line != ".":
    x, y, z, name = line.split()
    coord = float(x), float(y), float(z)
    gals.append((coord, name))

    line = input()

gal1, gal2, max_dist = None, None, 0
for i in range(len(gals)):
    for j in range (i+1, len(gals)):
        val = dist(gals[i][0], gals[j][0])
        if val > max_dist:
            gal1, gal2, max_dist = gals[i][1], gals[j][1], val
            if gal1 > gal2:
                gal1, gal2 = gal2, gal1


print (gal1, gal2)