def main():
    with open("./input.txt", "r") as guide:

        rps = {
            'A' : 1,
            'B' : 2,
            'C' : 3,
            'X' : 1,
            'Y' : 2,
            'Z' : 3
        }

        score = 0

        for game in guide.read().splitlines():
            r = tuple(rps[x] for x in game.split(" "))

            if r[0] == r[1]:
                score += 3 + r[1]
            elif (r[0]%3) + 1 == r[1]:
                score += 6 + r[1]
            else:
                score += r[1]

        print(score)

if __name__ == "__main__":
    main()