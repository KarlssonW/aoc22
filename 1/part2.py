def main():
    f = open("./input.txt", "r")

    suml = 0
    sums = []

    for l in f:
        if l == "\n":
            sums.append(suml)
            suml = 0
        else:
            suml += int(l)

    sums.sort()
    print(sum(sums[-3:]))

if __name__ == "__main__":
    main()