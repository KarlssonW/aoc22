import re

def main():
    with open("./input.txt", "r") as lines:
        lines = lines.read().splitlines()[1:]

        dirsizes = []
        dirsizes.append(sum_dir(dirsizes, lines))

        print([x for x in sorted(dirsizes) if x >= 30000000 - (70000000 - dirsizes[-1])][0])

def sum_dir(dirsizelist, lines):
    dirsum = 0
    while len(lines) > 0 and lines[0] != "$ cd ..":
        if re.match("\$ cd [a-z]+", lines[0]) != None:
            lines.pop(0)
            dirsum += sum_dir(dirsizelist, lines)
        elif re.match("[0-9]+", lines[0]) != None:
            dirsum += int(lines[0].split(" ")[0])
            lines.pop(0)
        else:
            lines.pop(0)
    if len(lines) > 0: lines.pop(0)
    dirsizelist.append(dirsum)
    return dirsum

if __name__ == "__main__":
    main()