import sys
from utils.TrailerData import TrailerData

def getVolume(a, b, c):
    return a*b*c;

if __name__ == '__main__':
    td = TrailerData()

    print(getVolume(td.width, td.height, td.depth))
