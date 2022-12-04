import re

def main():
    with open("./input.txt", "r") as assignments:
        overlapcount = 0

        for pair in assignments:
            s = list(map(int, re.split("[-,]", pair.strip())))

            if s[0] <= s[2] and s[1] >= s[3] or s[2] <= s[0] and s[3] >= s[1]:
                overlapcount += 1
        print(overlapcount)

if __name__ == "__main__":
    main()