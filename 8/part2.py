import math

def main():
    with open("./input.txt", "r") as lines:
        lines = lines.read().splitlines()
        trees = []
        score = []
        
        for line in lines:
            trees.append(list(map(int,[*line])))
            score.append([0] * len(line))
        size = len(trees)

        for y in range(size):
            for x in range(size):
                sight = [1,1,1,1]
                i = 1
                while x+i < size and trees[x+i][y] < trees[x][y]:
                    if x+i+1 != size: sight[0] += 1
                    i += 1
                i = 1
                while x-i >= 0 and trees[x-i][y] < trees[x][y]:
                    if x-i != 0: sight[1] += 1
                    i += 1
                i = 1
                while y+i < size and trees[x][y+i] < trees[x][y]:
                    if y+i+1 != size: sight[2] += 1
                    i += 1
                i = 1
                while y-i >= 0 and trees[x][y-i] < trees[x][y]:
                    if y-i != 0: sight[3] += 1
                    i += 1
                
                score[x][y] = math.prod(sight)
        
        print(score)
        print(max(max(line) for line in score))


if __name__ == "__main__":
    main()