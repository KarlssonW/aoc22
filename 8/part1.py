import numpy as np

def main():
    with open("./input.txt", "r") as lines:
        lines = lines.read().splitlines()
        trees = []
        
        visibility = []
        
        for line in lines:
            trees.append(list(map(int,[*line])))
            visibility.append([False] * len(line))

        for y in range(len(trees)):
            maxl, maxu, maxr, maxd = -1, -1, -1, -1
            for x in range(len(trees[y])):
                if trees[x][y] > maxr:
                    maxr = trees[x][y]
                    visibility[x][y] = True
                if trees[-(y+1)][x] > maxd:
                    maxd = trees[-(y+1)][x]
                    visibility[-(y+1)][x] = True
                if trees[-(x+1)][-(y+1)] > maxl:
                    maxl = trees[-(x+1)][-(y+1)]
                    visibility[-(x+1)][-(y+1)] = True
                if trees[y][-(x+1)] > maxu:
                    maxu = trees[y][-(x+1)]
                    visibility[y][-(x+1)] = True
                    
        print(sum(line.count(True) for line in visibility))


if __name__ == "__main__":
    main()