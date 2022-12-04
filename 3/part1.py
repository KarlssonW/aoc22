def main():
    with open("./input.txt", "r") as rucksacks:
        priosum = 0

        for rucksack in rucksacks:
            c1, c2 = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
            duplicate = list(set(c1).intersection(c2))[0]

            if duplicate.isupper():
                priosum += ord(duplicate) - 38
            else:
                priosum += ord(duplicate) - 96

        print(priosum)


if __name__ == "__main__":
    main()