def main():
    with open("./input.txt", "r") as rucksacks:
        rucksacks = rucksacks.read()
        priosum = 0

        for rucksackgroup in (rucksacks.splitlines()[p:p + 3] for p in range(0, len(rucksacks.splitlines()), 3)):
            badge = list(set(rucksackgroup[0]).intersection(*rucksackgroup[1:]))[0]

            if badge.isupper():
                priosum += ord(badge) - 38
            else:
                priosum += ord(badge) - 96

        print(priosum)


if __name__ == "__main__":
    main()