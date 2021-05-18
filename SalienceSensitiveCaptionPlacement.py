import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-row", "--row", required=True, help="number of rows")
ap.add_argument("-col", "--col", required=False, help="number of columns")

args = vars(ap.parse_args())

m = int(args.get("row"))
n = int(args.get("col"))


COV = [[-1,-1,-1,-1],[-1,-1,-1,-1],[-1,-1,-1,-1]];


DIST = [[1000,1000,1000,1000],[1000,1000,1000,1000],[1000,1000,1000,1000]];
def placeGazeData():
    DIST[0][1] = 1
    DIST[0][2] = 2
    DIST[1][2] = 4
    DIST[1][3] = 1
    DIST[0][3] = 1

placeGazeData()

def dindVecGrid():
    for i in range(0,2):
        for j in range(0,3):
            print(DIST[i][j])

